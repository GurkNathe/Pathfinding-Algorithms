import pygame
from .RP import get_unvisited_nodes, check


def reconstruct_path(
    draw: object,
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
        dist (list): A 2D list representing the distance matrix between nodes.
        V (int): The number of nodes in the grid.
        start (Node): The starting node.
        end (Node): The ending node.
        nodes (list): A list of all nodes in the grid.
        checked_nodes (list): A list of nodes that have been visited during the search.

    Returns:
        int: size of path found
    """

    # If the end node is not in the list of nodes, return False
    try:
        test = nodes.index(end)
        if end not in checked_nodes:
            return 0
    except ValueError:
        return 0

    # Get the indices of the start and end nodes in the list of nodes
    u, v = nodes.index(start), nodes.index(end)

    # Initialize empty lists for the path, left-side distances,
    # and right-side distances
    path = []
    left = []
    right = []
    current = v
    path_size: int = 0

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
                break

            # If the neighbor is in the path, mark it as part of the path and
            # set the current node to the neighbor
            if node in path:
                path_size += 1
                path.remove(node)
                curr = node
    return path_size

def floyd_warshall(draw: object, start: object, end: object, grid: list):
    """
    Implements the Floyd-Warshall algorithm to find the shortest path between
    the start and end nodes in the given grid.

    Parameters:
        draw (function): A function used to draw the search on the screen.
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.
        grid (List[List[Node]]): The grid of nodes to search.

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Get a list of all unvisited nodes, excluding the start node
    nodes = get_unvisited_nodes(start)

    # Get the number of nodes
    V = len(nodes)

    # Initialize the distance matrix with all values set to infinity
    distance = [[float("inf") for _ in range(V)] for _ in range(V)]

    # Initialize the distance values in the distance matrix
    for i in range(V):
        for j in range(V):
            # If the two nodes are the same, set the distance to 0
            if i == j:
                distance[i][j] = 0
            # If the nodes are neighbors, set the distance to 1
            elif nodes[i] in nodes[j].neighbors:
                distance[i][j] = 1

    # Initialize a flag to run the algorithm
    run = True

    # Used for path reconstruction
    checked_nodes = [start]

    # Iterate through all nodes in the list
    for k in range(V):
        # If the run flag is False, break out of the loop
        if not run:
            break
        # Update the run flag based on the current event queue
        run = check(pygame.event.get(), run)

        # Iterate through all pairs of nodes in the list
        for i in range(V):
            for j in range(V):
                # If the distance between the two nodes is currently longer than
                # the path through the k-th node, set it to the new shorter distance
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

                    # If none of the nodes are the start or end nodes, uncheck them
                    if (
                        not nodes[i].is_start()
                        and not nodes[i].is_end()
                        and not nodes[j].is_start()
                        and not nodes[j].is_end()
                        and not nodes[k].is_start()
                        and not nodes[k].is_end()
                    ):
                        nodes[i].uncheck()
                        nodes[j].uncheck()
                        nodes[k].uncheck()

                    # Draw the updated distances
                    draw()

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
                        nodes[i].check()
                        nodes[j].check()
                        nodes[k].check()

    if run:
        # Adding end if it is connected to start
        try:
            test = nodes.index(end)
            checked_nodes.append(end)
        except ValueError:
            pass

        # Trace the shortest path through the distance matrix
        reconstruct_path(draw, distance, V, start, end, nodes, checked_nodes)
