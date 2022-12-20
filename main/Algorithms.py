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
    "rand",
    "theta",
]


# Wrapper class to access all the pathfinding algorithms
# Default is A* pathfinding
class Algorithms:
    def __init__(self, *argv):
        self.draw = argv[0]
        self.grid = argv[1]
        self.start = argv[2]
        self.end = argv[3]

    def algorithm(self, algorithm):
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
            case "rand":
                rand_walk(self.draw, self.start, self.end)
            case "theta":
                theta_star(self.draw, self.start, self.end, self.grid)
            case _:
                a_star(self.draw, self.grid, self.start, self.end)
