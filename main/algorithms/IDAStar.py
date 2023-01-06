import pygame
from .RP import heuristic, markup, check


def reconstruct_path(draw: object, path: list):
    """
    Reconstructs the path taken by the search algorithm and marks the
    path on the grid.

    Parameters:
        draw (function): The draw function to update the grid display.
        path (list): The list of nodes representing the path taken by
            the search algorithm.

    Returns:
        None
    """
    for node in path:
        if not node.is_start() and not node.is_end():
            node.make_path()
            draw()


def ida_star(draw: object, start: object, end: object):
    """
    Implements the IDA* search algorithm.

    Parameters:
        draw (function): The draw function to update the grid display.
        start (Node): The starting node.
        end (Node): The ending node.

    Returns:
        None
    """
    bound = heuristic("manhattan", start, end)

    # Stack for path being searched
    path = [start]

    run = True

    while True and run:
        run = check(pygame.event.get(), run)

        result = search(draw, path, 0, bound, end)

        if result is True:
            path.reverse()
            reconstruct_path(draw, path)
            break
        if result is float("inf"):
            break

        bound = result


def search(draw: object, path: list, g: int, bound: float, end: object):
    """
    Recursive search function used by the IDA* algorithm.

    Parameters:
        draw (function): The draw function to update the grid display.
        path (list): The list of nodes representing the path taken by the
            search algorithm.
        g (int): The cost of the path represented by the list of nodes.
        bound (float): The bound on the cost of the path.
        end (Node): The ending node.
    Returns:
        True (boolean): end was reached
        f (float): g-score + heuristic is greater than current depth (bound)
        min_val (float): minimum value for the path
    """
    # Get last node in path
    node = path[-1]

    # Calculate the f-score
    f = g + heuristic("manhattan", node, end)

    if f > bound:
        return f
    if node.is_end():
        return True

    markup(draw, node)

    min_val = float("inf")
    for neighbor in node.neighbors:
        if neighbor not in path:
            if not neighbor.is_start() and not neighbor.is_end():
                neighbor.uncheck()

            path.append(neighbor)
            result = search(draw, path, g + 1, bound, end)

            if result is True:
                return True
            if result < min_val:
                min_val = result

            path.pop()
    return min_val
