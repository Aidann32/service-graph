from dataclasses import dataclass
from enum import Enum


class NodeType(Enum):
    KAFKA = "kafka"
    DB = "db"
    REDIS = "redis"
    RABBIT = "rabbit"
    SERVICE = "service"


@dataclass
class Node:
    name: str
    type: NodeType
    description: str


@dataclass
class Relation:
    fromService: Node
    toService: Node


@dataclass
class Graph:
    name: str
    relations: list[Relation]
