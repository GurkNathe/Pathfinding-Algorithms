from .RP import heuristic


def ida_star(grid: object):
    """
    Implements the IDA* search algorithm.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """
    bound = heuristic("manhattan", grid.start, grid.end)

    # Stack for path being searched
    path = [grid.start]

    visited_nodes: int = 0

    while True:
        result, temp_v_n = search(visited_nodes, path, 0, bound, grid.end)

        visited_nodes = temp_v_n

        if result is True:
            break
        if result is float("inf"):
            break

        bound = result

    return visited_nodes, len(path) - 2


def search(visited_nodes: int, path: list, g: int, bound: float, end: object):
    """
    Recursive search function used by the IDA* algorithm.

    Args:
        visited_nodes (int): Count of the number of nodes visited.
        path (list): The list of nodes representing the path taken by the
            search algorithm.
        g (int): The cost of the path represented by the list of nodes.
        bound (float): The bound on the cost of the path.
        end (Node): The ending node.
    Returns:
        True or f (boolean or float): 
            end was reached;
            g-score + heuristic is greater than current depth (bound)
        min_val (float): minimum value for the path
    """
    # Get last node in path
    node = path[-1]

    visited_nodes += 1

    # Calculate the f-score
    f = g + heuristic("manhattan", node, end)

    if f > bound:
        return f, visited_nodes
    if node.is_end():
        return True, visited_nodes

    min_val = float("inf")
    for neighbor in node.neighbors:
        if neighbor not in path:
            path.append(neighbor)
            result, temp_v_n = search(visited_nodes, path, g + 1, bound, end)
            visited_nodes = temp_v_n
            if result is True:
                return True, visited_nodes
            if result < min_val:
                min_val = result

            path.pop()
    return min_val, visited_nodes
