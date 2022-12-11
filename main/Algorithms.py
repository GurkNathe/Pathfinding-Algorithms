from algorithms.AStar import a_star
from algorithms.ThetaStar import theta_star
from algorithms.Dijkstra import dijkstra
from algorithms.RandomWalk import rand_walk
from algorithms.BFS import bfs
from algorithms.DFS import dfs
from algorithms.GFS import gfs

ALGORITHMS = ["astar", "bfs", "dfs", "dijkstra", "gfs", "rand", "theta"]


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
            case "rand":
                rand_walk(self.draw, self.start, self.end)
            case "dijkstra":
                dijkstra(self.draw, self.start, self.end)
            case "dfs":
                dfs(self.draw, self.start, self.end)
            case "bfs":
                bfs(self.draw, self.start, self.end)
            case "gfs":
                gfs(self.draw, self.start, self.end)
            case "theta":
                theta_star(self.draw, self.start, self.end, self.grid)
            case _:
                a_star(self.draw, self.grid, self.start, self.end)
