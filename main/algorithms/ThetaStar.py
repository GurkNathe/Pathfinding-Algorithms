import pygame
import time
from queue import PriorityQueue
from .RP import reconstruct_path, heuristic, check


def line_of_sight(node1: object, node2: object, grid: list):
    """
    Check if there is a straight line of sight between two nodes on the grid.
    This is determined by checking if there are any obstacles in a straight line
    between the two nodes.

    Args:
        node1 (Node): The first node to check.
        node2 (Node): The second node to check.
        grid (List[List[Node]]): The grid of nodes to search.

    Returns:
        bool: True if there is a straight line of sight between the two nodes,
        False otherwise.
    """

    # Get the x and y coordinates of the first and second nodes
    x1, y1 = node1.get_pos()
    x2, y2 = node2.get_pos()

    # If the x coordinates of the two nodes are the same
    if x1 == x2:
        # Check if there are no obstacles in between the nodes on the y axis
        min_y, max_y = min(y1, y2), max(y1, y2)
        for y in range(min_y + 1, max_y):
            # Return False as there is not a straight line of sight between the nodes
            if grid[x1][y].is_obstacle():
                return False
    # If the y coordinates of the two nodes are the same
    elif y1 == y2:
        # Check if there are no obstacles in between the nodes on the x axis
        min_x, max_x = min(x1, x2), max(x1, x2)
        for x in range(min_x + 1, max_x):
            # Return False as there is not a straight line of sight between the nodes
            if grid[x][y1].is_obstacle():
                return False
    # If the nodes are not aligned on the same x or y axis,
    # Return False as there cannot be a straight line of sight between them
    else:
        return False

    return True


def remove_add(
    open_set_hash: dict,
    open_set: object,
    distance: int or float,
    counter: int,
    neighbor: object,
):
    """
    Remove a node from the open set (if it exists) and add it back to the open set
    with an updated distance value.

    Args:
        open_set_hash (Dict[Node, Node]): A dictionary mapping nodes to distance
            values in the open set.
        open_set (PriorityQueue): The open set of nodes to search, prioritized
            by distance and then FIFO order.
        distance (int or float): The updated distance value for the node.
        counter (int): A counter value for the node.
        neighbor (Node): The node to remove from and add back to the open set.

    Returns:
        None
    """

    # If the neighbor node is in the open set
    if neighbor in open_set_hash and neighbor in open_set.queue:
        # Remove the neighbor from the open set
        open_set_hash.pop(neighbor)
        open_set.queue.remove(neighbor)

    # Add the neighbor node back to the open set with the updated distance value
    open_set.put(
        (
            distance,
            counter,
            neighbor,
        )
    )
    open_set_hash[neighbor] = distance


def update_vertex(
    current: object,
    neighbor: object,
    parent: dict,
    g_score: dict,
    open_set: object,
    open_set_hash: dict,
    end: object,
    counter: int,
    grid: list,
):
    """
    Update the distance values and parent pointers for a node in the search.

    Args:
        current (Node): The current node being processed.
        neighbor (Node): The neighbor node being processed.
        parent (Dict[Node, Node]): A dictionary mapping nodes to their parent nodes.
        g_score (Dict[Node, int]): A dictionary mapping nodes to their g scores
            (distance from the start node).
        open_set (PriorityQueue): The open set of nodes to search, prioritized
            by distance then FIFO order.
        open_set_hash (Dict[Node, Node]): A dictionary mapping nodes to distance values in
            the open set.
        end (Node): The end node of the search.
        counter (int): A counter value for the node.
        grid (List[List[Node]]): The grid of nodes to search.

    Returns:
        None
    """

    # Calculate the Manhattan distance heuristic for the neighbor node
    h = heuristic("manhattan", neighbor, end)

    # If there is a line of sight between the current node's parent and the neighbor
    if line_of_sight(parent[current], neighbor, grid):

        # Calculate the Euclidean distance between the parent and the neighbor
        g_p_curr = g_score[parent[current]] + heuristic(
            "euclidean", parent[current], neighbor
        )

        # If the distance through the parent is shorter
        if g_p_curr < g_score[neighbor]:
            g_score[neighbor] = g_p_curr
            parent[neighbor] = parent[current]

            # Update the open set with the new distance for the neighbor
            remove_add(
                open_set_hash, open_set, g_score[neighbor] + h, counter, neighbor
            )
    # If there is no line of sight between the current node's parent and
    # the neighbor
    else:
        # Calculate the Euclidean distance between the current node and the neighbor
        g_curr = g_score[current] + heuristic("euclidean", current, neighbor)

        # If the distance through the current node is shorter
        if g_curr < g_score[neighbor]:
            g_score[neighbor] = g_curr
            parent[neighbor] = current

            # Update the open set with the new distance for the neighbor
            remove_add(
                open_set_hash, open_set, g_score[neighbor] + h, counter, neighbor
            )


def connect_path(came_from: dict, current: object, draw: object, grid: list):
    """
    Connect the path between turn points on the grid.

    Args:
        came_from (Dict[Node, Node]): A dictionary mapping nodes to their parent nodes.
        current (Node): The current node being processed.
        draw (function): A function to draw the grid.
        grid (List[List[Node]]): The grid of nodes to search.

    Returns:
        None
    """

    # Temp variable to for connected path
    end = current

    # Displaying what Theta* generates (the turn points)
    reconstruct_path(came_from, current, draw)

    # Timeout for turn point visualization
    time.sleep(1.5)

    # Fill in path between turn points
    current = end
    while current in came_from and not current.is_start():
        previous = came_from[current]

        xp, yp = previous.get_pos()
        xc, yc = current.get_pos()

        x_dir = xp - xc
        y_dir = yp - yc

        # If the previous node is aligned with the current node on the x axis
        if x_dir == 0:
            # Current is above previous
            if y_dir > 0:
                # Iterate through all y values between the current and
                # previous nodes
                for y in range(yc, yp):
                    if not grid[xp][y].is_start() and not grid[xp][y].is_end():
                        grid[xp][y].make_path()

            # Current is bellow previous
            else:
                # Iterate through all y values between the current and
                # previous nodes
                for y in range(yp, yc):
                    if not grid[xp][y].is_start() and not grid[xp][y].is_end():
                        grid[xp][y].make_path()

        # If the previous node is aligned with the current node on the y axis
        elif y_dir == 0:
            # Current is left of previous
            if x_dir > 0:
                # Iterate through all x values between the current and
                # previous nodes
                for x in range(xc, xp):
                    if not grid[x][yp].is_start() and not grid[x][yp].is_end():
                        grid[x][yp].make_path()

            # Current is right of previous
            else:
                # Iterate through all x values between the current and
                # previous nodes
                for x in range(xp, xc):
                    if not grid[x][yp].is_start() and not grid[x][yp].is_end():
                        grid[x][yp].make_path()

        current = previous
        draw()


def theta_star(grid: object):
    """
    Perform the Theta* search algorithm on the grid.

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None
    """

    # Dictionary mapping nodes to their g scores (distance from the start vertex)
    g_score = {}
    g_score[grid.start] = 0

    counter = 0

    # Priority queue for the open set of nodes to search
    open_set = PriorityQueue()
    open_set.put(
        (
            g_score[grid.start] + heuristic("manhattan", grid.start, grid.end),
            counter,
            grid.start,
        )
    )
    open_set_hash = {}
    open_set_hash[grid.start] = grid.start

    parent = {}
    parent[grid.start] = grid.start

    run = True

    # While the open set is not empty and the run flag is True
    while open_set and run:
        # Check for any events that may have occurred
        run = check(pygame.event.get(), run)

        # Get minimum distance node in the open set
        current = open_set.get()[2]

        # If the current vertex is the end vertex
        if current.is_end():
            connect_path(parent, grid.end, grid.draw, grid.grid)
            break

        # Markup for drawing grid
        if not current.is_start():
            current.uncheck()
        else:
            current.been_checked = True

        grid.draw()

        if not current.is_start():
            current.check()

        for neighbor in current.neighbors:
            if not neighbor.been_checked:
                if not neighbor in open_set_hash:
                    g_score[neighbor] = float("inf")
                    parent[neighbor] = None

                # Markup for drawing neighbor
                if not neighbor.is_start() and not neighbor.is_end():
                    neighbor.uncheck()

                counter += 1
                # Update the distance values and parent pointers for the neighbor
                update_vertex(
                    current,
                    neighbor,
                    parent,
                    g_score,
                    open_set,
                    open_set_hash,
                    grid.end,
                    counter,
                    grid.grid,
                )
