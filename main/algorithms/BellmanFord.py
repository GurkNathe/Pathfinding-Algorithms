import pygame
from queue import Queue
from .RP import reconstruct_path, get_unvisited_nodes, check, markup


def bell_ford(draw: object, start: object, end: object, accuracy: float):
    """
    Perform a Bellman-Ford search from start to end with a given accuracy.

    Args:
        draw (function): A function used to draw the search on the screen.
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.
        accuracy (float): The fraction of nodes to visit at each step. (0, 1]

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Get the list of unvisited nodes
    nodes = get_unvisited_nodes(start)

    # Initialize dictionaries to store the distance and predecessor for each node
    distance = {node: float("inf") for node in nodes}
    predecessor = {}

    # Set the distance of the start node to 0
    distance[start] = 0

    # Calculate the number of nodes to visit at each step
    counter = int((len(nodes) - 1) * accuracy)

    # Initialize a flag to track whether the search should continue
    run = True

    # Perform the search
    while counter >= 0 and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Visit each node
        for current in nodes:
            # Exit the loop if the user interrupted
            if not run:
                break
            # Check for exit events
            run = check(pygame.event.get(), run)

            # Draw the current node
            markup(draw, current)

            # Check the neighbors of the current node
            for neighbor in current.neighbors:
                # Update the distance and predecessor for the neighbor if the
                # current distance is shorter
                if distance[current] + 1 < distance[neighbor]:
                    distance[neighbor] = distance[current] + 1
                    predecessor[neighbor] = current

                    # Uncheck the neighbor if it is not the start or end node
                    # for markup
                    if not neighbor.is_end() and not neighbor.is_start():
                        neighbor.uncheck()

        # Decrement the counter
        counter -= 1

    # Draw the path from the end node to the start node
    reconstruct_path(predecessor, end, draw)
