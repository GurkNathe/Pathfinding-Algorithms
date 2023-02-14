from queue import PriorityQueue
from .RP import heuristic, count_path


def branch_and_bound(grid: object):
    """
    Perform a Branch and Bound search from start to end.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """

    # Initialize counters and sets
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, grid.start))
    came_from = {}

    # Initialize dictionaries to store the g scores for each node
    g_score = {node: float("inf") for row in grid.grid for node in row}
    g_score[grid.start] = 0

    visited_nodes: int = 0
    path_size: int = 0

    while not open_set.empty():
        # Get the current node and distance from the open set
        dist, _, node = open_set.get()

        visited_nodes += 1

        # End the search if the current node is the end node
        if node.is_end():
            path_size = count_path(came_from, grid.end)
            break

        # Check the neighbors of the current node
        for neighbor in node.neighbors:
            temp_g_score = dist + heuristic("manhattan", neighbor, grid.end)

            if temp_g_score < g_score[neighbor]:
                g_score[neighbor] = temp_g_score
                came_from[neighbor] = node
                count += 1
                open_set.put((temp_g_score, count, neighbor))

    return visited_nodes, path_size