import os
import json

from internal import models


def parse_file(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f'[parse_file] | Cannot read or serialize file {file_path}. Error: {e}')


def parse_all_files(root_path: str) -> list[dict]:
    result = []
    try:
        subdirectories = [x[0] for x in os.walk(root_path)]
        for directory in subdirectories:
            subdirectory_path = os.path.join(root_path, directory)
            if "config.json" in os.listdir(subdirectory_path):
                result.append(parse_file(os.path.join(subdirectory_path, "config.json")))
            else:
                print(f"[parse_all_files] | config.json in {subdirectory_path} does not exist, skipping")
    except Exception as e:
        print(f'[parse_all_files] | Error: {e}')

    return result


def create_graph(configs: list[dict]) -> models.Graph:
    for config in configs:
        pass
