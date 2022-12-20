import pygame
from .RP import get_unvisited_nodes, check


def reconstruct_path(draw, dist, V, start, end, nodes):
    if end not in nodes:
        return False

    u, v = nodes.index(start), nodes.index(end)

    path = []
    left = []
    right = []
    current = v

    for k in range(V - 1, -1, -1):
        if dist[u][v] == dist[u][k] + dist[k][v]:
            if (
                not nodes[k].is_start()
                and not nodes[k].is_end()
                and dist[u][k] not in left
                and dist[k][v] not in right
            ):
                path.append(nodes[k])
                left.append(dist[u][k])
                right.append(dist[k][v])
                draw()
            current = k

    curr = end
    while curr != start:
        for node in curr.neighbors:
            if node.is_start():
                return True

            if node in path:
                node.make_path()
                path.remove(node)
                curr = node


def floyd_warshall(draw, start, end, grid):
    nodes = get_unvisited_nodes(start)

    V = len(nodes)

    # Distances matrix
    distance = [[float("inf") for _ in range(V)] for _ in range(V)]

    # Initialize distance values
    for i in range(V):
        for j in range(V):
            if i == j:
                distance[i][j] = 0
            elif nodes[i] in nodes[j].neighbors:
                distance[i][j] = 1

    run = True

    for k in range(V):

        if not run:
            break
        run = check(pygame.event.get(), run)

        for i in range(V):
            for j in range(V):
                # if distance between two nodes is currently longer than the
                # path through the k node, set it to new shorter distance
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

                    if (
                        not nodes[i].is_start()
                        and not nodes[i].is_end()
                        and not nodes[j].is_start()
                        and not nodes[j].is_end()
                        and not nodes[k].is_start()
                        and not nodes[k].is_end()
                    ):
                        nodes[i].uncheck()
                        nodes[j].uncheck()
                        nodes[k].uncheck()

                    draw()

                    if (
                        not nodes[i].is_start()
                        and not nodes[i].is_end()
                        and not nodes[j].is_start()
                        and not nodes[j].is_end()
                        and not nodes[k].is_start()
                        and not nodes[k].is_end()
                    ):
                        nodes[i].check()
                        nodes[j].check()
                        nodes[k].check()

    reconstruct_path(draw, distance, V, start, end, nodes)
