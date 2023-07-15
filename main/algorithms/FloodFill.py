import pygame
import heapq
from .RP import check, markup

def flood_fill(grid: object):
    # Create a dictionary to store distance values
    distances = { node: float("inf") for row in grid for node in row }
    distances[grid.end] = 0

    # Start from end
    queue = [(0, grid.end)]
    run = True

    while queue and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        dist, current = heapq.heappop(queue)

        if current.is_checked():
            continue

        if current.is_start():
            break

        markup(grid.draw, current)

        # Check every neighbor of the current cell and 
        # add it to the queue if it hasn't been checked before
        for neighbor in current.neighbors:
            if not neighbor.is_checked():
                distances[neighbor] = dist + 1
                heapq.heappush(queue, (dist + 1, neighbor))

                if not neighbor.is_start() and not neighbor.is_end():
                    neighbor.uncheck()
    
    # Create path if the algorithm wasn't stopped
    if run:
        current = grid.start
        found = False
        while not found:
            best = (float("inf"), None)
            for neighbor in current.neighbors:
                if neighbor.is_end():
                    found = True
                    break
                if distances[neighbor] < best[0]: 
                    best = (distances[neighbor], neighbor)
            if not found:
                best[1].make_path()
                grid.draw()
                current = best[1]
