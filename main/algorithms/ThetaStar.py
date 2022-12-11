import pygame
import math
from queue import PriorityQueue
from .RP import reconstruct_path

def euclidean(node1, node2):
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def line_of_sight(node1, node2, grid):
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()

    if x1 == x2:
        # Check if there are no obstacles in between
        min_y, max_y = min(y1, y2), max(y1, y2)
        for y in range(min_y + 1, max_y):
            if grid[x1][y].is_obstacle():
                return False
    elif y1 == y2:
        # Check if there are no obstacles in between
        min_x, max_x = min(x1, x2), max(x1, x2)
        for x in range(min_x + 1, max_x):
            if grid[x][y1].is_obstacle():
                return False
    else:
        return False

    return True


def remove_add(open_set_hash, open_set, distance, counter, neighbor):
    if neighbor in open_set_hash and neighbor in open_set.queue:
        open_set_hash.pop(neighbor)
        open_set.queue.remove(neighbor)
    open_set.put(
        (
            distance,
            counter,
            neighbor,
        )
    )
    open_set_hash[neighbor] = distance


def update_vertex(
    current, neighbor, parent, g_score, open_set, open_set_hash, end, counter, grid
):
    h = heuristic(neighbor.get_pos(), end.get_pos())
    if line_of_sight(parent[current], neighbor, grid):
        g_p_curr = g_score[parent[current]] + euclidean(parent[current], neighbor)
        if g_p_curr < g_score[neighbor]:
            g_score[neighbor] = g_p_curr
            parent[neighbor] = parent[current]
            remove_add(
                open_set_hash, open_set, g_score[neighbor] + h, counter, neighbor
            )
    else:
        g_curr = g_score[current] + euclidean(current, neighbor)
        if g_curr < g_score[neighbor]:
            g_score[neighbor] = g_curr
            parent[neighbor] = current
            remove_add(
                open_set_hash, open_set, g_score[neighbor] + h, counter, neighbor
            )


# Manhattan distance
def heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


def theta_star(draw, start, end, grid):
    g_score = {}
    g_score[start] = 0

    counter = 0
    open_set = PriorityQueue()
    open_set.put(
        (g_score[start] + heuristic(start.get_pos(), end.get_pos()), counter, start)
    )
    open_set_hash = {}
    open_set_hash[start] = start

    parent = {}
    parent[start] = start
    
    run = True

    while open_set and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                run = False
        
        current = open_set.get()

        if current[2].is_end():
            reconstruct_path(parent, end, draw)
            break

        if not current[2].is_start():
            current[2].uncheck()
        else:
            current[2].been_checked = True
        
        draw()
        
        if not current[2].is_start():
            current[2].check()

        for neighbor in current[2].neighbors:
            if not neighbor.been_checked:
                if not neighbor in open_set_hash:
                    g_score[neighbor] = float("inf")
                    parent[neighbor] = None

                update_vertex(
                    current[2],
                    neighbor,
                    parent,
                    g_score,
                    open_set,
                    open_set_hash,
                    end,
                    counter,
                    grid
                )
