import pygame
from queue import PriorityQueue
from .RP import reconstruct_path, heuristic, check, markup


def gbfs(draw: object, start: object, end: object):
    """
    Perform a greedy best-first search from start to end.

    Args:
        draw (function): A function used to draw the search on the screen.
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Initialize priority queue with the start node
    Q = PriorityQueue()
    Q.put((heuristic("manhattan", start, end), 0, start))

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
        markup(draw, current)

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
                distance = heuristic("manhattan", neighbor, end)
                previous[neighbor] = current
                Q.put((distance, counter, neighbor))

    # Draw the path from the end node to the start node
    reconstruct_path(previous, end, draw)
