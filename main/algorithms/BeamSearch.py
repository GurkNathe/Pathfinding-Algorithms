import pygame
import heapq
from .RP import reconstruct_path, heuristic, check, markup


def beam_search(draw, start, end, beam_size):
    # Initialize the beam with the root node
    beam = [(0, start)]

    previous = {}
    previous[start] = start

    run = True

    # Continue searching until the beam is empty
    while beam and run:
        run = check(pygame.event.get(), run)
        # Take the most promising node from the beam
        _, current = heapq.heappop(beam)

        # If the node is a goal node, return the path to it
        if current.is_end():
            reconstruct_path(previous, end, draw)
            end.make_end()
            break

        markup(draw, current)

        # Expand the node and add its children to the beam
        children = current.neighbors

        if previous[current] in children:
            children.remove(previous[current])

        for child in children:
            if not child.is_checked():
                previous[child] = current
                heapq.heappush(beam, (heuristic("manhattan", child, end), child))

        # Trim the beam to the desired size
        beam = beam[:beam_size]
