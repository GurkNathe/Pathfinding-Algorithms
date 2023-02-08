from .RP import check, count_path


def dfs(grid: object):
    """
    Perform a depth-first search from start to end.

    Args:
        grid (Grid): An object representing the current grid.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        count_path (int): Length of the path found.
    """

    # Initialize a stack to store the nodes to visit
    stack = [grid.start]

    # Initialize a dictionary to store the predecessor of each node
    previous = {}

    # Initialize flags to track the search status
    found = False

    visited_nodes: int = 0

    # Perform the search
    while len(stack) and not found:
        # Get the next node to visit
        current = stack.pop()

        # Skip the node if it has already been checked
        if current.is_checked():
            continue

        visited_nodes += 1

        check(current)

        # Check the neighbors of the current node
        for neighbor in current.neighbors:
            # Skip the neighbor if it has already been checked
            if not neighbor.is_checked():
                # End the search if the neighbor is the end node
                if neighbor.is_end():
                    previous[neighbor] = current
                    found = True
                    break
                # Add the neighbor to the stack of nodes to visit if it is not the end node
                else:
                    previous[neighbor] = current
                    stack.append(neighbor)

    return visited_nodes, count_path(previous, grid.end)
