import pygame
from queue import PriorityQueue, Queue
from .RP import reconstruct_path, get_unvisited_nodes, check, markup


# TODO: Refactor using a priority queue
# Make distance a priority queue (node, inf)
def dijkstra(draw, start, end):
    # Stores all nodes connected to start
    unvisited_nodes = get_unvisited_nodes(start)

    # Set up the node values
    distance = {node: float("inf") for node in unvisited_nodes}
    distance[start] = 0

    # Holds the path from start to end
    previous = {}

    run = True

    while unvisited_nodes and run:
        run = check(pygame.event.get(), run)

        # Choose node with smallest distance
        current_min = min(unvisited_nodes, key=distance.get)

        # Ends the search once the end is reached
        # May add a toggle for this
        if current_min == end:
            break

        for neighbor in current_min.neighbors:
            # Don't recheck for performance
            if not neighbor.is_checked():
                # edges between vertecies are not weighted
                # (using constant weight of 1)
                temp_value = distance[current_min] + 1
                if temp_value < distance[neighbor]:
                    distance[neighbor] = temp_value
                    previous[neighbor] = current_min

                markup(draw, neighbor)

        unvisited_nodes.remove(current_min)

    reconstruct_path(previous, end, draw)
