import re
from urllib.parse import urlparse
import json
import os


def is_url(string: str) -> bool:
    return True if re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                              string) else False


def is_ipv4_without_port(string: str) -> bool:
    return True if re.findall('^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$',
                              string) else False


def is_ipv4_with_port(string: str) -> bool:
    return True if re.findall('^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{1,4})(:[0-9]{1,4})?$',
                              string) else False


def parse_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            return json.loads(file.read())
    except Exception as e:
        print(f'[parse_file] | Error while reading {file_path} | Error: {e}')


def get_all_kv(d: dict) -> list:
    if isinstance(d, dict):
        for key, value in d.items():
            yield key, value
            if isinstance(value, dict):
                yield from get_all_kv(value)


def is_ipv4(string: str) -> bool:
    return is_ipv4_with_port(string) or is_ipv4_without_port(string)


def get_subdirectories(root_path: str) -> list:
    result = []
    for dir in os.listdir(root_path):
        result.append(dir)

    return result


def extract_host(url: str) -> str:
    parsed_url = urlparse(url)
    return parsed_url.hostname


def remove_host_and_protocol(url: str) -> str:
    parsed_url = urlparse(url)
    return parsed_url.path + ('?' + parsed_url.query if parsed_url.query else '') + (
        '#' + parsed_url.fragment if parsed_url.fragment else '')
