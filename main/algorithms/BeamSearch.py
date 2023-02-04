import pygame
import heapq
from .RP import reconstruct_path, heuristic, check, markup


def beam_search(grid: object, beam_size: int):
    """
    Perform a beam search from start to end with a given beam size.

    Args:
        grid (Grid): An object representing the current grid
        beam_size (int): The maximum number of nodes to consider at each step.

    Returns:
        None: The function updates the screen with the search progress and path.
    """

    # Initialize the beam with the root node
    beam = [(0, grid.start)]

    # Initialize a dictionary to store the previous nodes for each node
    previous = {}
    previous[grid.start] = grid.start

    # Initialize a flag to track whether the search should continue
    run = True

    # Perform the search
    while beam and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Get the most promising node from the beam
        _, current = heapq.heappop(beam)

        # End the search if the current node is the end node
        if current.is_end():
            reconstruct_path(previous, grid.end, grid.draw)
            grid.end.make_end()
            break

        # Draw the current node
        markup(grid.draw, current)

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

                # Uncheck the child if it is not the start or end node
                # for markup
                if not child.is_start() and not child.is_end():
                    child.uncheck()

        # Trim the beam to the desired size
        beam = beam[:beam_size]
