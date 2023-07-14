from queue import PriorityQueue
from .RP import heuristic, check, count_path


def gbls(grid: object):
    """
    Modified version of the greedy best-first search algorithm that explores neighbors
    in the direction of the last chosen node as long as the estimated distance to the
    goal is shorter than the current node.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        count_path (int): Length of the path found.
    """

    # Initialize the priority queue with the starting node
    Q = PriorityQueue()
    Q.put((heuristic("manhattan", grid.start, grid.end), 0, grid.start))

    # Initialize the counter and flags
    counter = 0
    found = False

    previous = {}
    last_direction = None

    visited_nodes: int = 0

    # Continue the search as long as there are nodes in the queue or the goal has
    # not been found
    while not Q.empty() and not found:
        current = Q.get()[2]

        if current.is_checked():
            continue

        visited_nodes += 1

        check(current)

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
                    visited_nodes += 1
                    found = True
                    break

                counter += 1
                distance = heuristic("manhattan", neighbor, grid.end)

                # Add the neighbor to the queue with the estimated
                # distance as the priority
                previous[neighbor] = current
                Q.put((distance, counter, neighbor))

                # Save the direction to the neighbor
                last_direction = (
                    neighbor.get_pos()[0] - current.get_pos()[0],
                    neighbor.get_pos()[1] - current.get_pos()[1],
                )
    return visited_nodes, count_path(previous, grid.end)
