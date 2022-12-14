import pygame
import sys
from colors import COLORS
from node import Node
from Algorithms import Algorithms, ALGORITHMS
from Maze import gen_maze


def make_grid(rows: int, width: int):
    """
    Create a 2D list representing the grid of the maze.

    Parameters:
        rows (int): The number of rows in the grid.
        width (int): The width of the grid in pixels.

    Returns:
        List[List[Node]]: A 2D list of Node objects representing the grid.
    """
    grid = []

    # Calculate the width of each node in the grid
    node_width = width // rows

    # Iterate through the rows and columns of the grid
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            # Create a new Node object for the current position and
            # add it to the grid
            node = Node(i, j, node_width, rows)
            grid[i].append(node)

    return grid


def clear_grid(current_grid: list, rows: int, width: int):
    """
    Clear the grid by creating a new 2D list of Node objects,
    keeping the start, end, obstacles and forbidden nodes from the
    original grid.

    Parameters:
        current_grid (List[List[Node]]): The original grid.
        rows (int): The number of rows in the grid.
        width (int): The width of the grid in pixels.

    Returns:
        List[List[Node]]: A 2D list of Node objects representing the cleared grid.
    """
    grid = []

    # Calculate the width of each node in the grid
    node_width = width // rows

    # Iterate through the rows and columns of the grid
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            # If the current node is not the start, end, an obstacle or
            # forbidden, create a new Node object for the current position
            # and add it to the grid
            if (
                not current_grid[i][j].is_start()
                and not current_grid[i][j].is_end()
                and not current_grid[i][j].is_obstacle()
                and not current_grid[i][j].is_forbidden()
            ):
                node = Node(i, j, node_width, rows)
                grid[i].append(node)

            # Otherwise, keep the original node in the grid
            else:
                grid[i].append(current_grid[i][j])

    return grid


def draw_grid_lines(win: object, rows: int, width: int):
    """
    Draw the lines separating the nodes in the grid.

    Parameters:
        win (pygame.Surface): The pygame window to draw on.
        rows (int): The number of rows in the grid.
        width (int): The width of the grid in pixels.

    Returns:
        None
    """
    # Calculate the width of each node in the grid
    node = width // rows

    for i in range(rows):
        # Draw a horizontal line at the top and bottom of each node
        pygame.draw.line(win, COLORS.get("GREY"), (0, i * node), (width, i * node))
        for j in range(rows):
            # Draw a vertical line at the left and right of each node
            pygame.draw.line(win, COLORS.get("GREY"), (j * node, 0), (j * node, width))


def draw(win, grid: list, rows: int, width: int):
    """
    Draw the grid and nodes on the window.

    Parameters:
        win (pygame.Surface): The window to draw on.
        grid (List[List[Node]]): A 2D list of Node objects representing the grid.
        rows (int): The number of rows in the grid.
        width (int): The width of the grid in pixels.
    """
    win.fill(COLORS.get("WHITE"))

    # Draw nodes on grid
    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid_lines(win, rows, width)

    pygame.display.update()


def get_clicked_pos(pos: tuple, rows: int, width: int):
    """
    Get the position of the node that was clicked in the grid.

    Parameters:
        pos (tuple): A tuple containing the x and y coordinates of the mouse click.
        rows (int): The number of rows in the grid.
        width (int): The width of the grid in pixels.

    Returns:
        tuple: A tuple containing the row and column indices of the clicked node.
    """

    # Calculate the width of a node in the grid
    node = width // rows

    # Unpack the x and y coordinates of the mouse click
    y, x = pos

    # Calculate the row and column index of the clicked node
    row = y // node
    col = x // node

    return row, col


def handle_errors(argv: list, func: str):
    """
    Check for errors in the command line arguments.

    Parameters:
        argv (list): A list of command line arguments.
        func (str): The name of the pathfinding algorithm.

    Returns:
        str: The name of the pathfinding algorithm.

    Raises:
        ValueError: If there are too many arguments or an invalid algorithm is specified.
        TypeError: If any of the arguments are not integers.
        ValueError: If the width or number of rows is too small.
    """

    # Check if there are too many arguments
    if len(argv) > 3:
        raise ValueError(
            "Too many arguments. arg-1: width, arg-2: # rows, alg-3: algorithm type"
        )

    # Check if the algorithm is specified and if it is valid
    if len(argv) == 3 and not argv[2] in ALGORITHMS:
        raise ValueError(
            "Invalid algorithm: please choose from the following: \n"
            + " ".join(ALGORITHMS),
        )

    # If the algorithm is specified and valid, set it as the function
    elif len(argv) == 3:
        func = argv[2]

        # Remove the algorithm from the list of arguments
        argv.remove(func)

    # Check if all of the arguments are integers
    if not all(x.isdigit() for x in argv):
        raise TypeError("All arguments must be integers")
    if len(argv) > 1 and int(argv[0]) < 2:
        raise ValueError("Width too small. width >= 2")
    if len(argv) == 2 and int(argv[1]) < 2:
        raise ValueError("Number of rows too small. # rows >= 2")

    if not func:
        func = "astar"

    return func


def setup(argv: list, func: str):
    """
    Set up the Pygame window and grid.

    Parameters:
        argv (list): A list of command line arguments.

    Returns:
    tuple: The start and end coordinates as tuples, the grid as a 2D list,
            the Pygame window, the width of the window, and the number of
            rows in the grid.
    """

    # Set the default width and number of rows if no arguments are given
    width = 800 if len(argv) == 0 else int(argv[0])
    ROWS = 50 if len(argv) < 2 else int(argv[1])

    # Create the Pygame window
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption(f"Pathfinding Visualization - {func}")

    # Create the grid
    grid = make_grid(ROWS, width)

    return None, None, grid, win, width, ROWS


def main(argv: list):
    """
    Run the Pygame window and handle user input.

    Parameters:
        argv (list): A list of command line arguments.

    Returns:
        None
    """

    # Check for errors in the command line arguments and set the function
    func = handle_errors(argv, None)

    # Set up the Pygame window and grid
    start, end, grid, win, width, ROWS = setup(argv, func)

    run = True
    ran = False

    print(func)

    # Main loop
    while run:
        # Draw the grid and nodes
        draw(win, grid, ROWS, width)

        # Handle user input
        for event in pygame.event.get():
            # Quit the program if the user closes the window
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_q
            ):
                run = False

            # Left mouse click
            # Add start, end, and obstacle nodes
            if pygame.mouse.get_pressed()[0]:
                # Clear algorithm mark-up upon edit
                if ran:
                    ran = False
                    grid = clear_grid(grid, ROWS, width)

                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)

                # Handling for non-square window dimensions
                if row > ROWS - 1 or col > ROWS - 1:
                    continue

                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != start and node != end:
                    if pygame.key.get_mods() & pygame.K_LSHIFT:
                        node.make_forbbiden()
                    else:
                        node.make_obstacle()

            # Right mouse click
            # Remove start, end, and obstacle nodes
            elif pygame.mouse.get_pressed()[2]:
                # Clear algorithm mark-up upon edit
                if ran:
                    ran = False
                    grid = clear_grid(grid, ROWS, width)

                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)

                # Handling for non-square window dimensions
                if row > ROWS - 1 or col > ROWS - 1:
                    continue

                node = grid[row][col]

                node.reset()

                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                # Start algorithm if "SPACE" is pressed and
                # a start and end are designated
                if event.key == pygame.K_SPACE and start and end:
                    # Clear algorithm mark-up
                    if ran:
                        ran = False
                        grid = clear_grid(grid, ROWS, width)

                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    Algorithms(
                        lambda: draw(win, grid, ROWS, width), grid, start, end
                    ).algorithm(func)

                    ran = True

                # Clear algorithm markup if W key is pressed
                if event.key == pygame.K_w:
                    ran = False
                    grid = clear_grid(grid, ROWS, width)

                # Reset grid when the "C" key is pressed
                if event.key == pygame.K_c:
                    ran = False
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

                # Go to next algorithm in list
                if event.key == pygame.K_n:
                    # Clear algorithm mark-up upon edit
                    if ran:
                        ran = False
                        grid = clear_grid(grid, ROWS, width)

                    index = ALGORITHMS.index(func) + 1

                    if index == len(ALGORITHMS):
                        index = 0

                    func = ALGORITHMS[index]

                    print(func)
                    pygame.display.set_caption(f"Pathfinding Visualization - {func}")

                # Go to previous algorithm in list
                if event.key == pygame.K_b:
                    # Clear algorithm mark-up upon edit
                    if ran:
                        ran = False
                        grid = clear_grid(grid, ROWS, width)

                    index = ALGORITHMS.index(func) - 1

                    if index == -1:
                        index = len(ALGORITHMS) - 1

                    func = ALGORITHMS[index]

                    print(func)
                    pygame.display.set_caption(f"Pathfinding Visualization - {func}")

                # Generate a new maze when "G" key is pressed
                if event.key == pygame.K_g:
                    ran = False
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                    start, end = gen_maze(grid)

    pygame.quit()


main(sys.argv[1:])
