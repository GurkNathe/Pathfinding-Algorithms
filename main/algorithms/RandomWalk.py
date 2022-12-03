import pygame
import random

# TODO: Find a more efficient way to store path,
# TODO: causes drawing issues when path is too long
# TODO: Break condition when all locations are checked that can be (i.e. can't reach end)
def reconstruct_path(came_from, current, draw):
    for current in reversed(came_from):
        if not current.is_start():
            current.make_path()
            draw()


def rand_walk(draw, grid, start, end):
    came_from = []
    current = start
    run = True
    
    # Added for debugging purposes
    make_path = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                run = False

        neighbor = random.randint(0, len(current.neighbors) - 1)
        came_from.append(current)
        current = current.neighbors[neighbor]

        if current == end and make_path:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        if current != start:
            current.uncheck()

        draw()

        if current != start and not current.been_checked:
            current.check()
        elif current != start:
            current.mult_check(3)

    return False
