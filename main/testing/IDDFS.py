from .RP import count_path


def depth_limit(
    visited_nodes: int,
    current: object,
    depth: int,
    visited: set,
    path: dict,
):
    """
    Recursive DFS with a depth limit.

    Args:
        visited_nodes (int): Count of the number of nodes visited.
        current (Node): Current node being visited.
        depth (int): Current depth of the search.
        visited (set): Set of nodes already visited.
        path (dict): Dictionary of parent nodes, used to reconstruct the path.

    Returns:
        dict: Dictionary of parent nodes, used to reconstruct the path.
            Returns an empty dictionary if no path is found.
        visited_nodes (int): Count of the number of nodes visited.
    """
    if depth < 0:
        return {}, visited_nodes
    if current.is_end():
        visited_nodes += 1
        return path, visited_nodes

    visited.add(current)

    visited_nodes += 1

    for neighbor in current.neighbors:
        if neighbor not in visited:
            path[neighbor] = current

            result, temp_v_n = depth_limit(
                visited_nodes, neighbor, depth - 1, visited, path
            )

            visited_nodes = temp_v_n

            if result:
                return result, visited_nodes

    return {}, visited_nodes


def iddfs(grid: object, length: int):
    """
    Iterative deepening DFS.

    Args:
        grid (Grid): An object representing the current grid.
        length (int): Length of the grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """

    visited_nodes: int = 0
    path_size: int = 0

    for depth in range(0, length):
        visited = set()
        path, temp_v_n = depth_limit(
            visited_nodes, grid.start, depth, visited, {grid.start: None}
        )

        visited_nodes = temp_v_n

        if path:
            path_size = count_path(path, grid.end)
            break
    return visited_nodes, path_size
