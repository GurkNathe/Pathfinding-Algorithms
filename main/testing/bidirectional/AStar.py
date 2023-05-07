from queue import PriorityQueue
from ..RP import heuristic, thread_construct


def bi_a_star(grid: object):
    """
    Performs a bidirectional search to find the shortest path between the
    start and end nodes. The search is visualized using the given draw object.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Initialize two queues, one for each direction of the search
    count_start = 0
    count_end = 0

    open_set_start = PriorityQueue()
    open_set_end = PriorityQueue()

    open_set_start.put((0, 0, grid.start))
    open_set_end.put((0, 0, grid.end))

    came_from_start = {}
    came_from_end = {}

    g_score_start = {node: float("inf") for row in grid.grid for node in row}
    g_score_start[grid.start] = 0

    g_score_end = {node: float("inf") for row in grid.grid for node in row}
    g_score_end[grid.end] = 0

    # Initialize two sets to keep track of visited nodes, one for
    # each direction of the search
    visited_start = set()
    visited_end = set()

    # Add the start and end nodes to the path dictionaries
    came_from_start[grid.start] = grid.start
    came_from_end[grid.end] = grid.end

    visited_nodes: int = 0
    path_size: int = 0

    # Loop until one of the queues is empty
    while not open_set_start.empty() and not open_set_end.empty():
        # Dequeue a node from each queue and process it
        start_score, start_count, start_node = open_set_start.get()
        
        # Check for redundant checks
        if start_node in visited_start:
            continue

        _, _, end_node = open_set_end.get()
        # Check for redundant checks
        if end_node in visited_end:
            open_set_start.put((start_score, start_count, start_node))
            continue

        # Check if the nodes have already been visited from the other direction
        if start_node in visited_end:
            # Construct two threads to reconstruct the path from the start and
            # end directions
            path_size = thread_construct(
                (came_from_start, start_node, grid.start),
                (came_from_end, start_node, grid.end),
            )
            break
        if end_node in visited_start:
            # Construct two threads to reconstruct the path from the start and
            # end directions
            path_size = thread_construct(
                (came_from_start, end_node, grid.start),
                (came_from_end, end_node, grid.end),
            )
            break

        visited_nodes += 2

        # Add the neighbors of the dequeued nodes to their respective queues
        for neighbor in start_node.neighbors:
            temp_g_score = g_score_start[start_node] + 1

            if temp_g_score < g_score_start[neighbor]:
                came_from_start[neighbor] = start_node
                g_score_start[neighbor] = temp_g_score
                if neighbor not in visited_start:
                    f_score = temp_g_score + heuristic("manhattan", neighbor, grid.end)
                    count_start += 1
                    open_set_start.put((f_score, count_start, neighbor))
                    visited_start.add(start_node)

        for neighbor in end_node.neighbors:
            temp_g_score = g_score_end[end_node] + 1

            if temp_g_score < g_score_end[neighbor]:
                came_from_end[neighbor] = end_node
                g_score_end[neighbor] = temp_g_score
                if neighbor not in visited_end:
                    f_score = temp_g_score + heuristic("manhattan", neighbor, grid.start)
                    count_end += 1
                    open_set_end.put((f_score, count_end, neighbor))
                    visited_end.add(end_node)

    return visited_nodes, path_size
