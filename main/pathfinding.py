import pygame
import sys
from colors import COLORS
from node import Node
from Algorithms import Algorithms
from Algorithms import ALGORITHMS


def make_grid(rows, width):
    grid = []
    node_width = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, node_width, rows)
            grid[i].append(node)

    return grid


# Clears the grid except for the start, end, and obstacles
def clear_grid(current_grid, rows, width):
    grid = []
    node_width = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            if (
                not current_grid[i][j].is_start()
                and not current_grid[i][j].is_end()
                and not current_grid[i][j].is_obstacle()
            ):
                node = Node(i, j, node_width, rows)
                grid[i].append(node)
            else:
                grid[i].append(current_grid[i][j])

    return grid


def draw_grid_lines(win, rows, width):
    node = width // rows

    for i in range(rows):
        pygame.draw.line(win, COLORS.get("GREY"), (0, i * node), (width, i * node))
        for j in range(rows):
            pygame.draw.line(win, COLORS.get("GREY"), (j * node, 0), (j * node, width))


def draw(win, grid, rows, width):
    win.fill(COLORS.get("WHITE"))

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid_lines(win, rows, width)

    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    node = width // rows
    y, x = pos

    row = y // node
    col = x // node

    return row, col


def main(argv):
    func = None
    if len(argv) > 3:
        raise ValueError(
            "Too many arguments. arg-1: width, arg-2: # rows, alg-3: algorithm type"
        )
    if len(argv) == 3 and not argv[2] in ALGORITHMS:
        raise ValueError(
            "Invalid algorithm: please choose from the following: \n"
            + " ".join(ALGORITHMS),
        )
    elif len(argv) == 3:
        func = argv[2]
        argv.remove(func)
    if not all(x.isdigit() for x in argv):
        raise TypeError("All arguments must be integers")
    if len(argv) > 1 and int(argv[0]) < 2:
        raise ValueError("Width too small. width >= 2")
    if len(argv) == 2 and int(argv[1]) < 2:
        raise ValueError("Number of rows too small. # rows >= 2")

    width = 800 if len(argv) == 0 else int(argv[0])
    ROWS = 50 if len(argv) < 2 else int(argv[1])

    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Pathfinding Visualization")

    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    ran = False

    while run:
        draw(win, grid, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_q
            ):
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                ran = False
                grid = clear_grid(grid, ROWS, width)

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
                # Start algorithm is "SPACE" is pressed and
                # a start and end are designated
                if event.key == pygame.K_SPACE and start and end:
                    # Clear algorithm mark-up upon edit
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

                # Reset grid when the "C" key is pressed
                if event.key == pygame.K_c:
                    ran = False
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()


main(sys.argv[1:])
