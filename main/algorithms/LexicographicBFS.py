import pygame
from .RP import markup, check, reconstruct_path


def LexBFS(draw: object, start: object):
    """
    Implements the Lexicographic Breadth-First Search (LexBFS) algorithm.

    Args:
        draw (function): The draw function to update the grid display.
        start (start): The starting node.

    Returns:
        order (list): A list of nodes in the graph, in the order they were
            visited by LexBFS.
        levels (dict): A dictionary containing the level of each node in the
            breadth-first search tree.
        parent (dict): A dictionary containing the parent of each node in the
            breadth-first search tree.
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

    # Set the flag to run the algorithm
    run = True

    # Run the algorithm until the queue is empty or the flag is set to False
    while Q and run:
        # Check if the flag to run the algorithm is set to False
        run = check(pygame.event.get(), run)

        # Pop the first element from the queue
        current = Q.pop(0)

        order.append(current)

        # Mark the node as visited
        markup(draw, current)

        for neighbor in current.neighbors:
            # If neighbor has not been visited before
            if neighbor not in levels:
                if not neighbor.is_start() and not neighbor.is_end():
                    neighbor.uncheck()
                # Set the level of neighbor to the current level + 1
                levels[neighbor] = level + 1
                parent[neighbor] = current
                Q.append(neighbor)
        level = level + 1

    # If the flag to run the algorithm is set to False, return False
    # for all outputs
    if not run:
        return False, False, False
    return order, levels, parent


def lbfs(grid: object):
    """
    Solves the shortest path problem using LexBFS.

    Args:
        grid (Grid): An object representing the current grid
    
    Returns:
        None
    """

    # Run LexBFS to get the order of the vertices
    order, levels, parent = LexBFS(grid.draw, grid.start)

    if order is not False:
        # Initialize the distances dictionary
        distances = {node: float("inf") for row in grid.grid for node in row}
        distances[grid.start] = 0

        # Iterate through the vertices in the order produced by LexBFS
        for current in order:
            # Update the distances of the neighbors of current
            for neighbor in current.neighbors:
                if distances[current] + 1 < distances[neighbor]:
                    distances[neighbor] = distances[current] + 1
                    parent[neighbor] = current

        reconstruct_path(parent, grid.end, grid.draw)
