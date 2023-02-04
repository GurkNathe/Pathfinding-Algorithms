import pygame
import sys
from Colors import COLORS
from Algorithms import algorithm, ALGORITHMS
from Maze import gen_maze
from Testing import Testing
from Grid import Grid


def handle_errors(argv: list, func: str):
    """
    Check for errors in the command line arguments.

    Args:
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

    Args:
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

    return Grid(win, ROWS, width)


def handle_mouse_clicks(mouse: object, ran: bool, grid: object):
    """
    Hanlde mouse left and right clicks

    Args:
        mouse (object): pygame mouse object
        ran (bool): flag set if an algorithm was previously run
        grid (Grid): An object representing the current grid

    Returns:
        ran (bool): flag set if an algorithm was previously run
        grid (Grid): An object representing the current grid
    """

    # Left mouse click
    # Add start, end, and obstacle nodes
    if mouse.get_pressed()[0]:
        # Clear algorithm mark-up upon edit
        if ran:
            ran = False
            grid.clear_grid()

        pos = mouse.get_pos()
        row, col = grid.get_clicked_pos(pos)

        # Handling for non-square window dimensions
        if row > grid.rows - 1 or col > grid.rows - 1:
            return ran, grid

        node = grid.get_cell(row, col)

        if not grid.start and node != grid.end:
            grid.start = node
            grid.start.make_start()
        elif not grid.end and node != grid.start:
            grid.end = node
            grid.end.make_end()
        elif node != grid.start and node != grid.end:
            node.make_obstacle()

    # Right mouse click
    # Remove start, end, and obstacle nodes
    elif mouse.get_pressed()[2]:
        # Clear algorithm mark-up upon edit
        if ran:
            ran = False
            grid.clear_grid()

        pos = mouse.get_pos()
        row, col = grid.get_clicked_pos(pos)

        # Handling for non-square window dimensions
        if row > grid.rows - 1 or col > grid.rows - 1:
            return ran, grid

        node = grid.get_cell(row, col)

        node.reset()

        if node == grid.start:
            grid.start = None
        elif node == grid.end:
            grid.end = None

    return ran, grid


def handle_key_presses(event: object, ran: bool, grid: object, func: str):
    """
    Handles key pressed on keyboard

    Args:
        event (object): pygame event object
        ran (bool): flag set if an algorithm was previously run
        grid (Grid): An object representing the current grid
        func (str): name of algorithm selected

    Returns:
        ran (bool): flag set if an algorithm was previously run
        grid (Grid): An object representing the current grid
        func (str): name of algorithm selected
    """
    # Start algorithm if "SPACE" is pressed and
    # a start and end are designated
    if event.key == pygame.K_SPACE and grid.start and grid.end:
        # Clear algorithm mark-up
        if ran:
            ran = False
            grid.clear_grid()

        for row in grid.grid:
            for node in row:
                node.update_neighbors(grid.grid)

        algorithm(grid, func)

        ran = True

    # Test algorithms if T key is pressed
    if event.key == pygame.K_t and grid.start and grid.end:
        Testing(grid)

    # Clear algorithm markup if W key is pressed
    if event.key == pygame.K_w:
        ran = False
        grid.clear_grid()

    # Reset grid when the "C" key is pressed
    if event.key == pygame.K_c:
        ran = False
        grid.reset_grid()

    # Go to next algorithm in list
    if event.key == pygame.K_n:
        # Clear algorithm mark-up upon edit
        if ran:
            ran = False
            grid.clear_grid()

        index = ALGORITHMS.index(func) + 1

        if index == len(ALGORITHMS):
            index = 0

        func = ALGORITHMS[index]

        pygame.display.set_caption(f"Pathfinding Visualization - {func}")

    # Go to previous algorithm in list
    if event.key == pygame.K_b:
        # Clear algorithm mark-up upon edit
        if ran:
            ran = False
            grid.clear_grid()

        index = ALGORITHMS.index(func) - 1

        if index == -1:
            index = len(ALGORITHMS) - 1

        func = ALGORITHMS[index]

        pygame.display.set_caption(f"Pathfinding Visualization - {func}")

    # Generate a new maze when "G" key is pressed
    if event.key == pygame.K_g:
        ran = False
        grid.reset_grid()
        grid.start, grid.end = gen_maze(grid.grid)

    return ran, grid, func


def quit(event: object, run: bool):
    """
    Checks if user wants to close window

    Args:
        event (object): pygame event object
        run (bool): flag indicating whether to continue running the program

    Returns:
        run (bool): flag indicating whether to continue running the program
    """
    # Quit the program if the user closes the window or presses Q
    if event.type == pygame.QUIT or (
        event.type == pygame.KEYDOWN and event.key == pygame.K_q
    ):
        run = False
    return run


def main(argv: list):
    """
    Run the Pygame window and handle user input.

    Args:
        argv (list): A list of command line arguments.q

    Returns:
        None
    """

    # Check for errors in the command line arguments and set the function
    func = handle_errors(argv, None)

    # Set up the Pygame window and grid
    grid = setup(argv, func)

    run = True
    ran = False

    # Main loop
    while run:
        # Draw the grid and nodes
        grid.draw()

        # Handle user input
        for event in pygame.event.get():
            # Check if user wants to close window
            run = quit(event, run)

            # Handle left and right mouse clicks
            ran, grid = handle_mouse_clicks(pygame.mouse, ran, grid)

            # Check if user pressed a key
            if event.type == pygame.KEYDOWN:
                ran, grid, func = handle_key_presses(event, ran, grid, func)

    pygame.quit()


main(sys.argv[1:])
