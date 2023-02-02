from .RP import get_unvisited_nodes, check


def reconstruct_path(
    dist: list,
    V: int,
    start: object,
    end: object,
    nodes: list,
    checked_nodes: list,
):
    """
    Function to reconstruct a path from the start node to the end node based on
    the given distance matrix, list of nodes, and list of checked nodes.

    Parameters:
        draw (function): Function to draw the updated grid.
        dist (list): A 2D list representing the distance matrix between nodes.
        V (int): The number of nodes in the grid.
        start (Node): The starting node.
        end (Node): The ending node.
        nodes (list): A list of all nodes in the grid.
        checked_nodes (list): A list of nodes that have been visited during the search.

    Returns:
        bool: True if a path is found, False if not.
    """

    path_size: int = 0

    # If the end node is not in the list of nodes, return False
    try:
        test = nodes.index(end)
        if end not in checked_nodes:
            return -1
    except ValueError:
        return -2

    # Get the indices of the start and end nodes in the list of nodes
    u, v = nodes.index(start), nodes.index(end)

    # Initialize empty lists for the path, left-side distances,
    # and right-side distances
    path = []
    left = []
    right = []
    current = v

    # Iterate backwards through the distance matrix
    for k in range(V - 1, -1, -1):
        # If the distance between the start and end nodes is equal to the
        # distance between the start node and the k-th node plus the distance
        # between the k-th node and the end node, add the k-th node to the
        # path and add the coresponding distances to the left and right lists
        if dist[u][v] == dist[u][k] + dist[k][v]:
            # Only add the node to the path if it is not the start or end node
            # and its distance values are not already in the
            # left and right lists
            if (
                not nodes[k].is_start()
                and not nodes[k].is_end()
                and dist[u][k] not in left
                and dist[k][v] not in right
            ):
                path.append(nodes[k])
                left.append(dist[u][k])
                right.append(dist[k][v])
            current = k

    # Set the current node to the end node
    curr = end
    # Keep looping until the current node is the start node
    while curr != start:
        # Check each neighbor of the current node
        for node in curr.neighbors:
            # If the neighbor is the start node, return True
            if node.is_start():
                return path_size

            # If the neighbor is in the path, mark it as part of the path and
            # set the current node to the neighbor
            if node in path:
                path_size += 1
                path.remove(node)
                curr = node

    return path_size


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

    # Used for path reconstruction
    checked_nodes = [start]

    visited_nodes: int = 0

    # Initialize the distance values in the distance matrix
    for i in range(V):
        for j in range(V):
            visited_nodes += 1

            # If the nodes are neighbors, set the distance to 1
            if nodes[i] in nodes[j].neighbors:
                distance[i][j] = 1

    # If the two nodes are the same, set the distance to 0
    for i in range(V):
        visited_nodes += 1
        distance[i][i] = 0


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

                    # If none of the nodes are the start or end nodes, check them again
                    if (
                        not nodes[i].is_start()
                        and not nodes[i].is_end()
                        and not nodes[j].is_start()
                        and not nodes[j].is_end()
                        and not nodes[k].is_start()
                        and not nodes[k].is_end()
                    ):
                        checked_nodes.append(nodes[i])
                        checked_nodes.append(nodes[j])
                        checked_nodes.append(nodes[k])

    # Adding end if it is connected to start
    try:
        test = nodes.index(end)
        checked_nodes.append(end)
    except ValueError:
        pass

    return visited_nodes, reconstruct_path(
        distance, V, start, end, nodes, checked_nodes
    )
