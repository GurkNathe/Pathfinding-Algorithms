import pygame
from collections import deque
from .RP import heuristic


def get_checked_neighbors(node):
    checked = []
    for neighbor in node.neighbors:
        if neighbor.is_checked() or neighbor.is_start():
            checked.append(neighbor)
    return checked


def reconstruct_path(current, costs, draw):
    while not current.is_start():
        current = min(get_checked_neighbors(current), key=lambda x: costs[x])

        if current.is_start():
            break

        current.make_path()
        draw()


# TODO: implement using a PriorityQueue
def best_fs(draw, start, end):
    queue = deque([start])

    costs = {start: 0}

    run = True

    while len(queue) > 0 and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                run = False

        current = min(
            queue, key=lambda x: costs[x] + heuristic("manhattan", x, end)
        )
        queue.remove(current)

        if current == end:
            reconstruct_path(current, costs, draw)
            end.make_end()
            break

        # Drawing stuff
        if current != start:
            current.uncheck()

        draw()

        if current != start:
            current.check()

        for neighbor in current.neighbors:
            cost = costs[current] + 1
            if neighbor not in costs or cost < costs[neighbor]:
                costs[neighbor] = cost
                queue.append(neighbor)
