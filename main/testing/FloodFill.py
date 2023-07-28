import pygame
import heapq

def flood_fill(grid: object):
    """
    Performs the Flood Fill algorithm to solve the 
    shortest path problem.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """
    # Create a dictionary to store distance values
    distances = { node: float("inf") for row in grid for node in row }
    distances[grid.end] = 0

    # Start from end
    queue = [(0, grid.end)]

    visited_nodes: int = 0
    path_size: int = 0

    while queue:
        dist, current = heapq.heappop(queue)

        if current.is_checked():
            continue


        if current.is_start():
            break

        if not current.is_end():
            current.check()

        visited_nodes += 1

        # Check every neighbor of the current cell and 
        # add it to the queue if it hasn't been checked before
        for neighbor in current.neighbors:
            if not neighbor.is_checked():
                distances[neighbor] = dist + 1
                heapq.heappush(queue, (dist + 1, neighbor))
    
    # Count path
    if distances[grid.start] != float("inf"):
        current = grid.start
        found = False
        while not found:
            best = (float("inf"), None)
            for neighbor in current.neighbors:
                if neighbor.is_end():
                    found = True
                    break
                if distances[neighbor] < best[0]: 
                    best = (distances[neighbor], neighbor)
            if not found:
                path_size += 1
                current = best[1]

    return visited_nodes, path_size
