from .RP import heuristic, count_path


def jps(grid: object):
    """
    Perform an Jump Point Search from start to end.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """

    open_set = set([grid.start])
    closed_set = set()

    came_from = {}

    g_values = {grid.start: 0}
    f_values = {grid.start: heuristic("manhattan", grid.start, grid.end)}

    visited_nodes: int = 0
    path_size: int = 0

    while open_set:
        # Find the node with the lowest f-value in the open set.
        current = min(open_set, key=lambda node: f_values[node])

        visited_nodes += 1

        if current.is_end():
            path_size = count_path(came_from, grid.end)
            break

        # Move current from open set to closed set
        open_set.remove(current)
        closed_set.add(current)

        for neighbor in current.neighbors:
            # Check if neighbor is already closed
            if neighbor in closed_set:
                continue

            if neighbor not in open_set:
                g_value = g_values[current] + heuristic("manhattan", current, neighbor)

                g_values[neighbor] = g_value
                f_values[neighbor] = g_value + heuristic(
                    "manhattan", neighbor, grid.end
                )

                came_from[neighbor] = current
                open_set.add(neighbor)
    return visited_nodes, path_size
