import pygame
from queue import PriorityQueue
from ..RP import heuristic, check, markup, thread_construct


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

    run = True

    # Loop until one of the queues is empty
    while not open_set_start.empty() and not open_set_end.empty() and run:
        # Check for events and update the run flag accordingly
        run = check(pygame.event.get(), run)

        # Dequeue a node from each queue and process it
        f_score1, count1, node1 = open_set_start.get()
        
        # Check for redundant checks
        if node1 in visited_start:
            continue

        _, _, node2 = open_set_end.get()
        # Check for redundant checks
        if node2 in visited_end:
            open_set_start.put((f_score1, count1, node1))
            continue

        # Check if the nodes have already been visited from the other direction
        if node1 in visited_end:
            # Construct two threads to reconstruct the path from the start and
            # end directions
            thread_construct(
                (came_from_start, node1, grid.start, grid.draw),
                (came_from_end, node1, grid.end, grid.draw),
            )
            break
        if node2 in visited_start:
            # Construct two threads to reconstruct the path from the start and
            # end directions
            thread_construct(
                (came_from_start, node2, grid.start, grid.draw),
                (came_from_end, node2, grid.end, grid.draw),
            )
            break

        # Mark up the nodes that are being processed
        markup(grid.draw, node1)
        markup(grid.draw, node2)

        # Add the neighbors of the dequeued nodes to their respective queues
        for neighbor in node1.neighbors:
            temp_g_score = g_score_start[node1] + 1

            if temp_g_score < g_score_start[neighbor]:
                came_from_start[neighbor] = node1
                g_score_start[neighbor] = temp_g_score
                if neighbor not in visited_start:
                    f_score = temp_g_score + heuristic("manhattan", neighbor, grid.end)
                    count_start += 1
                    open_set_start.put((f_score, count_start, neighbor))
                    visited_start.add(node1)

                    if not neighbor.is_start() and not neighbor.is_end():
                        neighbor.uncheck()

        for neighbor in node2.neighbors:
            temp_g_score = g_score_end[node2] + 1

            if temp_g_score < g_score_end[neighbor]:
                came_from_end[neighbor] = node2
                g_score_end[neighbor] = temp_g_score
                if neighbor not in visited_end:
                    f_score = temp_g_score + heuristic("manhattan", neighbor, grid.start)
                    count_end += 1
                    open_set_end.put((f_score, count_end, neighbor))
                    visited_end.add(node2)

                    if not neighbor.is_start() and not neighbor.is_end():
                        neighbor.uncheck()
