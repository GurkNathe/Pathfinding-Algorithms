import pygame
from queue import PriorityQueue
from .RP import reconstruct_path, heuristic, check


def b_star(draw: object, grid: list, start: object, end: object):
    """
    Perform a B* search from start to end.

    Args:
        draw (function): A function used to draw the search on the screen.
        grid (List[List[Node]]): The grid of nodes to search.
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Initialize counters and sets
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    # Initialize dictionaries to store the g and f scores for each node
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = heuristic("manhattan", start, end)

    # Initialize a set to store the nodes in the open set
    open_set_hash = {start}

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
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
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
                f_score[neighbor] = temp_g_score + heuristic("manhattan", neighbor, end)

                # Add the neighbor to the open set if it is not already there
                # and the neighbor isn't marked as forbidden
                if neighbor not in open_set_hash and not neighbor.is_forbidden():
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.uncheck()

        # Update the screen with the search progress
        draw()

        # Check the current node if it is not the start node
        if current != start:
            current.check()
