import pygame
from queue import Queue
from .RP import reconstruct_path, check, markup

"""
1. Add root node to the queue, and mark it as visited(already explored).
2. Loop on the queue as long as it's not empty.
   1. Get and remove the node at the top of the queue(current).
   2. For every non-visited child of the current node, do the following: 
       1. Mark it as visited.
       2. Check if it's the goal node, If so, then return it.
       3. Otherwise, push it to the queue.
3. If queue is empty, then goal node was not found!
"""


def bfs(draw, start, end):
    nodes = []
    nodes.append(start)

    previous = {}

    found = False
    run = True

    while nodes and not found and run:
        run = check(pygame.event.get(), run)

        current = nodes.pop(0)

        if current.is_checked():
            continue

        markup(draw, current)

        for neighbor in current.neighbors:
            if not neighbor.is_checked():
                if neighbor.is_end():
                    previous[neighbor] = current
                    found = True
                    break
                else:
                    previous[neighbor] = current
                    nodes.append(neighbor)

    reconstruct_path(previous, end, draw)
