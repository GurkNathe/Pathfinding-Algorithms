from queue import PriorityQueue
from .RP import check, count_path


def dijkstra(grid: object):
    """
    Perform Dijkstra's algorithm from start to end.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """

    # Initialize a priority queue to store the nodes to visit
    queue = PriorityQueue()

    # Set up the node values
    distance = {node: float("inf") for row in grid.grid for node in row}
    distance[grid.start] = 0

    # Holds the path from start to end
    previous = {}

    # Add the start node to the priority queue
    queue.put((distance[grid.start], 0, grid.start))
    count = 0

    visited_nodes: int = 0
    path_size: int = 0

    # Perform the search
    while not queue.empty():
        # Get the next node to visit
        current_distance, _, current_min = queue.get()

        visited_nodes += 1

        # End the search if the current node is the end node
        if current_min.is_end():
            path_size = count_path(previous, grid.end)
            break

        check(current_min)

        # Check the neighbors of the current node
        for neighbor in current_min.neighbors:
            # Don't recheck for performance
            if not neighbor.is_checked():
                # edges between vertecies are not weighted
                # (using constant weight of 1)
                temp_value = distance[current_min] + 1
                if temp_value < distance[neighbor]:
                    distance[neighbor] = temp_value
                    previous[neighbor] = current_min
                    count += 1

                    # Add the neighbor to the priority queue
                    queue.put((distance[neighbor], count, neighbor))

    return visited_nodes, path_size
