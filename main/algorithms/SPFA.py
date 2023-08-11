import pygame
from queue import Queue
from .RP import check, markup, reconstruct_path

def spfa(grid: object):
    d = {node: float("inf") for row in grid.grid for node in row}
    d[grid.start] = 0

    queue = Queue()
    queue.put(grid.start)

    path = {}

    run = True

    while not queue.empty() and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Exit the loop if the user interrupted
        if not run:
            break

        u = queue.get()

        # Draw the current node
        markup(grid.draw, u)

        for v in u.neighbors:
            if d[u] + 1 < d[v]:
                # Update the distance and predecessor for the neighbor if the
                # current distance is shorter
                d[v] = d[u] + 1
                path[v] = u

                if v not in queue.queue:
                    queue.put(v)

                    # Uncheck the neighbor if it is not the start or end node
                    # for markup
                    if not v.is_end() and not v.is_start():
                        v.uncheck()

    if run:
        reconstruct_path(path, grid.end, grid.draw)