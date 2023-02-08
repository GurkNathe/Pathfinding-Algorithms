import random


def rand_walk(grid: object):
    """
    Generates a random walk from the starting node to the goal node.

    Parameters:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """

    # Initialize the list of previous nodes and the current node
    came_from = []
    current = grid.start

    visited_nodes: int = 0

    # Continue the search until the goal is reached
    while True:
        # Choose a random neighbor of the current node
        neighbor = random.randint(0, len(current.neighbors) - 1)

        # Add the current node to the list of previous nodes if it
        # has not already been added
        if current not in came_from:
            came_from.append(current)

        # Move to the chosen neighbor
        current = current.neighbors[neighbor]

        visited_nodes += 1

        if current.is_end():
            break
    return visited_nodes, len(came_from) - 1
