import pygame
from queue import PriorityQueue
from .RP import reconstruct_path, get_unvisited_nodes, check, markup


def dijkstra(draw, start, end):
    """
    Perform Dijkstra's algorithm from start to end.
    
    Args:
        draw (function): A function used to draw the search on the screen.
        start (Node): The starting node of the search.
        end (Node): The ending node of the search.
    
    Returns:
        None: The function updates the screen with the search progress and path.
    """
    
    # Initialize a priority queue to store the nodes to visit
    queue = PriorityQueue()

    # Initialize a set to store the unvisited nodes
    unvisited_nodes = get_unvisited_nodes(start)

    # Set up the node values
    distance = {node: float("inf") for node in unvisited_nodes}
    distance[start] = 0

    # Holds the path from start to end
    previous = {}

    # Add the start node to the priority queue
    queue.put((distance[start], 0, start))
    count = 0

    # Initialize a flag to track the search status
    run = True

    # Perform the search
    while not queue.empty() and run:
        # Check for exit events
        run = check(pygame.event.get(), run)

        # Get the next node to visit
        current_distance, _, current_min = queue.get()

        # End the search if the current node is the end node
        if current_min == end:
            break

        # Draw the current node
        markup(draw, current_min)
        
        # Check the neighbors of the current node
        for neighbor in current_min.neighbors:
            # Don't recheck for performance
            if not neighbor.is_checked():
                # edges between vertecies are not weighted
                # (using constant weight of 1)
                temp_value = distance[current_min] + 1
                if temp_value < distance[neighbor]:
                    distance[neighbor] = temp_value
                    previous[neighbor] = current_min

                    # Add the neighbor to the priority queue
                    queue.put((distance[neighbor], count + 1, neighbor))
                    
                    # Uncheck the neighbor if it is not the start or end node
                    # for markup
                    if not neighbor.is_end() and not neighbor.is_start():
                        neighbor.uncheck()

        # Remove the current node from the set of unvisited nodes
        unvisited_nodes.remove(current_min)

    # Draw the path from the end node to the start node
    reconstruct_path(previous, end, draw)
