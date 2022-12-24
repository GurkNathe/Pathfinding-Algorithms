import pygame
import random
from .RP import check


def reconstruct_path(came_from, current, draw):
    """
    Reconstructs the path from the starting node to the current node,
    by following the `came_from` dictionary.

    Parameters:
        came_from (dict): dictionary mapping each node to its previous
            node in the path
        current (Node): current node
        draw (function): function for drawing the search path on the grid

    Returns:
        None
    """

    for current in reversed(came_from):
        if not current.is_start():
            current.make_path()
            draw()


def rand_walk(draw, start, end):
    """
    Generates a random walk from the starting node to the goal node.

    Parameters:
        draw (function): function for drawing the search path on the grid
        start (Node): starting node
        end (Node): goal node

    Returns:
        None
    """

    # Initialize the list of previous nodes and the current node
    came_from = []
    current = start

    # Flag for continuing the search
    run = True

    # Flag for making the path
    make_path = True

    # Continue the search until the search is stopped or the goal is reached
    while run:
        # Check for events that may stop the search
        run = check(pygame.event.get(), run)

        # Choose a random neighbor of the current node
        neighbor = random.randint(0, len(current.neighbors) - 1)

        # Add the current node to the list of previous nodes if it
        # has not already been added
        if current not in came_from:
            came_from.append(current)

        # Move to the chosen neighbor
        current = current.neighbors[neighbor]

        # If the current node is the goal node and the path has not
        # been made yet, reconstruct the path and make the goal node
        if current == end and make_path:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            break

        # Markup for drawing path with color change
        if current != start:
            current.uncheck()

        draw()

        if current != start and not current.been_checked:
            current.check()
        elif current != start:
            current.mult_check(3)
