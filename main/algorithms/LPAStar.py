import pygame
import heapq
from .RP import reconstruct_path, heuristic, check


def find_path(grid, g):
    path = []
    current = grid.start
    while current != grid.end:
        path.append(current)
        min_cost = float("inf")
        min_node = None
        for neighbor in current.neighbors:
            cost = g[neighbor] + heuristic("manhattan", current, neighbor)
            if cost < min_cost:
                min_cost = cost
                min_node = neighbor
        current = min_node
    path.append(grid.end)
    return path


def update_vertex(grid, node, rhs, g, open_list, parent):
    if node != grid.start:
        rhs[node] = float("inf")
        for neighbor in node.neighbors:
            if neighbor.is_checked() or neighbor.is_start():
                rhs[node] = min(rhs[node], g[neighbor] + heuristic("manhattan", neighbor, node));

        open_list = [(key, value) for key, value in open_list if value != node]
        heapq.heapify(open_list)

        if g[node] != rhs[node]:
            heapq.heappush(open_list, (calc_key(grid.end, node, g, rhs), node))
    return open_list

def calc_key(end, node, g, rhs):
    return (min(g[node], rhs[node]) + heuristic("manhattan", node, end), 
            min(g[node], rhs[node]))

def lpa_star(grid: object):
    rhs = {node: float("inf") for row in grid.grid for node in row}
    g = {node: float("inf") for row in grid.grid for node in row}
    parent = {node: None for row in grid.grid for node in row}
    open_list = []

    rhs[grid.start] = 0
    topKey = calc_key(grid.end, grid.start, g, rhs)
    open_list.append((topKey, grid.start))

    # Initialize a flag to track whether the search should continue
    run = True

    while (topKey < calc_key(grid.end, grid.end, g, rhs) or rhs[grid.end] != g[grid.end]) and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        topKey, node = heapq.heappop(open_list)
        print(open_list)
        if g[node] > rhs[node]:
            g[node] = rhs[node]
        else:
            g[node] = float("inf")
            open_list = update_vertex(grid, node, rhs, g, open_list, parent)

        for neighbor in node.neighbors:
            if not neighbor.is_start() and not neighbor.is_end():
                neighbor.uncheck()
            open_list = update_vertex(grid, neighbor, rhs, g, open_list, parent)

        print(open_list)
        # Update the screen with the search progress
        grid.draw()

        # Check the current node if it is not the start node
        if not node.is_start():
            node.check()

    # path = find_path(grid, g)