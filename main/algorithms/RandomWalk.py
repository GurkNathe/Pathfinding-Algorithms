import pygame
import random
from .RP import check, get_unvisited_nodes


def reconstruct_path(came_from: list, current: object, draw: object):
    """
    Reconstructs the path from the starting node to the current node,
    by following the `came_from` dictionary.

    Args:
        came_from (List[Node]): list containing which nodes were checked
        current (Node): current node
        draw (function): function for drawing the search path on the grid

    Returns:
        None
    """

    for current in reversed(came_from):
        if not current.is_start():
            current.make_path()
            draw()


def rand_walk(grid: object):
    """
    Generates a random walk from the starting node to the goal node.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None
    """

    # Initialize the list of previous nodes and the current node
    came_from = []
    current = grid.start

    # Flag for continuing the search
    run = True

    # Flag for making the path
    make_path = True

    possible_nodes = get_unvisited_nodes(grid.start)

    maxed = []

    # Continue the search until the search is stopped or the goal is reached
    while run and len(possible_nodes) - 1 > len(maxed):
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
        if current.is_end() and make_path:
            reconstruct_path(came_from, grid.end, grid.draw)
            grid.end.make_end()
            break

        # Markup for drawing path with color change
        if not current.is_start():
            current.uncheck()

        grid.draw()

        if not current.is_start() and not current.been_checked:
            current.check()
        elif not current.is_start():
            current.mult_check(3)

        if current.color[0] <= 3 and not current in maxed:
            maxed.append(current)
