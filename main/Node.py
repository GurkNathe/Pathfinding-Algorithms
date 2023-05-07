import pygame
from Colors import COLORS


# Define colors for different node states
DEFAULT = COLORS.get("WHITE")
CHECKED = COLORS.get("RED")
UNCHECKED = COLORS.get("GREEN")
OBSTACLE = COLORS.get("BLACK")
START = COLORS.get("ORANGE")
END = COLORS.get("TURQUOISE")
PATH = COLORS.get("PURPLE")


class Node:
    def __init__(self, row: int, col: int, width: int, total_rows: int):
        """
        Initializes a node with its position, size, and color.

        Args:
            row (int): row index of the node in the grid
            col (int): column index of the node in the grid
            width (int): width of the node
            total_rows (int): total number of rows in the grid
        """
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = DEFAULT
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

        # Flag for whether the node has been checked
        self.been_checked = False

        # Color for checked nodes that have been checked multiple times
        self.checked_color = None

    def get_pos(self):
        """
        Returns the position (row, column) of the node in the grid.

        Returns:
            tuple: (row, column) of the node in the grid
        """
        return self.row, self.col

    # Checking node states
    def is_default(self):
        return self.color == DEFAULT

    def is_checked(self):
        return self.color == CHECKED

    def is_unchecked(self):
        return self.color == UNCHECKED

    def is_obstacle(self):
        return self.color == OBSTACLE

    def is_start(self):
        return self.color == START

    def is_end(self):
        return self.color == END

    # Setting node states
    def check(self):
        """
        Marks the node as checked and sets the checked flag to True.
        """
        self.color = CHECKED
        self.been_checked = True
        self.checked_color = CHECKED

    def uncheck(self):
        self.color = UNCHECKED

    def make_obstacle(self):
        self.color = OBSTACLE

    def make_start(self):
        self.color = START

    def make_end(self):
        self.color = END

    def make_path(self):
        self.color = PATH

    def make_color(self, color: tuple):
        """
        Makes the node the specified color.

        Args:
            color (tuple): tuple of (R, G, B) values representing the
            desired color of the node

        Returns:
            None
        """
        self.color = color

    def mult_check(self, dec: int):
        """
        Changes the color of a checked node that has been checked multiple times.

        Args:
            dec (int): value to change the color by

        Returns:
            None
        """
        if self.checked_color[0] > dec:
            self.color = (self.checked_color[0] - dec, 0, self.checked_color[2] + dec)
            self.checked_color = self.color
        else:
            self.color = self.checked_color

    def reset(self):
        self.color = DEFAULT
        self.been_checked = False
        self.checked_color = None

    # Visualization functions
    def draw(self, win: object):
        """
        Draws the node on the given window.

        Args:
            win (pygame.Surface): window to draw the node on

        Returns:
            None
        """
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid: list):
        """
        Updates the neighbors of the node in the grid.

        Args:
            grid (List[List[Node]]): 2D list of nodes representing the grid

        Returns:
            None
        """
        self.neighbors = []

        # BOTTOM CELL
        if (
            self.row < self.total_rows - 1
            and not grid[self.row + 1][self.col].is_obstacle()
        ):
            self.neighbors.append(grid[self.row + 1][self.col])

        # TOP CELL
        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle():
            self.neighbors.append(grid[self.row - 1][self.col])

        # LEFT CELL
        if self.col > 0 and not grid[self.row][self.col - 1].is_obstacle():
            self.neighbors.append(grid[self.row][self.col - 1])

        # RIGHT CELL
        if (
            self.col < self.total_rows - 1
            and not grid[self.row][self.col + 1].is_obstacle()
        ):
            self.neighbors.append(grid[self.row][self.col + 1])

    def __lt__(self, other: object):
        """
        Comparison operator for the priority queue.

        Args:
            other (Node): node to compare to

        Returns:
            bool: False (nodes are not meant to be sorted)
        """
        return False
