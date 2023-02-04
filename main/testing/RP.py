import pygame
import math
from queue import Queue


# Chebyshev distance
def chebyshev(node1: object, node2: object):
    """
    Calculate the Chebyshev distance between two nodes.

    Args:
        node1 (Node): The first node.
        node2 (Node): The second node.

    Returns:
        int: The Chebyshev distance between the two nodes.
    """
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()

    return max(abs(x1 - x2), abs(y1 - y2))


# Manhattan distance
def manhattan(node1: object, node2: object):
    """
    Calculate the Manhattan distance between two nodes.

    Args:
        node1 (Node): The first node.
        node2 (Node): The second node.

    Returns:
        int: The Manhattan distance between the two nodes.
    """
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()

    return abs(x1 - x2) + abs(y1 - y2)


# Euclidean distance
def euclidean(node1: object, node2: object):
    """
    Calculate the Euclidean distance between two nodes.

    Args:
        node1 (Node): The first node.
        node2 (Node): The second node.

    Returns:
        float: The Euclidean distance between the two nodes.
    """
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def heuristic(type: str, node1: object, node2: object):
    """
    Calculate the heuristic distance between two nodes.

    Args:
        type (str): The type of heuristic distance to use.
            Valid options are "euclidean" and "manhattan".
        node1 (Node): The first node.
        node2 (Node): The second node.

    Returns:
        float: The heuristic distance between the two nodes.
    """
    match type:
        case "chebyshev":
            return chebyshev(node1, node2)
        case "euclidean":
            return euclidean(node1, node2)
        case "manhattan":
            return manhattan(node1, node2)
        case _:
            return manhattan(node1, node2)


def get_unvisited_nodes(start: object):
    """
    Find all nodes connected to the start node in the grid.

    Args:
        start (Node): The starting node.

    Returns:
        List[Node]: A list of nodes connected to the start node.
    """
    Q = Queue()
    Q_hash = [start]
    Q.put(start)

    while not Q.empty():
        current = Q.get()

        for neighbor in current.neighbors:
            if neighbor not in Q_hash:
                Q.put(neighbor)
                Q_hash.append(neighbor)
    return Q_hash


def check(current: object):
    """
    Mark the current node as visited.

    Args:
        current (Node): The current node being visited.

    Returns:
        None
    """
    if not current.is_start() and not current.is_end():
        current.check()


def count_path(came_from: dict, current: object):
    num_nodes_path = 0

    while current in came_from:
        if not came_from[current].is_start():
            current = came_from[current]
            num_nodes_path += 1
        else:
            break

    return num_nodes_path
