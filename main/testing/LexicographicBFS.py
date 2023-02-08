from .RP import count_path


def lex_bfs(visited_nodes: int, start: object):
    """
    Implements the Lexicographic Breadth-First Search (LexBFS) algorithm.

    Args:
        visited_nodes (int): Count of the number of nodes visited.
        start (start): The starting node.

    Returns:
        order (list): A list of nodes in the graph, in the order they were
            visited by LexBFS.
        levels (dict): A dictionary containing the level of each node in the
            breadth-first search tree.
        visited_nodes (int): Count of the number of nodes visited.
        parent (dict): A dictionary containing the parent of each node checked.
    """

    # Initialize the list to store the order of the vertices
    order = []

    # Initialize the dictionaries to store the levels and parents of
    # the vertices
    levels = {}
    parent = {}

    # Set the level of the starting vertex to 0 and its parent to None
    levels[start] = 0
    parent[start] = None

    # Initialize the counter and the queue
    level = 0
    Q = [start]

    # Run the algorithm until the queue is empty or the flag is set to False
    while Q:
        # Pop the first element from the queue
        current = Q.pop(0)

        visited_nodes += 1

        order.append(current)

        for neighbor in current.neighbors:
            # If neighbor has not been visited before
            if neighbor not in levels:
                # Set the level of neighbor to the current level + 1
                levels[neighbor] = level + 1
                parent[neighbor] = current
                Q.append(neighbor)
        level = level + 1

    return order, levels, visited_nodes, parent


def lbfs(grid: object):
    """
    Solves the shortest path problem using LexBFS.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        count_path (int): Length of the path found.
    """

    visited_nodes: int = 0

    # Run LexBFS to get the order of the vertices
    order, levels, temp_v_n, parent = lex_bfs(visited_nodes, grid.start)

    visited_nodes = temp_v_n

    if order is not False:
        # Initialize the distances dictionary
        distances = {node: float("inf") for row in grid.grid for node in row}
        distances[grid.start] = 0

        # Iterate through the vertices in the order produced by LexBFS
        for current in order:
            visited_nodes += 1
            # Update the distances of the neighbors of current
            for neighbor in current.neighbors:
                if distances[current] + 1 < distances[neighbor]:
                    distances[neighbor] = distances[current] + 1
                    parent[neighbor] = current

    return visited_nodes, count_path(parent, grid.end)
