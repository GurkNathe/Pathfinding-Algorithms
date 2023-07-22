import pygame
import random
from queue import LifoQueue
from .RP import check, markup, reconstruct_path

def rand_lifo(grid: object):
    """
    Runs a Random search on the grid using a LIFO Queue
    to choose the next node to check.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None: The function updates the screen with the search progress and path.
    """
    # Initialize path and queue
    came_from = {}
    queue = LifoQueue()
    queue.put(grid.start)

    run = True

    # Run search till queue is empty
    while not queue.empty() and run:
        # Check for events that may stop the search
        run = check(pygame.event.get(), run)

        current = queue.get()

        # End search if target is found
        if current.is_end():
            reconstruct_path(came_from, current, grid.draw)
            break

        markup(grid.draw, current)

        # Choose a random neighbor of the current node
        next_node = random.randint(0, len(current.neighbors) - 1)

        # Add every possible neighbor to the queue in the correct order
        for index, neighbor in enumerate(current.neighbors):
            if neighbor.is_checked():
                continue
            came_from[neighbor] = current
            if index != next_node:
                queue.put(neighbor)
            if not neighbor.is_start() and not neighbor.is_end():
                neighbor.uncheck()

        if not current.neighbors[next_node].is_checked():
            queue.put(current.neighbors[next_node])