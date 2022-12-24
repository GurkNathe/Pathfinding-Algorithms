import pygame
from queue import PriorityQueue
from .RP import reconstruct_path, heuristic, check, markup


def gbls(draw, start, end, grid):
    """
    Modified version of the greedy best-first search algorithm that explores neighbors in the direction of the last chosen node
    as long as the estimated distance to the goal is shorter than the current node.

    Parameters:
        draw (function): A function used to draw the search on the screen.
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.
        grid (List[List[Node]]): grid containing the nodes

    Returns:
        None
    """

    # Initialize the priority queue with the starting node
    Q = PriorityQueue()
    Q.put((heuristic("euclidean", start, end), 0, start))

    # Initialize the counter and flags
    counter = 0
    run = True
    found = False

    previous = {}
    last_direction = None

    # Continue the search as long as there are nodes in the queue and the search
    # has not been stopped or the goal has not been found
    while not Q.empty() and run and not found:
        # Check for events that may stop the search
        run = check(pygame.event.get(), run)

        current = Q.get()[2]

        if current.is_checked():
            continue

        markup(draw, current)

        # Choose the neighbors in the last direction first,
        # if a direction has been chosen
        if last_direction:
            neighbors = [
                n
                for n in current.neighbors
                if n.get_pos()[0] - current.get_pos()[0] == last_direction[0]
                and n.get_pos()[1] - current.get_pos()[1] == last_direction[1]
            ]

            # Add the other neighbors to the list
            neighbors += [n for n in current.neighbors if n not in neighbors]
        # If no direction has been chosen, explore all neighbors
        else:
            neighbors = current.neighbors

        for neighbor in neighbors:
            if not neighbor.is_checked():
                if neighbor.is_end():
                    previous[neighbor] = current
                    found = True
                    break

                # Markup for drawing neighbor
                if not neighbor.is_start() and not neighbor.is_end():
                    neighbor.uncheck()

                counter += 1
                distance = heuristic("euclidean", neighbor, end)

                # Add the neighbor to the queue with the estimated
                # distance as the priority
                previous[neighbor] = current
                Q.put((distance, counter, neighbor))

                # Save the direction to the neighbor
                last_direction = (
                    neighbor.get_pos()[0] - current.get_pos()[0],
                    neighbor.get_pos()[1] - current.get_pos()[1],
                )

    reconstruct_path(previous, end, draw)
