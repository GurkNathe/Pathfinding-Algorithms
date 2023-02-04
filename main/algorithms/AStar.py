import pygame
from queue import PriorityQueue
from .RP import reconstruct_path, heuristic, check


def a_star(grid: object):
    """
    Perform an A* search from start to end.

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

    # Initialize dictionaries to store the g and f scores for each node
    g_score = {node: float("inf") for row in grid.grid for node in row}
    g_score[grid.start] = 0
    f_score = {node: float("inf") for row in grid.grid for node in row}
    f_score[grid.start] = heuristic("manhattan", grid.start, grid.end)

    # Initialize a set to store the nodes in the open set
    open_set_hash = {grid.start}

    # Initialize a flag to track whether the search should continue
    run = True

    # Perform the search
    while not open_set.empty() and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Get the current node from the open set
        current = open_set.get()[2]
        open_set_hash.remove(current)

        # End the search if the current node is the end node
        if current.is_end():
            reconstruct_path(came_from, grid.end, grid.draw)
            grid.end.make_end()
            break

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # Calculate the tentative g score for the neighbor
            temp_g_score = g_score[current] + 1

            # Update the g and f scores for the neighbor if the
            # tentative g score is lower
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(
                    "manhattan", neighbor, grid.end
                )

                # Add the neighbor to the open set if it is not already there
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)

                    if not neighbor.is_start() and not neighbor.is_end():
                        neighbor.uncheck()

        # Update the screen with the search progress
        grid.draw()

        # Check the current node if it is not the start node
        if not current.is_start():
            current.check()
