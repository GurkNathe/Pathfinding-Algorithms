from algorithms.AStar import a_star
from algorithms.BeamSearch import beam_search
from algorithms.BellmanFord import bell_ford
from algorithms.BestFS import best_fs
from algorithms.BFS import bfs
from algorithms.BStar import b_star
from algorithms.DFS import dfs
from algorithms.Dijkstra import dijkstra
from algorithms.FloydWarshall import floyd_warshall
from algorithms.GBFS import gbfs
from algorithms.GBLS import gbls
from algorithms.RandomWalk import rand_walk
from algorithms.ThetaStar import theta_star


ALGORITHMS = [
    "astar",
    "beam",
    "bellford",
    "bestfs",
    "bfs",
    "bstar",
    "dfs",
    "dijkstra",
    "floyd",
    "gbfs",
    "gbls",
    "rand",
    "theta",
]


class Algorithms:
    """
    Wrapper class to access all the pathfinding algorithms.
    Default is A* pathfinding.
    """

    def __init__(self, *argv: list):
        """
        Parameters:
            draw (function): function to draw the grid and path
            grid (List[List[Node]]): 2D list of nodes representing the grid
            start (Node): starting node
            end (Node): ending node
        """
        self.draw = argv[0]
        self.grid = argv[1]
        self.start = argv[2]
        self.end = argv[3]

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
                a_star(self.draw, self.grid, self.start, self.end)
            case "beam":
                beam_search(self.draw, self.start, self.end, 50)
            case "bellford":
                bell_ford(self.draw, self.start, self.end, 1)
            case "bestfs":
                best_fs(self.draw, self.start, self.end)
            case "bfs":
                bfs(self.draw, self.start, self.end)
            case "bstar":
                b_star(self.draw, self.grid, self.start, self.end)
            case "dfs":
                dfs(self.draw, self.start, self.end)
            case "dijkstra":
                dijkstra(self.draw, self.start, self.end)
            case "floyd":
                floyd_warshall(self.draw, self.start, self.end, self.grid)
            case "gbfs":
                gbfs(self.draw, self.start, self.end)
            case "gbls":
                gbls(self.draw, self.start, self.end, self.grid)
            case "rand":
                rand_walk(self.draw, self.start, self.end)
            case "theta":
                theta_star(self.draw, self.start, self.end, self.grid)
            case _:
                a_star(self.draw, self.grid, self.start, self.end)
