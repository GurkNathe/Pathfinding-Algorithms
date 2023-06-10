import pygame
from ..RP import check, markup, thread_construct

def bi_search(grid: object):
    """
    Performs a bidirectional search to find the shortest path between the
    start and end nodes. The search is visualized using the given draw object.

    Args:
        grid (Grid): An object representing the current grid
    """

    # Initialize two queues, one for each direction of the search
    queue_start = [grid.start]
    queue_end = [grid.end]

    # Initialize two sets to keep track of visited nodes, one for
    # each direction of the search
    visited_start = set()
    visited_end = set()

    # Initialize dictionaries to store the paths taken by each search direction
    start_path = {}
    end_path = {}

    # Add the start and end nodes to the path dictionaries
    start_path[grid.start] = grid.start
    end_path[grid.end] = grid.end

    run = True

    # Loop until one of the queues is empty
    while queue_start and queue_end and run:
        # Check for events and update the run flag accordingly
        run = check(pygame.event.get(), run)

        # Dequeue a node from each queue and process it
        node1 = queue_start.pop(0)
        # Check for redundant checks
        if node1 in visited_start:
            continue

        node2 = queue_end.pop(0)
        # Check for redundant checks
        if node2 in visited_end:
            queue_start.insert(0, node1)
            continue

        # Check if the nodes have already been visited from the other direction
        if node1 in visited_end:
            # Construct two threads to reconstruct the path from the start and
            # end directions
            thread_construct(
                (start_path, node1, grid.start, grid.draw),
                (end_path, node1, grid.end, grid.draw),
            )
            break
        if node2 in visited_start:
            # Construct two threads to reconstruct the path from the start and
            # end directions
            thread_construct(
                (start_path, node2, grid.start, grid.draw),
                (end_path, node2, grid.end, grid.draw),
            )
            break

        # Mark up the nodes that are being processed
        markup(grid.draw, node1)
        markup(grid.draw, node2)

        # Mark the nodes as visited
        visited_start.add(node1)
        visited_end.add(node2)

        loop_helper(node1, visited_start, queue_start, start_path)
        loop_helper(node2, visited_end, queue_end, end_path)


def loop_helper(node, visited, queue, path):
    for neighbor in node.neighbors:
        if neighbor not in visited:
            queue.append(neighbor)
            path[neighbor] = node
            neighbor.uncheck()