import pygame
from .RP import reconstruct_path, check, markup


def dfs(draw: object, start: object, end: object):
    """
    Perform a depth-first search from start to end.

    Args:
        draw (function): A function used to draw the search on the screen.
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Initialize a stack to store the nodes to visit
    stack = [start]

    # Initialize a dictionary to store the predecessor of each node
    previous = {}

    # Initialize flags to track the search status
    found = False
    run = True

    # Perform the search
    while len(stack) and not found and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Get the next node to visit
        current = stack.pop()

        # Skip the node if it has already been checked
        if current.is_checked():
            continue

        # Draw the current node
        markup(draw, current)

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # Skip the neighbor if it has already been checked
            if not neighbor.is_checked():
                # End the search if the neighbor is the end node
                if neighbor.is_end():
                    previous[neighbor] = current
                    found = True
                    break
                # Add the neighbor to the stack of nodes to visit if it is not the end node
                else:
                    previous[neighbor] = current
                    stack.append(neighbor)
                    # Uncheck the neighbor if it is not the start or end node
                    # for markup
                    if not neighbor.is_start():
                        neighbor.uncheck()

    # Draw the path from the end node to the start node
    reconstruct_path(previous, end, draw)
