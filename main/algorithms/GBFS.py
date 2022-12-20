import pygame
from queue import PriorityQueue
from .RP import reconstruct_path, heuristic, check, markup


def gbfs(draw, start, end):
    Q = PriorityQueue()
    Q.put((heuristic("manhattan", start, end), 0, start))

    counter = 0
    run = True
    found = False

    previous = {}

    while not Q.empty() and run and not found:
        run = check(pygame.event.get(), run)
        
        current = Q.get()

        if current[2].is_checked():
            continue

        markup(draw, current[2])

        largest = (None, None, None)
        for neighbor in current[2].neighbors:
            if not neighbor.is_checked():
                if neighbor.is_end():
                    previous[neighbor] = current[2]
                    found = True
                    break

                counter += 1
                distance = heuristic("manhattan", neighbor, end)
                largest = (distance, counter, neighbor)
                previous[largest[2]] = current[2]
                Q.put(largest)

    reconstruct_path(previous, end, draw)
