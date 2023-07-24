import pygame
from .RP import heuristic, markup, check

def reconstruct_path(cache: dict, current: object, draw: object):
    """
    Iterates through the cache and constructs the path using the data stored.

    Args:
        came_from (Dict[Node, Node]): A dictionary containing the nodes traversed
            during the pathfinding algorithm.
        current (Node): The end node of the path.
        draw (function): A function for drawing the maze.

    Returns:
        None
    """
    while not current.is_start():
        if not current.is_end():
            current.make_path()
        _, current = cache[current]
        draw()

def fringe_search(grid: object):
    """
    Performs a Fringe Search over the grid.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None: The function updates the screen with the search progress and path.
    """
    # Initialize data structures
    fringe = []
    cache = {}
    cache[grid.start] = (0, None)
    fringe.append(grid.start)

    f_limit = heuristic("manhattan", grid.start, grid.end)

    found = False
    run = True

    while not found and run and fringe:
        # Check for exit events
        run = check(pygame.event.get(), run)

        f_min = float("inf")

        # Check every node in the fringe
        for node in fringe:
            g, parent = cache[node]

            # Get f-score for current node
            f = g + heuristic("manhattan", node, grid.end)

            # Check if the f-score is greater than the allowed limit
            if f > f_limit:
                f_min = min(f, f_min)
                continue
            if node.is_end():
                reconstruct_path(cache, node, grid.draw)
                found = True
                break

            markup(grid.draw, node)

            for child in node.neighbors:
                g_child = g + 1
                # If the child node has already been seen
                if child in cache:
                    g_cached, c_parent = cache[child]
                    if g_child >= g_cached:
                        continue

                if child in fringe:
                    fringe.remove(child)
                fringe.append(child)
                cache[child] = (g_child, node)

                if not child.is_start() and not child.is_end():
                    child.uncheck()
            fringe.remove(node)
        f_limit = f_min