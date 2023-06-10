import pygame
from queue import PriorityQueue
from .RP import reconstruct_path, heuristic, check


def branch_and_bound(grid: object):
    """
    Perform a Branch and Bound search from start to end.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Initialize counters and sets
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, grid.start))
    came_from = {}

    # Initialize dictionaries to store the g scores for each node
    g_score = {node: float("inf") for row in grid.grid for node in row}
    g_score[grid.start] = 0

    # Initialize a flag to track whether the search should continue
    run = True

    # Perform the search
    while run and not open_set.empty():
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Get the current node and distance from the open set
        dist, _, node = open_set.get()

        # End the search if the current node is the end node
        if node.is_end():
            reconstruct_path(came_from, grid.end, grid.draw)
            break

        # Check the neighbors of the current node
        for neighbor in node.neighbors:
            # Calculate the tentative g score for the neighbor
            temp_g_score = dist + heuristic("manhattan", neighbor, grid.end)

            if temp_g_score < g_score[neighbor]:
                g_score[neighbor] = temp_g_score
                came_from[neighbor] = node
                count += 1
                open_set.put((temp_g_score, count, neighbor))

                if not neighbor.is_start() and not neighbor.is_end():
                    neighbor.uncheck()

        # Update the screen with the search progress
        grid.draw()

        # Check the current node if it is not the start node
        if not node.is_start():
            node.check()
