import pygame
from .RP import reconstruct_path, check, markup


def bfs(grid: object):
    """
    Perform a breadth-first search from start to end.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Initialize a list to store the nodes to visit (queue)
    nodes = []
    nodes.append(grid.start)

    # Initialize a dictionary to store the predecessor of each node
    previous = {}

    # Initialize flags to track the search status
    found = False
    run = True

    # Perform the search
    while nodes and not found and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Get the next node to visit
        current = nodes.pop(0)

        # Skip the node if it has already been checked
        if current.is_checked():
            continue

        # Draw the current node
        markup(grid.draw, current)

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # Skip the neighbor if it has already been checked
            if not neighbor.is_checked():
                # End the search if the neighbor is the end node
                if neighbor.is_end():
                    previous[neighbor] = current
                    found = True
                    reconstruct_path(previous, grid.end, grid.draw)
                    break
                # Add the neighbor to the list of nodes to visit if it is not the end node
                else:
                    previous[neighbor] = current
                    nodes.append(neighbor)

                    # Uncheck the child if it is not the start or end node
                    # for markup
                    if not neighbor.is_start() and not neighbor.is_end():
                        neighbor.uncheck()
