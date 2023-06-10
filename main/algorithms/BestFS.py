import pygame
from queue import PriorityQueue
from .RP import heuristic, check, markup


def get_checked_neighbors(node: object):
    """
    Get the neighbors of a node that have been checked or are the start node.

    Args:
        node (Node): The node to check.

    Returns:
        List[Node]: The list of checked or start neighbors.
    """

    checked = []
    for neighbor in node.neighbors:
        if neighbor.is_checked() or neighbor.is_start():
            checked.append(neighbor)
    return checked


def reconstruct_path(current: object, costs: dict, draw: object):
    """
    Reconstruct the path from the end node to the start node.

    Args:
        current (Node): The current node in the search.
        costs (Dict[Node, int]): The cost of reaching each node from the start.
        draw (function): A function used to draw the search on the screen.

    Returns:
        None: The function updates the screen with the path.
    """

    # Continue until the current node is the start node
    while not current.is_start():
        # Find the neighbor with the lowest cost
        current = min(get_checked_neighbors(current), key=lambda x: costs[x])

        # Break if the current node is the start node
        if current.is_start():
            break

        # Draw the path to the current node
        current.make_path()
        draw()


def best_fs(grid: object):
    """
    Perform a best-first search from start to end.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Initialize the priority queue with the start node
    queue = PriorityQueue()
    queue.put((0, 0, grid.start))
    count = 0

    # Initialize a dictionary to store the cost of reaching each node from the start
    costs = {grid.start: 0}

    # Initialize a flag to track whether the search should continue
    run = True

    # Perform the search
    while not queue.empty() and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Get the node with the lowest cost from the queue
        cost, _, current = queue.get()

        # End the search if the current node is the end node
        if current.is_end():
            reconstruct_path(current, costs, grid.draw)
            grid.end.make_end()
            break

        # Draw the current node
        markup(grid.draw, current)

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # Calculate the cost of reaching the neighbor
            cost = costs[current] + 1

            # Update the cost in the dictionary if it is lower than the current value
            if neighbor not in costs or cost < costs[neighbor]:
                costs[neighbor] = cost
                # Add the neighbor to the queue with the calculated cost as the priority
                count += 1
                queue.put(
                    (
                        cost + heuristic("manhattan", neighbor, grid.end),
                        count,
                        neighbor,
                    )
                )

                # Uncheck the child if it is not the start or end node
                # for markup
                if not neighbor.is_start() and not neighbor.is_end():
                    neighbor.uncheck()
