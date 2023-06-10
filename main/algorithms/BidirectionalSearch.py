import pygame
import threading
import time
from .RP import check, markup


def reconstruct_path(came_from: object, current: object, target: object, draw: object):
    """
    Reconstructs the path from the current node to the target node in a maze.

    Args:
        came_from (Dict[Node, Node]): A dictionary containing the nodes traversed
            during the pathfinding algorithm.
        current (Node): The node being checked when the algorithm terminated
        target (Node): The node to traverse back to
        draw (function): A function for drawing the maze.

    Returns:
        None
    """

    # Draw the intersected node
    win = pygame.display.get_surface()
    current.make_path()
    current.draw(win)
    pygame.display.update()

    while current in came_from:
        if came_from[current] != target:
            current = came_from[current]
            current.make_path()
            current.draw(win)
            pygame.display.update()
            time.sleep(0.015)
        else:
            break


# This method is included for a more aesthetic reconstruction
def thread_construct(args1: tuple, args2: tuple):
    """
    Constructs two threads that will run the `reconstruct_path` function with the
    given arguments. The threads are started and then joined, which waits for
    them to finish before returning.

    Args:
        args1 (tuple): A tuple of arguments to pass to the first
            `reconstruct_path` function.
        args2 (tuple): A tuple of arguments to pass to the second
            `reconstruct_path` function.
    """
    # Create two threads that will run the `reconstruct_path` function with the
    # given arguments
    n1 = threading.Thread(target=reconstruct_path, args=args1)
    n2 = threading.Thread(target=reconstruct_path, args=args2)

    # Start the threads
    n1.start()
    n2.start()

    # Wait for the threads to finish
    n1.join()
    n2.join()


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

        # Add the neighbors of the dequeued nodes to their respective queues
        for neighbor in node1.neighbors:
            if neighbor not in visited_start:
                queue_start.append(neighbor)
                start_path[neighbor] = node1
                neighbor.uncheck()
        for neighbor in node2.neighbors:
            if neighbor not in visited_end:
                queue_end.append(neighbor)
                end_path[neighbor] = node2
                neighbor.uncheck()
