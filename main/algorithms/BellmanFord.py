import pygame
from queue import Queue
from .RP import reconstruct_path, get_unvisited_nodes


def bell_ford(draw, start, end, accuracy):
    nodes = get_unvisited_nodes(start)

    distance = {node: float("inf") for node in nodes}
    predecessor = {}

    distance[start] = 0
    counter = int((len(nodes) - 1) * accuracy)
    run = True

    while counter >= 0 and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                run = False
        
        for current in nodes:
            if not run:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    run = False
                    break
                
            if not current.is_start() and not current.is_end():
                current.uncheck()

            draw()

            if not current.is_start() and not current.is_end():
                current.check()

            for neighbor in current.neighbors:
                if distance[current] + 1 < distance[neighbor]:
                    distance[neighbor] = distance[current] + 1
                    predecessor[neighbor] = current
        counter -= 1

    reconstruct_path(predecessor, end, draw)
