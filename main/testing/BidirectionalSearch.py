import pygame
import threading

def count_path(path_size: list, came_from: object, current: object, target: object):
    """
    Reconstructs the path from the current node to the target node in a maze.

    Parameters:
        came_from (Dict[Node, Node]): A dictionary containing the nodes traversed
            during the pathfinding algorithm.
        current (Node): The node being checked when the algorithm terminated
        target (Node): The node to traverse back to
        draw (function): A function for drawing the maze.

    Returns:
        None
    """
    
    while current in came_from:
        if came_from[current] != target:
            current = came_from[current]
            path_size[0] += 1
        else:
            break


# This method is included for a more aesthetic reconstruction
def thread_construct(args1: tuple, args2: tuple):
    """
    Constructs two threads that will run the `reconstruct_path` function with the
    given arguments. The threads are started and then joined, which waits for
    them to finish before returning.

    Parameters:
        args1 (tuple): A tuple of arguments to pass to the first
            `reconstruct_path` function.
        args2 (tuple): A tuple of arguments to pass to the second
            `reconstruct_path` function.
    """
    # Create two threads that will run the `reconstruct_path` function with the
    # given arguments
    path1 = [0]
    path2 = [0]
    
    n1 = threading.Thread(target=count_path, args=(path1, *args1))
    n2 = threading.Thread(target=count_path, args=(path2, *args2))

    # Start the threads
    n1.start()
    n2.start()

    # Wait for the threads to finish
    n1.join()
    n2.join()
    return path1[0] + path2[0] + 1

def bi_search(start: object, end: object):
    """
    Performs a bidirectional search to find the shortest path between the
    start and end nodes.

    Parameters:
        start (Node): The starting node for the search.
        end (Node): The ending node for the search.
    """

    # Initialize two queues, one for each direction of the search
    queue_start = [start]
    queue_end = [end]

    # Initialize two sets to keep track of visited nodes, one for
    # each direction of the search
    visited_start = set()
    visited_end = set()

    # Initialize dictionaries to store the paths taken by each search direction
    start_path = {}
    end_path = {}

    # Add the start and end nodes to the path dictionaries
    start_path[start] = start
    end_path[end] = end
    
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

        visited_nodes += 2

        # Check if the nodes have already been visited from the other direction
        if start_node in visited_end:
            # Construct two threads to reconstruct the path from the start and
            # end directions
            path_size = thread_construct(
                (start_path, start_node, start), (end_path, start_node, end)
            )
            break
        if end_node in visited_start:
            # Construct two threads to reconstruct the path from the start and
            # end directions
            path_size = thread_construct(
                (start_path, end_node, start), (end_path, end_node, end)
            )
            break

        # Mark the nodes as visited
        visited_start.add(start_node)
        visited_end.add(end_node)

        # Add the neighbors of the dequeued nodes to their respective queues
        for neighbor in start_node.neighbors:
            if neighbor not in visited_start:
                queue_start.append(neighbor)
                start_path[neighbor] = start_node
        for neighbor in end_node.neighbors:
            if neighbor not in visited_end:
                queue_end.append(neighbor)
                end_path[neighbor] = end_node

    return visited_nodes, path_size