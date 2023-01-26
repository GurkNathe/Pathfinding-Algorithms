from queue import PriorityQueue
from .RP import heuristic, check, count_path


def gbfs(start: object, end: object):
    """
    Perform a greedy best-first search from start to end.

    Args:
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.

    Returns:
        None
    """

    # Initialize priority queue with the start node
    Q = PriorityQueue()
    Q.put((heuristic("manhattan", start, end), 0, start))

    # Initialize counters and flags
    counter = 0
    found = False

    # Initialize a dictionary to store the previous nodes for each node
    previous = {}

    visited_nodes: int = 0

    # Perform the search
    while not Q.empty() and not found:
        # Get the current node from the queue
        current = Q.get()[2]

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
                    found = True
                    break

                # Add the neighbor to the queue
                counter += 1
                distance = heuristic("manhattan", neighbor, end)
                previous[neighbor] = current
                Q.put((distance, counter, neighbor))
    return visited_nodes, count_path(previous, end)