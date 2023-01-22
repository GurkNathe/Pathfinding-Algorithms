from queue import PriorityQueue
from .RP import heuristic, check


def get_checked_neighbors(node: object):
    """
    Get the neighbors of a node that have been checked or are the start node.

    Args:
        node (Node): The node to check.

    Returns:
        List[Node]: The list of checked or start neighbors.
    """

    checked = []
    for neighbor in node.neighbors:
        if neighbor.is_checked() or neighbor.is_start():
            checked.append(neighbor)
    return checked


def best_fs(start: object, end: object):
    """
    Perform a best-first search from start to end.

    Args:
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.

    Returns:
        None
    """

    # Initialize the priority queue with the start node
    queue = PriorityQueue()
    queue.put((0, 0, start))
    count = 0

    # Initialize a dictionary to store the cost of reaching each node from the start
    costs = {start: 0}
    
    visited_nodes: int = 0

    # Perform the search
    while not queue.empty():
        # Get the node with the lowest cost from the queue
        cost, _, current = queue.get()
        
        visited_nodes += 1

        # End the search if the current node is the end node
        if current == end:
            break

        check(current)

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # Calculate the cost of reaching the neighbor
            cost = costs[current] + 1

            # Update the cost in the dictionary if it is lower than the current value
            if neighbor not in costs or cost < costs[neighbor]:
                costs[neighbor] = cost
                # Add the neighbor to the queue with the calculated cost as the priority
                queue.put(
                    (cost + heuristic("manhattan", neighbor, end), count + 1, neighbor)
                )
    return visited_nodes