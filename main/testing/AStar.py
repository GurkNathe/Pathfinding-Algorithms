from queue import PriorityQueue
from .RP import heuristic, count_path


def a_star(grid: list, start: object, end: object):
    """
    Perform an A* search from start to end.

    Args:
        grid (List[List[Node]]): The grid of nodes to search.
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.

    Returns:
        None
    """

    # Initialize counters and sets
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    # Initialize dictionaries to store the g and f scores for each node
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = heuristic("manhattan", start, end)

    # Initialize a set to store the nodes in the open set
    open_set_hash = {start}

    visited_nodes: int = 0
    path_size: int = 0

    # Perform the search
    while not open_set.empty():
        # Get the current node from the open set
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        visited_nodes += 1

        # End the search if the current node is the end node
        if current == end:
            path_size = count_path(came_from, end)
            break

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # Calculate the tentative g score for the neighbor
            temp_g_score = g_score[current] + 1

            # Update the g and f scores for the neighbor if the
            # tentative g score is lower
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic("manhattan", neighbor, end)

                # Add the neighbor to the open set if it is not already there
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
    return visited_nodes, path_size