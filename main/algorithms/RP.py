import pygame
import math
from queue import Queue


# Manhattan distance
def manhattan(node1: object, node2: object):
    """
    Calculate the Manhattan distance between two nodes.

    Parameters:
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

    Parameters:
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

    Parameters:
        type (str): The type of heuristic distance to use.
            Valid options are "euclidean" and "manhattan".
        node1 (Node): The first node.
        node2 (Node): The second node.

    Returns:
        float: The heuristic distance between the two nodes.
    """
    match type:
        case "euclidean":
            return euclidean(node1, node2)
        case "manhattan":
            return manhattan(node1, node2)
        case _:
            return manhattan(node1, node2)


def reconstruct_path(came_from: object, current: object, draw: object):
    """
    Reconstructs the path from the start node to the end node in a maze.

    Parameters:
        came_from (Dict[Node, Node]): A dictionary containing the nodes traversed 
            during the pathfinding algorithm.
        current (Node): The end node of the path.
        draw (function): A function for drawing the maze.

    Returns:
        None
    """
    while current in came_from:
        if not came_from[current].is_start():
            current = came_from[current]
            current.make_path()
            draw()
        else:
            break


def get_unvisited_nodes(start: object):
    """
    Find all nodes connected to the start node in the grid.

    Parameters:
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


def check(events: list, run: bool):
    """
    Check for and handle user events such as quitting the program or 
    pausing the algorithm.

    Parameters:
        events (list): A list of pygame events.
        run (bool): A flag indicating whether the algorithm is currently running.

    Returns:
        bool: A flag indicating whether the algorithm is currently running.
    """
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            run = False
    
    return run

def markup(draw: object, current: object):
    """
    Mark the current node as visited and redraw the grid.

    Parameters:
        draw (function): A function that draws the grid to the pygame window.
        current (Node): The current node being visited.

    Returns:
        None
    """
    if not current.is_start() and not current.is_end():
        current.uncheck()

    draw()

    if not current.is_start() and not current.is_end():
        current.check()