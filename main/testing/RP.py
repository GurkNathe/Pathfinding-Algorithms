import pygame
import math
from queue import Queue


def determinant_2x2(matrix: list):
    """
    Determinant for a 2x2 matrix, used for divide by zero checking

    Args:
        matrix (list): covariance matrix between given points

    Returns:
        float: determinant
    """
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def covariance_matrix(point1: tuple, point2: tuple):
    """
    Calculates the covariance matrix for the given points

    Args:
        point1 (tuple): x, y coordinates for node 1
        point2 (tuple): x, y coordinates for node 2

    Returns:
        list: covariance matrix
    """
    x1, y1 = point1
    x2, y2 = point2
    
    cov_x_x = (x1 - x2) ** 2
    cov_y_y = (y1 - y2) ** 2
    cov_x_y = (x1 - x2) * (y1 - y2)

    return [[cov_x_x, cov_x_y], [cov_x_y, cov_y_y]]


# Mahalanobis distance
def mahalanobis(node1: object, node2: object):
    """
    Calculates the Mahalanobis distance between two nodes.

    Args:
        node1 (Node): The first node.
        node2 (Node): The second node.

    Returns:
        float: The Mahalanobis distance between the two nodes.
    """
    matrix = covariance_matrix(node1.get_pos(), node2.get_pos())

    # Checking for potential divide by zero errors
    if determinant_2x2(matrix) < 1e-10:
        return float("inf")

    # Getting the difference between the two nodes' respective x and y values
    diff = [a - b for a, b in zip(node1.get_pos(), node2.get_pos())]

    result = 0
    for i, d in enumerate(diff):
        result += d * d / matrix[i][i]
    return math.sqrt(result)


# Minkowski distance
def minkowski(node1: object, node2: object, p: int or float):
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()

    d1 = abs(x1 - x2)**p
    d2 = abs(y1 - y2)**p

    return (d1 + d2)**(1/p)


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


def heuristic(type: str, node1: object, node2: object, *args):
    """
    Calculate the heuristic distance between two nodes.

    Args:
        type (str): The type of heuristic distance to use.
            Valid options are "euclidean" and "manhattan".
        node1 (Node): The first node.
        node2 (Node): The second node.
        *args (list): additional arguments for different heuristics

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
        case "minkowski":
            return minkowski(node1, node2, args[0])
        case "mahalanobis":
            return mahalanobis(node1, node2)
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
