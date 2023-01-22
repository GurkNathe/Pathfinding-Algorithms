import time
from queue import PriorityQueue
from .RP import heuristic, check


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


def remove_add(open_set_hash: dict, open_set: object, distance: int or float, counter: int, neighbor: object):
    """
    Remove a node from the open set (if it exists) and add it back to the open set
    with an updated distance value.

    Parameters:
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

    Parameters:
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


def theta_star(start: object, end: object, grid: list):
    """
    Perform the Theta* search algorithm on the grid.

    Parameters:
        start (Node): The start node of the search.
        end (Node): The end node of the search.
        grid (List[List[Node]]): The grid of nodes to search.

    Returns:
        None
    """

    # Dictionary mapping nodes to their g scores (distance from the start vertex)
    g_score = {}
    g_score[start] = 0

    counter = 0

    # Priority queue for the open set of nodes to search
    open_set = PriorityQueue()
    open_set.put((g_score[start] + heuristic("manhattan", start, end), counter, start))
    open_set_hash = {}
    open_set_hash[start] = start

    parent = {}
    parent[start] = start

    visited_nodes: int = 0

    # While the open set is not empty and the run flag is True
    while open_set:
        # Get minimum distance node in the open set
        current = open_set.get()[2]

        visited_nodes += 1

        # If the current vertex is the end vertex
        if current.is_end():
            break

        if current.is_start():
            current.been_checked = True
        else:
            check(current)
        
        for neighbor in current.neighbors:
            if not neighbor.been_checked:
                if not neighbor in open_set_hash:
                    g_score[neighbor] = float("inf")
                    parent[neighbor] = None

                # Update the distance values and parent pointers for the neighbor
                update_vertex(
                    current,
                    neighbor,
                    parent,
                    g_score,
                    open_set,
                    open_set_hash,
                    end,
                    counter,
                    grid,
                )
    return visited_nodes