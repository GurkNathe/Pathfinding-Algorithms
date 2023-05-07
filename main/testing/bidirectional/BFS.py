from ..RP import thread_construct


def bi_search(grid: object):
    """
    Performs a bidirectional search to find the shortest path between the
    start and end nodes.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
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

    visited_nodes: int = 0
    path_size: int = 0

    # Loop until one of the queues is empty
    while queue_start and queue_end:
        # Dequeue a node from each queue and process it
        start_node = queue_start.pop(0)
        # Check for redundant checks
        if start_node in visited_start:
            continue

        end_node = queue_end.pop(0)
        # Check for redundant checks
        if end_node in visited_end:
            queue_start.insert(0, start_node)
            continue

        # Check if the nodes have already been visited from the other direction
        if start_node in visited_end:
            # Construct two threads to reconstruct the path from the start and
            # end directions
            path_size = thread_construct(
                (start_path, start_node, grid.start), (end_path, start_node, grid.end)
            )
            break

        if end_node in visited_start:
            # Construct two threads to reconstruct the path from the start and
            # end directions
            path_size = thread_construct(
                (start_path, end_node, grid.start), (end_path, end_node, grid.end)
            )
            break

        visited_nodes += 2

        # Mark the nodes as visited
        visited_start.add(start_node)
        visited_end.add(end_node)

        # Add the neighbors of the dequeued nodes to their respective queues
        loop_helper(start_node, visited_start, queue_start, start_path)
        loop_helper(end_node, visited_end, queue_end, end_path)

    return visited_nodes, path_size


def loop_helper(node: object, visited: set, queue: list, path: dict):
    """
    Does the neighbor search.

    Args:
        node (Node): The node being checked.
        visited (set): The set of visited nodes from the side the node is being 
            checked from.
        queue (list): The list of node to visit.
        path (dict): The path taken from the side the node is being checked.

    Returns:
        None
    """
    for neighbor in node.neighbors:
        if neighbor not in visited:
            queue.append(neighbor)
            path[neighbor] = node