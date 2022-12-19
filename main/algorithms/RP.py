from queue import Queue
import math

# Manhattan distance
def manhattan(node1, node2):
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()
    
    return abs(x1 - x2) + abs(y1 - y2)


# Euclidean distance
def euclidean(node1, node2):
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def heuristic(type, node1, node2):
    match type:
        case "euclidean":
            return euclidean(node1, node2)
        case "manhattan":
            return manhattan(node1, node2)
        case _:
            return manhattan(node1, node2)

# Reconstructs path using a dictionary mapping
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


# Traverse the grid and find all nodes connected to the start
def get_unvisited_nodes(start):
    Q = Queue()
    Q_hash = {start}
    Q.put(start)

    while not Q.empty():
        current = Q.get()

        for neighbor in current.neighbors:
            if neighbor not in Q_hash:
                Q.put(neighbor)
                Q_hash.add(neighbor)
    return Q_hash
