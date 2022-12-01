import pygame
import random
import time


def reconstruct_path(came_from, current, draw):
    for current in reversed(came_from):
        if not current.is_start():
            current.make_path()
            draw()


def rand_walk(draw, grid, start, end):
    came_from = []
    current = start

    while current != end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        neighbor = random.randint(0, len(current.neighbors) - 1)
        came_from.append(current)
        current = current.neighbors[neighbor]

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        if current != start:
            current.uncheck()

        draw()

        if current != start:
            current.check()

    return False
