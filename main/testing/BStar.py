from queue import PriorityQueue
from .RP import count_path, check, heuristic


def b_star(grid: object):
    """
    Perform a B* search from start to end.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        None
    """

    # Initialize counters and sets
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, grid.start))
    came_from = {}

    # Initialize dictionaries to store the g and f scores for each node
    g_score = {node: float("inf") for row in grid.grid for node in row}
    g_score[grid.start] = 0

    # Initialize a set to store the nodes in the open set
    open_set_hash = {grid.start}

    visited_nodes: int = 0
    path_size: int = 0

    # Perform the search
    while not open_set.empty():
        # Get the current node from the open set
        _, _, current = open_set.get()
        open_set_hash.remove(current)

        visited_nodes += 1

        # End the search if the current node is the end node
        if current.is_end():
            path_size = count_path(came_from, grid.end)
            break

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # Calculate the tentative g score for the neighbor
            temp_g_score = g_score[current] + 1

            # Update the g and f scores for the neighbor if the
            # tentative g score is lower
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score = temp_g_score + heuristic("d_manhattan", neighbor, grid.end)

                # Add the neighbor to the open set if it is not already there
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score, count, neighbor))
                    open_set_hash.add(neighbor)

    return visited_nodes, path_size