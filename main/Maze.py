import random

# Based on the code from here:
# https://github.com/OrWestSide/python-scripts/blob/master/maze.py


def surroundingCells(grid: list, y: int, x: int):
    """
    Calculate the number of unchecked cells surrounding the given cell.

    Args:
        grid (List[List[Node]]): A 2D list representing the maze grid.
        y (int): The y-coordinate of the cell.
        x (int): The x-coordinate of the cell.

    Returns:
        int: The number of unchecked cells surrounding the given cell.
    """
    s_cells = 0
    if grid[y - 1][x].is_unchecked():
        s_cells += 1
    if grid[y + 1][x].is_unchecked():
        s_cells += 1
    if grid[y][x - 1].is_unchecked():
        s_cells += 1
    if grid[y][x + 1].is_unchecked():
        s_cells += 1

    return s_cells


def delete_wall(walls: list, rand_wall: object):
    """
    Remove the given wall from the list of walls.

    Args:
        walls (list): A list of walls.
        rand_wall (Node): The wall to remove from the list.
    """
    r_x, r_y = rand_wall.get_pos()
    for wall in walls:
        w_x, w_y = wall.get_pos()
        if w_x == r_x and w_y == r_y:
            walls.remove(wall)


def check_up(grid: list, walls: list, r_y: int, r_x: int):
    """
    Check the cell above the given cell and add it to the list of walls
    if it is not checked.

    Args:
        grid (List[List[Node]]): A 2D list representing the maze grid.
        walls (List[Node]): A list of walls.
        r_y (int): The y-coordinate of the given cell.
        r_x (int): The x-coordinate of the given cell.
    """
    if r_y != 0:
        if not grid[r_y - 1][r_x].is_unchecked():
            grid[r_y - 1][r_x].make_obstacle()
        if grid[r_y - 1][r_x] not in walls:
            walls.append(grid[r_y - 1][r_x])


def check_down(grid: list, walls: list, r_y: int, r_x: int, height: int):
    """
    Check the cell below the given cell and add it to the list of walls
    if it is not checked.

    Args:
        grid (List[List[Node]]): A 2D list representing the maze grid.
        walls (List[Node]): A list of walls.
        r_y (int): The y-coordinate of the given cell.
        r_x (int): The x-coordinate of the given cell.
        height (int): The height of the grid.
    """
    if r_y != height - 1:
        if not grid[r_y + 1][r_x].is_unchecked():
            grid[r_y + 1][r_x].make_obstacle()
        if grid[r_y + 1][r_x] not in walls:
            walls.append(grid[r_y + 1][r_x])


def check_left(grid: list, walls: list, r_y: int, r_x: int):
    """
    Check the cell to the left of the given cell and add it to the
    list of walls if it is not checked.

    Args:
        grid (List[List[Node]]): A 2D list representing the maze grid.
        walls (List[Node]): A list of walls.
        r_y (int): The y-coordinate of the given cell.
        r_x (int): The x-coordinate of the given cell.
    """
    if r_x != 0:
        if not grid[r_y][r_x - 1].is_unchecked():
            grid[r_y][r_x - 1].make_obstacle()
        if grid[r_y][r_x - 1] not in walls:
            walls.append(grid[r_y][r_x - 1])


def check_right(grid: list, walls: list, r_y: int, r_x: int, width: int):
    """
    Check the cell to the right of the given cell and add it to the
    list of walls if it is not checked.

    Args:
        grid (List[List[Node]]): A 2D list representing the maze grid.
        walls (List[Node]): A list of walls.
        r_y (int): The y-coordinate of the given cell.
        r_x (int): The x-coordinate of the given cell.
        width (int): The width of the grid.
    """
    if r_x != width - 1:
        if grid[r_y][r_x + 1].is_unchecked():
            grid[r_y][r_x + 1].make_obstacle()
        if grid[r_y][r_x + 1] not in walls:
            walls.append(grid[r_y][r_x + 1])


def check_borders(
    dirs: str,
    grid: list,
    walls: list,
    r_y: int,
    r_x: int,
    width: int,
    height: int,
    rand_wall: object,
):
    """
    Checks the four neighbors of the current node and marks them accordingly.

    Args:
        dirs (str): Directions to check.
        grid (list): A 2D list representing the maze grid.
        walls (list): Current list of obstacles in the grid.
        r_y (int): Y-value of the current node.
        r_x (int): X-value of the current node.
        width (int): Number of nodes wide the grid is.
        height (int): Number of nodes tall the grid is.
        rand_wall (object): Current node.
    """
    s_cells = surroundingCells(grid, r_y, r_x)
    if s_cells < 2:
        grid[r_y][r_x].uncheck()

        if "u" in dirs:
            check_up(grid, walls, r_y, r_x)
        if "d" in dirs:
            check_down(grid, walls, r_y, r_x, height)
        if "l" in dirs:
            check_left(grid, walls, r_y, r_x)
        if "r" in dirs:
            check_right(grid, walls, r_y, r_x, width)

    delete_wall(walls, rand_wall)


def gen_maze(grid: list, start: object = None, end: object = None):
    """
    Generate a maze using the recursive backtracking algorithm.

    Args:
        grid (List[List[Node]]): A 2D list representing the maze grid.
        start (Node): The start node of the given grid.
        end (Node): The end node of the given grid.

    Returns:
        List[List[Node]]: The generated maze as a 2D list.
    """
    height = len(grid)
    width = len(grid[0])

    # Choose random starting point for the maze
    start_height = random.randint(1, len(grid) - 2)
    start_width = random.randint(1, len(grid[0]) - 2)

    walls = []

    # Mark starting cell as checked
    grid[start_height][start_width].uncheck()

    # Add the surrounding cells of the starting cell to the list of walls
    walls.append(grid[start_height - 1][start_width])
    walls.append(grid[start_height][start_width - 1])
    walls.append(grid[start_height][start_width + 1])
    walls.append(grid[start_height + 1][start_width])

    # Mark the surrounding cells of the starting cell as obstacles
    for node in walls:
        node.make_obstacle()

    # Loop until there are no more walls
    while walls:
        # Choose a random wall from the list
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Get the coordinates of the chosen wall
        r_y, r_x = rand_wall.get_pos()

        # Check if the wall is not on the left border of the grid
        if r_x != 0:
            # Check if the cell to the left of the wall is not checked and the cell
            # to the right of the wall is checked
            if grid[r_y][r_x - 1].is_default() and grid[r_y][r_x + 1].is_unchecked():
                check_borders("udl", grid, walls, r_y, r_x, width, height, rand_wall)
                continue

        # Check if the wall is not on the top border of the grid
        if r_y != 0:
            # Check if the cell above the wall is not checked and the cell below the
            # wall is checked
            if grid[r_y - 1][r_x].is_default() and grid[r_y + 1][r_x].is_unchecked():
                check_borders("ulr", grid, walls, r_y, r_x, width, height, rand_wall)
                continue

        # Check if the wall is not on the bottom border of the grid
        if r_y != height - 1:
            # Check if the cell bellow the wall is not checked and the cell above the
            # wall is checked
            if grid[r_y + 1][r_x].is_default() and grid[r_y - 1][r_x].is_unchecked():
                check_borders("dlr", grid, walls, r_y, r_x, width, height, rand_wall)
                continue

        # Check if the wall is not on the right border of the grid
        if r_x != width - 1:
            # Check if the cell to the right of the wall is not checked and the cell
            # to the left of the wall is checked
            if grid[r_y][r_x + 1].is_default() and grid[r_y][r_x - 1].is_unchecked():
                check_borders("udr", grid, walls, r_y, r_x, width, height, rand_wall)
                continue

        delete_wall(walls, rand_wall)

    # Make remaining unvisited cells walls
    for row in grid:
        for node in row:
            if node.is_default():
                node.make_obstacle()

    # Set start and end
    while not start:
        node = random.randint(1, width - 1)

        if grid[1][node].is_unchecked():
            start = grid[0][node]
            start.make_start()
            break

    while not end:
        node = random.randint(1, width - 1)

        if grid[height - 2][node].is_unchecked():
            end = grid[height - 1][node]
            end.make_end()
            break

    # Clear unchecks
    for row in grid:
        for node in row:
            if node.is_unchecked():
                node.reset()

    return start, end
