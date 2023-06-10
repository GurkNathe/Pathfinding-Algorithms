from queue import Queue
from .RP import get_unvisited_nodes, count_path


def bell_ford(grid: object, accuracy: float):
    """
    Perform a Bellman-Ford search from start to end with a given accuracy.

    Args:
        grid (Grid): An object representing the current grid.
        accuracy (float): The fraction of nodes to visit at each step. (0, 1]

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        count_path (int): Length of the path found.
    """

    # Get the list of unvisited nodes
    nodes = get_unvisited_nodes(grid.start)

    # Initialize dictionaries to store the distance and predecessor for each node
    distance = {node: float("inf") for node in nodes}
    predecessor = {}

    # Set the distance of the start node to 0
    distance[grid.start] = 0

    # Calculate the number of nodes to visit at each step
    counter = int((len(nodes) - 1) * accuracy)

    visited_nodes: int = 0

    # Perform the search
    while counter >= 0:
        # Visit each node
        for current in nodes:

            visited_nodes += 1

            # Check the neighbors of the current node
            for neighbor in current.neighbors:
                # Update the distance and predecessor for the neighbor if the
                # current distance is shorter
                if distance[current] + 1 < distance[neighbor]:
                    distance[neighbor] = distance[current] + 1
                    predecessor[neighbor] = current
        # Decrement the counter
        counter -= 1

    return visited_nodes, count_path(predecessor, grid.end)
