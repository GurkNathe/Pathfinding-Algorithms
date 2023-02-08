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


def count_path(current: object, costs: dict):
    """
    Reconstruct the path from the end node to the start node.

    Args:
        current (Node): The current node in the search.
        costs (Dict[Node, int]): The cost of reaching each node from the start.

    Returns:
        path_size (int): Length of the path found.
    """
    path_size: int = 0

    # Continue until the current node is the start node
    while not current.is_start():
        # Find the neighbor with the lowest cost
        current = min(get_checked_neighbors(current), key=lambda x: costs[x])

        # Break if the current node is the start node
        if current.is_start():
            break
        path_size += 1
    return path_size


def best_fs(grid: object):
    """
    Perform a best-first search from start to end.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """

    # Initialize the priority queue with the start node
    queue = PriorityQueue()
    queue.put((0, 0, grid.start))
    count = 0

    # Initialize a dictionary to store the cost of reaching each node from the start
    costs = {grid.start: 0}

    visited_nodes: int = 0
    path_size: int = 0

    # Perform the search
    while not queue.empty():
        # Get the node with the lowest cost from the queue
        cost, _, current = queue.get()

        visited_nodes += 1

        # End the search if the current node is the end node
        if current.is_end():
            path_size = count_path(current, costs)
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
                    (cost + heuristic("manhattan", neighbor, grid.end), count + 1, neighbor)
                )
    return visited_nodes, path_size
