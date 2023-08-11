from queue import Queue
from .RP import count_path

def spfa(grid: object):
    d = {node: float("inf") for row in grid.grid for node in row}
    d[grid.start] = 0

    queue = Queue()
    queue.put(grid.start)

    path = {}

    visited_nodes: int = 0

    while not queue.empty():
        u = queue.get()

        visited_nodes += 1

        for v in u.neighbors:
            if d[u] + 1 < d[v]:
                # Update the distance and predecessor for the neighbor if the
                # current distance is shorter
                d[v] = d[u] + 1
                path[v] = u

                if v not in queue.queue:
                    queue.put(v)

    return visited_nodes, count_path(path, grid.end)