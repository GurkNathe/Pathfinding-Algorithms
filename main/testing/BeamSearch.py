import heapq
from .RP import heuristic, check


def beam_search(start: object, end: object, beam_size: int):
    """
    Perform a beam search from start to end with a given beam size.

    Args:
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.
        beam_size (int): The maximum number of nodes to consider at each step.

    Returns:
        None
    """

    # Initialize the beam with the root node
    beam = [(0, start)]

    # Initialize a dictionary to store the previous nodes for each node
    previous = {}
    previous[start] = start
    
    visited_nodes: int = 0

    # Perform the search
    while beam:
        # Get the most promising node from the beam
        _, current = heapq.heappop(beam)

        visited_nodes += 1

        # End the search if the current node is the end node
        if current.is_end():
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
                heapq.heappush(beam, (heuristic("manhattan", child, end), child))

        # Trim the beam to the desired size
        beam = beam[:beam_size]
    return visited_nodes