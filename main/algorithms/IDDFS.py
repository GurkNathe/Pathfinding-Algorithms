import pygame
from .RP import check, markup, reconstruct_path


def depth_limit(draw: object, current: object, depth: int, visited: set, path: dict):
    """
    Recursive DFS with a depth limit.

    Args:
        draw (function): Function to draw the current state of the search.
        current (Node): Current node being visited.
        end (Node): Goal node.
        depth (int): Current depth of the search.
        visited (set): Set of nodes already visited.
        path (dict): Dictionary of parent nodes, used to reconstruct the path.

    Returns:
        dict: Dictionary of parent nodes, used to reconstruct the path.
            Returns an empty dictionary if no path is found.
    """
    if depth < 0:
        return {}
    if current.is_end():
        return path

    visited.add(current)

    markup(draw, current)

    for neighbor in current.neighbors:
        if neighbor not in visited:
            if not neighbor.is_start() and not neighbor.is_end():
                neighbor.uncheck()

            path[neighbor] = current

            result = depth_limit(draw, neighbor, depth - 1, visited, path)

            if result:
                return result

    return {}


def iddfs(grid: object, length: int):
    """
    Iterative deepening DFS.

    Args:
        grid (Grid): An object representing the current grid
        length (int): Length of the grid.

    Returns:
        None
    """
    run = True

    for depth in range(0, length):
        if not run:
            break

        run = check(pygame.event.get(), run)

        visited = set()
        path = depth_limit(grid.draw, grid.start, depth, visited, {grid.start: None})

        if path:
            reconstruct_path(path, grid.end, grid.draw)
            break
