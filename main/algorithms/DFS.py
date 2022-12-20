import pygame
from .RP import reconstruct_path, check, markup


def dfs(draw, start, end):
    stack = [start]
    previous = {}

    found = False
    run = True

    while len(stack) and not found and run:
        run = check(pygame.event.get(), run)

        current = stack.pop()

        if current.is_checked():
            continue

        # Drawing stuff
        markup(draw, current)

        # Find unvisited neighbors and check for end
        for neighbor in current.neighbors:
            if not neighbor.is_checked():
                if neighbor.is_end():
                    previous[neighbor] = current
                    found = True
                    break
                else:
                    previous[neighbor] = current
                    stack.append(neighbor)

    reconstruct_path(previous, end, draw)
