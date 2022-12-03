import pygame
from queue import PriorityQueue

"""
Algorithm

for each vertex in graph:
    distance[vertex] = inf
    previous[vertex] = null
    if vertex != start, and veertex to Priority Queue
distance[start] = 0

while the queue is not empty:
    U = min from queue
    for each unvisited neighbor vertex of U
        tempDistance = distance[U] + edge_weight(U, vertex)
        if tempDistance < distance[vertex]:
            distance[vertex] = tempDistance
            previous[vertex] = U

return distance[], previous[]
"""


def merge_dicts(d1, d2):
    return {} if any(d1[k] != d2[k] for k in d1.keys() & d2) else {**d1, **d2}


# TODO: Look at implementing better dynamic programming
def get_unvisited_nodes(current):
    unvisited = {}
    if current is not None:
        unvisited[current] = current
        for neighbor in current.neighbors:
            if not neighbor.been_checked:
                unvisited[neighbor] = neighbor
                neighbor.been_checked = True
                unvisited = merge_dicts(unvisited, get_unvisited_nodes(neighbor))
    return unvisited


def reconstruct_path(came_from, current, draw):
    """
    came_from : dictionary of nodes traversed in the algorithm
    current : end node
    draw : pygame draw function
    """
    while current in came_from:
        if not came_from[current].is_start():
            current = came_from[current]
            current.make_path()
            draw()
        else:
            break


def dijkstra(draw, grid, start, end):
    unvisited_nodes = get_unvisited_nodes(start)
    distance = {node: float("inf") for row in grid for node in row}
    distance[start] = 0

    previous = {}

    while unvisited_nodes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Choose node with smallest distance
        current_min = None
        for node in unvisited_nodes:
            if current_min == None:
                current_min = node
            elif distance[node] < distance[current_min]:
                current_min = node

        for neighbor in current_min.neighbors:
            if not neighbor.is_start() and not neighbor.is_end():
                neighbor.check()
            # edges between vertecies are not weighted 
            # (using constant weight of 1)
            temp_value = distance[current_min] + 1
            if temp_value < distance[neighbor]:
                distance[neighbor] = temp_value
                previous[neighbor] = current_min

            draw()

        del unvisited_nodes[current_min]

    reconstruct_path(previous, end, draw)
