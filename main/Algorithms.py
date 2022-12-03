from algorithms.AStar import a_star
from algorithms.RandomWalk import rand_walk
from algorithms.Dijkstra import dijkstra

ALGORITHMS = ["astar", "bfs", "dfs", "dijkstra", "rand", "yen"]

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
                rand_walk(self.draw, self.grid, self.start, self.end)
            case "dijkstra":
                dijkstra(self.draw, self.grid, self.start, self.end)
            case _:
                a_star(self.draw, self.grid, self.start, self.end)
