import timeit
import csv
from os import system, name, path

from testing.AStar import a_star
from testing.BeamSearch import beam_search
from testing.BellmanFord import bell_ford
from testing.BestFS import best_fs
from testing.BFS import bfs
from testing.BidirectionalSearch import bi_search
from testing.BStar import b_star
from testing.DFS import dfs
from testing.Dijkstra import dijkstra
from testing.FloydWarshall import floyd_warshall
from testing.GBFS import gbfs
from testing.GBLS import gbls
from testing.IDAStar import ida_star
from testing.IDDFS import iddfs
from testing.LexicographicBFS import LBFS
from testing.RandomWalk import rand_walk
from testing.ThetaStar import theta_star
from testing.RP import get_unvisited_nodes

from Algorithms import ALGORITHMS
from Node import Node


class Testing:
    """
    Testing class for detailing various metrics for each algorithm.
    """

    def __init__(self, *argv: list):
        """
        Parameters:
            grid (List[List[Node]]): 2D list of nodes representing the grid
            start (Node): starting node
            end (Node): ending node
        """
        self.grid = argv[0]
        self.start = argv[1]
        self.end = argv[2]
        self.rows = argv[3]
        self.width = argv[4]

        # Clear grid after every run
        self.grid = self.clear_grid(self.grid, self.rows, self.width)

        for row in self.grid:
            for node in row:
                node.update_neighbors(self.grid)

        animation: list = [
            "[■□□□□□□□□□]",
            "[■■□□□□□□□□]",
            "[■■■□□□□□□□]",
            "[■■■■□□□□□□]",
            "[■■■■■□□□□□]",
            "[■■■■■■□□□□]",
            "[■■■■■■■□□□]",
            "[■■■■■■■■□□]",
            "[■■■■■■■■■□]",
            "[■■■■■■■■■■]",
        ]
        completion: int = 0

        self.clear()

        print("Testing Algorithms...")

        with open(
            path.join(
                path.dirname(__file__),
                f"testing/results/{int(timeit.default_timer())}.csv",
            ),
            "w",
            newline="",
        ) as myfile:
            wr = csv.writer(
                myfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )

            wr.writerow(
                [
                    "Algorithm",
                    "Local Run Time",
                    "Times Nodes Checked",
                    "Path Length",
                    "General Data",
                ]
            )
            algo_data: list = [
                [
                    "",
                    "",
                    "",
                    "",
                    f"Total Open Nodes: {len(get_unvisited_nodes(self.start))}",
                ]
            ]

            for alg in ALGORITHMS:
                # Clear grid after every run
                self.grid = self.clear_grid(self.grid, self.rows, self.width)

                for row in self.grid:
                    for node in row:
                        node.update_neighbors(self.grid)

                # Run and get run time of algorithm
                start_time = timeit.default_timer()
                num_visited_nodes, path_size = self.algorithm(alg)
                end_time = timeit.default_timer()

                if type(path_size) == tuple:
                    algo_data.append(
                        [
                            alg,
                            end_time - start_time,
                            num_visited_nodes,
                            path_size[1],
                            f"Turn points: {path_size[0]}",
                        ]
                    )
                else:
                    algo_data.append(
                        [alg, end_time - start_time, num_visited_nodes, path_size]
                    )

                # Progress markup
                # !!! There might be errors here in the future
                completion += 1
                index = int((completion / len(ALGORITHMS)) * len(animation))

                if alg == ALGORITHMS[-1]:
                    break

                print(
                    f" {int(100 * (completion / len(ALGORITHMS)))}% {animation[index]} \r",
                    flush=True,
                    end="",
                )

            print(f"100% {animation[9]} \rTesting Finished!", flush=True, end="")

            wr.writerows(algo_data)

    def clear_grid(self, current_grid: list, rows: int, width: int):
        """
        Clear the grid by creating a new 2D list of Node objects,
        keeping the start, end, and obstacles nodes from the
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
                # If the current node is not the start, end, or an obstacle
                # create a new Node object for the current position
                # and add it to the grid
                if (
                    not current_grid[i][j].is_start()
                    and not current_grid[i][j].is_end()
                    and not current_grid[i][j].is_obstacle()
                ):
                    node = Node(i, j, node_width, rows)
                    grid[i].append(node)

                # Otherwise, keep the original node in the grid
                else:
                    grid[i].append(current_grid[i][j])

        return grid

    def clear(self):
        # for windows
        if name == "nt":
            _ = system("cls")
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system("clear")

    def algorithm(self, algorithm: str):
        """
        Select and run the specified pathfinding algorithm.

        Parameters:
            algorithm (str): name of the algorithm to use

        Returns:
            None
        """
        match algorithm:
            case "astar":
                return a_star(self.grid, self.start, self.end)
            case "beam":
                return beam_search(self.start, self.end, 50)
            case "bellford":
                return bell_ford(self.start, self.end, 1)
            case "bestfs":
                return best_fs(self.start, self.end)
            case "bfs":
                return bfs(self.start, self.end)
            case "bisearch":
                return bi_search(self.start, self.end)
            case "bstar":
                return b_star(self.grid, self.start, self.end)
            case "dfs":
                return dfs(self.start, self.end)
            case "dijkstra":
                return dijkstra(self.start, self.end)
            case "floyd":
                return floyd_warshall(self.start, self.end, self.grid)
            case "gbfs":
                return gbfs(self.start, self.end)
            case "gbls":
                return gbls(self.start, self.end, self.grid)
            case "ida":
                return ida_star(self.start, self.end)
            case "iddfs":
                return iddfs(
                    self.start, self.end, self.grid, len(self.grid) * len(self.grid[0])
                )
            case "lbfs":
                return LBFS(self.start, self.end, self.grid)
            case "rand":
                return rand_walk(self.start, self.end)
            case "theta":
                return theta_star(self.start, self.end, self.grid)
            case _:
                return a_star(self.grid, self.start, self.end)
