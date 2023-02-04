from .RP import check, count_path


def depth_limit(
    visited_nodes: int,
    current: object,
    end: object,
    depth: int,
    visited: set,
    path: dict,
):
    """
    Recursive DFS with a depth limit.

    Args:
        current (Node): Current node being visited.
        end (Node): Goal node.
        depth (int): Current depth of the search.
        visited (set): Set of nodes already visited.
        path (dict): Dictionary of parent nodes, used to reconstruct the path.

    Returns:
        dict: Dictionary of parent nodes, used to reconstruct the path.
            Returns an empty dictionary if no path is found.
    """
    if depth < 0:
        return {}, visited_nodes
    if current == end:
        return path, visited_nodes

    visited.add(current)

    visited_nodes += 1

    check(current)

    for neighbor in current.neighbors:
        if neighbor not in visited:
            path[neighbor] = current

            result, temp_v_n = depth_limit(
                visited_nodes, neighbor, end, depth - 1, visited, path
            )

            visited_nodes = temp_v_n

            if result:
                return result, visited_nodes

    return {}, visited_nodes


def iddfs(start: object, end: object, grid: list, length: int):
    """
    Iterative deepening DFS.

    Args:
        start (Node): Start node.
        end (Node): Goal node.
        grid (List[List[Node]]): List of nodes in the grid.
        length (int): Length of the grid.

    Returns:
        None
    """

    visited_nodes: int = 0
    path_size: int = 0

    for depth in range(0, length):
        visited = set()
        path, temp_v_n = depth_limit(
            visited_nodes, start, end, depth, visited, {start: None}
        )

        visited_nodes = temp_v_n

        if path:
            path_size = count_path(path, end)
            break
    return visited_nodes, path_size
