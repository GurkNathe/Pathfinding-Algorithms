import heapq
from .RP import heuristic, check, count_path


def beam_search(grid: object, beam_size: int):
    """
    Perform a beam search from start to end with a given beam size.

    Args:
        grid (Grid): An object representing the current grid.
        beam_size (int): The maximum number of nodes to consider at each step.

    Returns:
        visited_nodes (int): Count of the number of nodes visited.
        path_size (int): Length of the path found.
    """

    # Initialize the beam with the root node
    beam = [(0, grid.start)]

    # Initialize a dictionary to store the previous nodes for each node
    previous = {}
    previous[grid.start] = grid.start

    visited_nodes: int = 0
    path_size: int = 0

    # Perform the search
    while beam:
        # Get the most promising node from the beam
        _, current = heapq.heappop(beam)

        visited_nodes += 1

        # End the search if the current node is the end node
        if current.is_end():
            path_size = count_path(previous, grid.end)
            break

        check(current)

        # Expand the current node and add its children to the beam
        children = current.neighbors

        # Remove the previous node from the list of children
        if previous[current] in children:
            children.remove(previous[current])

        # Add the children to the beam
        for child in children:
            # Skip the child if it has already been checked
            if not child.is_checked():
                previous[child] = current
                heapq.heappush(beam, (heuristic("manhattan", child, grid.end), child))

        # Trim the beam to the desired size
        beam = beam[:beam_size]
    return visited_nodes, path_size
