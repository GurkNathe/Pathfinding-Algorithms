import pygame
from .RP import heuristic, reconstruct_path, markup, check


def search(draw, current, end, path, depth, cost, visited):
    if current.is_end():
        return True
    
    f = heuristic("euclidean", current, end) + depth
    
    if f > cost:
        return f

    visited.add(current)

    markup(draw, current)

    min_cost = float("inf")
    for neighbor in current.neighbors:
        if neighbor not in visited:
            path[neighbor] = current
            
            if not neighbor.is_start() and not neighbor.is_end():
                neighbor.uncheck()
            
            result = search(draw, neighbor, end, path, depth + 1, cost, visited)

            if result is True:
                return True

            min_cost = min(min_cost, result)
    return min_cost


def ida_star(draw, start, end):
    cost = heuristic("euclidean", start, end) + 1

    run = True
    
    path = {}

    while True and run:
        run = check(pygame.event.get(), run)
        
        result = search(draw, start, end, path, 0, cost, set())

        if result is True:
            reconstruct_path(path, end, draw)
            break
        if result is float("inf"):
            break

        cost = result
