import pygame
import heapq
from .RP import check, reconstruct_path, markup

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

    run = True

    # Perform the search
    while considered and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Get the current node from the open set
        ccost, current = heapq.heappop(considered)

        # End the search if the current node is the end node
        if current.is_end():
            reconstruct_path(came_from, grid.end, grid.draw)
            break

        # Draw the current node
        markup(grid.draw, current)

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

                        # Uncheck the neighbor if it is not the start or end node
                        # for markup
                        if not neighbor.is_start() and not neighbor.is_end():
                            neighbor.uncheck()