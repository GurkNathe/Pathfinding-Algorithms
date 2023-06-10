from Node import Node
import pygame


class Grid:
    def __init__(self, win: object, ROWS: int, width: int):
        self.rows = ROWS
        self.width = width
        self.node_width = width // ROWS
        self.win = win
        self.grid = []
        self.start = None
        self.end = None

        self.make_grid()

    def reset_grid(self):
        self.start = None
        self.end = None
        self.make_grid()

    def get_clicked_pos(self, pos: tuple):
        """
        Get the position of the node that was clicked in the grid.

        Args:
            pos (tuple): A tuple containing the x and y coordinates of the mouse click.
            rows (int): The number of rows in the grid.
            width (int): The width of the grid in pixels.

        Returns:
            tuple: A tuple containing the row and column indices of the clicked node.
        """
        # Unpack the x and y coordinates of the mouse click
        y, x = pos

        # Calculate the row and column index of the clicked node
        row = y // self.node_width
        col = x // self.node_width

        return row, col

    def make_grid(self):
        """
        Create a 2D list representing the grid of the maze.

        Args:
            rows (int): The number of rows in the grid.
            width (int): The width of the grid in pixels.

        Returns:
            List[List[Node]]: A 2D list of Node objects representing the grid.
        """
        grid = []

        # Iterate through the rows and columns of the grid
        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                # Create a new Node object for the current position and
                # add it to the grid
                node = Node(i, j, self.node_width, self.rows)
                grid[i].append(node)

        self.grid = grid

    def clear_grid(self):
        """
        Clear the grid by creating a new 2D list of Node objects,
        keeping the start, end, and obstacles nodes from the
        original grid.

        Args:
            current_grid (List[List[Node]]): The original grid.
            rows (int): The number of rows in the grid.
            width (int): The width of the grid in pixels.

        Returns:
            List[List[Node]]: A 2D list of Node objects representing the cleared grid.
        """
        grid = []

        # Iterate through the rows and columns of the grid
        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                # If the current node is not the start, end, or an obstacle, create a new Node
                # object for the current position and add it to the grid
                if (
                    not self.grid[i][j].is_start()
                    and not self.grid[i][j].is_end()
                    and not self.grid[i][j].is_obstacle()
                ):
                    node = Node(i, j, self.node_width, self.rows)
                    grid[i].append(node)

                # Otherwise, keep the original node in the grid
                else:
                    grid[i].append(self.grid[i][j])

        self.grid = grid

    def draw_grid_lines(self):
        """
        Draw the lines separating the nodes in the grid.

        Args:
            None

        Returns:
            None
        """
        for i in range(self.rows):
            # Draw a horizontal line at the top and bottom of each node
            pygame.draw.line(
                self.win,
                (128, 128, 128),
                (0, i * self.node_width),
                (self.width, i * self.node_width),
            )
            for j in range(self.rows):
                # Draw a vertical line at the left and right of each node
                pygame.draw.line(
                    self.win,
                    (128, 128, 128),
                    (j * self.node_width, 0),
                    (j * self.node_width, self.width),
                )

    def draw(self):
        """
        Draw the grid and nodes on the window.

        Args:
            None

        Returns:
            None
        """
        self.win.fill((255, 255, 255))

        # Draw nodes on grid
        for row in self.grid:
            for node in row:
                node.draw(self.win)

        self.draw_grid_lines()

        pygame.display.update()

    def __getitem__(self, key):
        return self.grid[key]