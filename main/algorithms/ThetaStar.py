import pygame
import time
from queue import PriorityQueue
from .RP import reconstruct_path, heuristic


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
    h = heuristic("manhattan", neighbor, end)
    if line_of_sight(parent[current], neighbor, grid):
        g_p_curr = g_score[parent[current]] + heuristic(
            "euclidean", parent[current], neighbor
        )
        if g_p_curr < g_score[neighbor]:
            g_score[neighbor] = g_p_curr
            parent[neighbor] = parent[current]
            remove_add(
                open_set_hash, open_set, g_score[neighbor] + h, counter, neighbor
            )
    else:
        g_curr = g_score[current] + heuristic("euclidean", current, neighbor)
        if g_curr < g_score[neighbor]:
            g_score[neighbor] = g_curr
            parent[neighbor] = current
            remove_add(
                open_set_hash, open_set, g_score[neighbor] + h, counter, neighbor
            )


def connect_path(came_from, current, draw, grid):
    # Temp variable to for connected path
    end = current

    # Displaying what Theta* generates (the turn points)
    reconstruct_path(came_from, current, draw)

    # Timeout for turn point visualization
    time.sleep(1.5)

    # Fill in path between turn points
    current = end
    while current in came_from and not current.is_start():
        previous = came_from[current]
        xp, yp = previous.get_pos()
        xc, yc = current.get_pos()

        x_dir = xp - xc
        y_dir = yp - yc

        if x_dir == 0:
            # Current is above previous
            if y_dir > 0:
                for y in range(yc, yp):
                    if not grid[xp][y].is_start():
                        grid[xp][y].make_path()
            # Current is bellow previous
            else:
                for y in range(yp, yc):
                    if not grid[xp][y].is_start():
                        grid[xp][y].make_path()
        elif y_dir == 0:
            # Current is left of previous
            if x_dir > 0:
                for x in range(xc, xp):
                    if not grid[x][yp].is_start():
                        grid[x][yp].make_path()
            # Current is right of previous
            else:
                for x in range(xp, xc):
                    if not grid[x][yp].is_start():
                        grid[x][yp].make_path()

        current = previous
        draw()


def theta_star(draw, start, end, grid):
    g_score = {}
    g_score[start] = 0

    counter = 0
    open_set = PriorityQueue()
    open_set.put((g_score[start] + heuristic("manhattan", start, end), counter, start))
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
            connect_path(parent, end, draw, grid)
            end.make_end()
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
                    grid,
                )
