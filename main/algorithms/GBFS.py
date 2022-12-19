import pygame
from queue import PriorityQueue
from .RP import reconstruct_path, heuristic


def gbfs(draw, start, end):
    Q = PriorityQueue()
    Q.put((heuristic("manhattan", start, end), 0, start))

    counter = 0
    run = True
    found = False

    previous = {}

    while not Q.empty() and run and not found:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                run = False

        current = Q.get()

        if current[2].is_checked():
            continue

        if not current[2].is_start() and not current[2].is_end():
            current[2].uncheck()

        draw()

        if not current[2].is_start() and not current[2].is_end():
            current[2].check()

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
