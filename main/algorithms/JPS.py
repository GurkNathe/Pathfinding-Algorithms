import pygame
from .RP import heuristic, check, markup, reconstruct_path

def jps(grid: object):
    open_set = set([grid.start])
    closed_set = set()
    
    came_from = {}

    g_values = {grid.start: 0}
    f_values = {grid.start: heuristic("manhattan", grid.start, grid.end)}

    run = True

    while open_set and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Find the node with the lowest f-value in the open set.
        current = min(open_set, key=lambda node: f_values[node])

        if current.is_end():
            reconstruct_path(came_from, grid.end, grid.draw)
            break

        # Move current from open set to closed set
        open_set.remove(current)
        closed_set.add(current)

        markup(grid.draw, current)

        for neighbor in current.neighbors:
            # Check if neighbor is already closed
            if neighbor in closed_set:
                continue

            if neighbor not in open_set:
                g_value = g_values[current] + heuristic("manhattan", current, neighbor)

                g_values[neighbor] = g_value
                f_values[neighbor] = g_value + heuristic("manhattan", neighbor, grid.end)

                came_from[neighbor] = current
                open_set.add(neighbor)

                if not neighbor.is_start() and not neighbor.is_end():
                    neighbor.uncheck()