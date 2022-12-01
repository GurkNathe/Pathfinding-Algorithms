import pygame
from colors import COLORS

CHECKED = COLORS.get("RED")
UNCHECKED = COLORS.get("GREEN")
OBSTACLE = COLORS.get("BLACK")
START = COLORS.get("ORANGE")
END = COLORS.get("TURQUOISE")
PATH = COLORS.get("PURPLE")


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = COLORS.get("WHITE")
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.been_checked = False
        self.checked_color = None

    def get_pos(self):
        return self.row, self.col

    # Checking states
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

    # Setting states
    def check(self):
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

    def mult_check(self, dec):
        if self.checked_color[0] > dec:
            self.color = (self.checked_color[0] - dec, 0, 0)
            self.checked_color = self.color
        else:
            self.color = self.checked_color

    def reset(self):
        self.color = COLORS.get("WHITE")

    # Visualization functions
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
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

    def __lt__(self, other):
        return False
