import pygame
from queue import PriorityQueue
from .RP import reconstruct_path, heuristic, check, markup


def gbfs(grid: object):
    """
    Perform a greedy best-first search from start to end.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Initialize priority queue with the start node
    Q = PriorityQueue()
    Q.put((heuristic("manhattan", grid.start, grid.end), 0, grid.start))

    # Initialize counters and flags
    counter = 0
    run = True
    found = False

    # Initialize a dictionary to store the previous nodes for each node
    previous = {}

    # Perform the search
    while not Q.empty() and run and not found:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Get the current node from the queue
        current = Q.get()[2]

        # Skip if the node has already been checked
        if current.is_checked():
            continue

        # Draw the current node
        markup(grid.draw, current)

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # Skip if the neighbor has already been checked
            if not neighbor.is_checked():
                # End the search if the neighbor is the end node
                if neighbor.is_end():
                    previous[neighbor] = current
                    found = True
                    break

                # Markup for drawing neighbor
                if not neighbor.is_start() and not neighbor.is_end():
                    neighbor.uncheck()

                # Add the neighbor to the queue
                counter += 1
                distance = heuristic("manhattan", neighbor, grid.end)
                previous[neighbor] = current
                Q.put((distance, counter, neighbor))

    # Draw the path from the end node to the start node
    if run:
        reconstruct_path(previous, grid.end, grid.draw)
