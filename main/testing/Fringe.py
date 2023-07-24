from .RP import heuristic

def count_path(cache: dict, current: object):
    """
    Counts the path size.

    Args:
        cache (dict): the cache of nodes in the grid that were visited
        current (Node): the ending node

    Returns:
        path (int): path size
    """
    path = -1
    while not current.is_start():
        path += 1
        _, current = cache[current]
    return path

def fringe_search(grid: object):
    """
    Performs a Fringe Search over the grid.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """
    fringe = []
    cache = {}
    cache[grid.start] = (0, None)
    fringe.append(grid.start)

    f_limit = heuristic("manhattan", grid.start, grid.end)

    found = False

    visited_nodes: int = 0
    path_size: int = 0

    while not found  and fringe:
        f_min = float("inf")
        # Check every node in the fringe
        for node in fringe:
            g, parent = cache[node]
            # Get f-score for current node
            f = g + heuristic("manhattan", node, grid.end)
            # Check if the f-score is greater than the allowed limit
            if f > f_limit:
                f_min = min(f, f_min)
                continue

            visited_nodes += 1

            if node.is_end():
                path_size = count_path(cache, node)
                found = True
                break

            for child in node.neighbors:
                g_child = g + 1
                # If the child node has already been seen
                if child in cache:
                    g_cached, c_parent = cache[child]
                    if g_child >= g_cached:
                        continue
                if child in fringe:
                    fringe.remove(child)
                fringe.append(child)
                cache[child] = (g_child, node)
            fringe.remove(node)
        f_limit = f_min
    return visited_nodes, path_size