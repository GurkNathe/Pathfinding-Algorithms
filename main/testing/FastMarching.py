import pygame
import heapq
from .RP import count_path

def fmm(grid: object):
    """
    Performs the Fast Marching Method on a uniform cost grid
    to solve the shortest path problem.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None: The function updates the screen with the search progress and path.
    """
    # Initialize dictionarie to store the cost for each node
    costs = {node: float("inf") for row in grid.grid for node in row}
    costs[grid.start] = 0

    # Record all the unvisited nodes in the grid
    far = [node for row in grid.grid for node in row if not node.is_start()]

    # Initialize the visited priority queue
    considered = []
    heapq.heappush(considered, (0, grid.start))

    came_from = {}

    visited_nodes: int = 0
    path_size: int = 0

    # Perform the search
    while considered:
        # Get the current node from the open set
        ccost, current = heapq.heappop(considered)

        visited_nodes += 1

        # End the search if the current node is the end node
        if current.is_end():
            path_size = count_path(came_from, grid.end)
            break

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # If the neighbor hasn't been checked
            if neighbor not in considered and not neighbor.is_checked():
                # Edges between nodes are not weighted
                # (using constant weight of 1)
                cost = ccost + 1
                if cost < costs[neighbor]:
                    costs[neighbor] = cost
                    came_from[neighbor] = current

                    # If neighbor hasn't been checked or been visited before
                    # add it to the queue
                    if neighbor in far:
                        heapq.heappush(considered, (cost, neighbor))
                        far.remove(neighbor)
    return visited_nodes, path_size