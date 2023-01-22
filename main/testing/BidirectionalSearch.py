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

    # Loop until one of the queues is empty
    while queue_start and queue_end:
        # Dequeue a node from each queue and process it
        node1 = queue_start.pop(0)
        # Check for redundant checks
        if node1 in visited_start:
            continue

        node2 = queue_end.pop(0)
        # Check for redundant checks
        if node2 in visited_end:
            queue_start.insert(0, node1)
            continue

        visited_nodes += 2

        # Check if the nodes have already been visited from the other direction
        if node1 in visited_end:
            break
        if node2 in visited_start:
            break

        # Mark the nodes as visited
        visited_start.add(node1)
        visited_end.add(node2)

        # Add the neighbors of the dequeued nodes to their respective queues
        for neighbor in node1.neighbors:
            if neighbor not in visited_start:
                queue_start.append(neighbor)
                start_path[neighbor] = node1
        for neighbor in node2.neighbors:
            if neighbor not in visited_end:
                queue_end.append(neighbor)
                end_path[neighbor] = node2
    return visited_nodes