import pygame
from queue import Queue
from .RP import reconstruct_path, get_unvisited_nodes, check, markup


def bell_ford(draw, start, end, accuracy):
    nodes = get_unvisited_nodes(start)

    distance = {node: float("inf") for node in nodes}
    predecessor = {}

    distance[start] = 0
    counter = int((len(nodes) - 1) * accuracy)
    run = True

    while counter >= 0 and run:
        run = check(pygame.event.get(), run)

        for current in nodes:
            if not run:
                break
            run = check(pygame.event.get(), run)

            markup(draw, current)

            for neighbor in current.neighbors:
                if distance[current] + 1 < distance[neighbor]:
                    distance[neighbor] = distance[current] + 1
                    predecessor[neighbor] = current
        counter -= 1

    reconstruct_path(predecessor, end, draw)
