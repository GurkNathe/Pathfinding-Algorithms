from queue import Queue
from .RP import get_unvisited_nodes, check, count_path


def bell_ford(start: object, end: object, accuracy: float):
    """
    Perform a Bellman-Ford search from start to end with a given accuracy.

    Args:
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.
        accuracy (float): The fraction of nodes to visit at each step. (0, 1]

    Returns:
        None
    """

    # Get the list of unvisited nodes
    nodes = get_unvisited_nodes(start)

    # Initialize dictionaries to store the distance and predecessor for each node
    distance = {node: float("inf") for node in nodes}
    predecessor = {}

    # Set the distance of the start node to 0
    distance[start] = 0

    # Calculate the number of nodes to visit at each step
    counter = int((len(nodes) - 1) * accuracy)

    visited_nodes: int = 0

    # Perform the search
    while counter >= 0:
        # Visit each node
        for current in nodes:
            
            visited_nodes += 1
            
            check(current)
            
            # Check the neighbors of the current node
            for neighbor in current.neighbors:
                # Update the distance and predecessor for the neighbor if the
                # current distance is shorter
                if distance[current] + 1 < distance[neighbor]:
                    distance[neighbor] = distance[current] + 1
                    predecessor[neighbor] = current
        # Decrement the counter
        counter -= 1
    
    return visited_nodes, count_path(predecessor, end)