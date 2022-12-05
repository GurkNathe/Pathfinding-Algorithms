def reconstruct_path(came_from, current, draw):
    """
    came_from : dictionary of nodes traversed in the algorithm
    current : end node
    draw : pygame draw function
    """
    while current in came_from:
        if not came_from[current].is_start():
            current = came_from[current]
            current.make_path()
            draw()
        else:
            break
