from queue import PriorityQueue
from .RP import heuristic, check, count_path


def gbfs(grid: object):
    """
    Perform a greedy best-first search from start to end.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        count_path (int): Length of the path found.
    """

    # Initialize priority queue with the start node
    Q = PriorityQueue()
    Q.put((heuristic("manhattan", grid.start, grid.end), 0, grid.start))

    # Initialize counters and flags
    counter = 0
    found = False

    # Initialize a dictionary to store the previous nodes for each node
    previous = {}

    visited_nodes: int = 0

    # Perform the search
    while not Q.empty() and not found:
        # Get the current node from the queue
        _, _, current = Q.get()

        # Skip if the node has already been checked
        if current.is_checked():
            continue

        visited_nodes += 1

        # Draw the current node
        check(current)

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # Skip if the neighbor has already been checked
            if not neighbor.is_checked():
                # End the search if the neighbor is the end node
                if neighbor.is_end():
                    previous[neighbor] = current
                    visited_nodes += 1
                    found = True
                    break

                # Add the neighbor to the queue
                counter += 1
                distance = heuristic("manhattan", neighbor, grid.end)
                previous[neighbor] = current
                Q.put((distance, counter, neighbor))
    return visited_nodes, count_path(previous, grid.end)
