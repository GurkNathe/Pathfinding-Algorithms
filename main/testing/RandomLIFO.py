import pygame
import random
from queue import LifoQueue
from .RP import count_path

def rand_lifo(grid: object):
    """
    Runs a Random search on the grid using a LIFO Queue
    to choose the next node to check.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """
    # Initialize path and queue
    came_from = {}
    queue = LifoQueue()
    queue.put(grid.start)

    visited_nodes: int = 0
    path_size: int = 0

    # Run search till queue is empty
    while not queue.empty():
        current = queue.get()

        visited_nodes += 1

        # End search if target is found
        if current.is_end():
            path_size = count_path(came_from, current)
            break

        if not current.is_start():
            current.check()

        # Choose a random neighbor of the current node
        next_node = random.randint(0, len(current.neighbors) - 1)

        # Add every possible neighbor to the queue in the correct order
        for index, neighbor in enumerate(current.neighbors):
            if neighbor.is_checked():
                continue

            came_from[neighbor] = current
            if index != next_node:
                queue.put(neighbor)

        if not current.neighbors[next_node].is_checked():
            queue.put(current.neighbors[next_node])
    return visited_nodes, path_size