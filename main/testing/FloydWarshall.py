from .RP import get_unvisited_nodes, check


def floyd_warshall(start: object, end: object, grid: list):
    """
    Implements the Floyd-Warshall algorithm to find the shortest path between
    the start and end nodes in the given grid.

    Parameters:draw (function): A function used to draw the search on the screen.
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.
        grid (List[List[Node]]): The grid of nodes to search.

    Returns:
        None
    """

    # Get a list of all unvisited nodes, excluding the start node
    nodes = get_unvisited_nodes(start)

    # Get the number of nodes
    V = len(nodes)

    # Initialize the distance matrix with all values set to infinity
    distance = [[float("inf") for _ in range(V)] for _ in range(V)]

    visited_nodes: int = 0

    # Initialize the distance values in the distance matrix
    for i in range(V):
        for j in range(V):
            visited_nodes += 1
            # If the two nodes are the same, set the distance to 0
            if i == j:
                distance[i][j] = 0
            # If the nodes are neighbors, set the distance to 1
            elif nodes[i] in nodes[j].neighbors:
                distance[i][j] = 1

    # Iterate through all nodes in the list
    for k in range(V):
        # Iterate through all pairs of nodes in the list
        for i in range(V):
            for j in range(V):
                visited_nodes += 1
                # If the distance between the two nodes is currently longer than
                # the path through the k-th node, set it to the new shorter distance
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return visited_nodes