import pygame
from queue import PriorityQueue
from .RP import reconstruct_path, check, markup


def dijkstra(grid: object):
    """
    Perform Dijkstra's algorithm from start to end.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Initialize a priority queue to store the nodes to visit
    queue = PriorityQueue()

    # Set up the node values
    distance = {node: float("inf") for row in grid.grid for node in row}
    distance[grid.start] = 0

    # Holds the path from start to end
    previous = {}

    # Add the start node to the priority queue
    queue.put((0, 0, grid.start))
    count = 0

    # Initialize a flag to track the search status
    run = True

    # Perform the search
    while not queue.empty() and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Get the next node to visit
        current_distance, _, current_min = queue.get()

        # End the search if the current node is the end node
        if current_min.is_end():
            break

        # Draw the current node
        markup(grid.draw, current_min)

        # Check the neighbors of the current node
        for neighbor in current_min.neighbors:
            # Don't recheck for performance
            if not neighbor.is_checked():
                # edges between vertecies are not weighted
                # (using constant weight of 1)
                temp_value = distance[current_min] + 1
                if temp_value < distance[neighbor]:
                    distance[neighbor] = temp_value
                    previous[neighbor] = current_min

                    # Add the neighbor to the priority queue
                    count += 1
                    queue.put((distance[neighbor], count, neighbor))

                    # Uncheck the neighbor if it is not the start or end node
                    # for markup
                    if not neighbor.is_end() and not neighbor.is_start():
                        neighbor.uncheck()

    # Draw the path from the end node to the start node
    reconstruct_path(previous, grid.end, grid.draw)
