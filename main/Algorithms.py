from algorithms.AStar import a_star
from algorithms.BeamSearch import beam_search
from algorithms.BellmanFord import bell_ford
from algorithms.BestFS import best_fs
from algorithms.BFS import bfs
from algorithms.bidirectional.BFS import bi_search
from algorithms.bidirectional.AStar import bi_a_star
from algorithms.BStar import b_star
from algorithms.DFS import dfs
from algorithms.Dijkstra import dijkstra
from algorithms.FloodFill import flood_fill
from algorithms.FloydWarshall import floyd_warshall
from algorithms.FastMarching import fmm
from algorithms.Fringe import fringe_search
from algorithms.GBFS import gbfs
from algorithms.GBLS import gbls
from algorithms.IDAStar import ida_star
from algorithms.IDDFS import iddfs
from algorithms.JPS import jps
from algorithms.LexicographicBFS import lbfs
from algorithms.LPAStar import lpa_star
from algorithms.RandomLIFO import rand_lifo
from algorithms.RandomWalk import rand_walk
from algorithms.SPFA import spfa
from algorithms.ThetaStar import theta_star


ALGORITHMS = [
    "astar",
    "beam",
    "bellford",
    "bestfs",
    "bfs",
    "biastar",
    "bisearch",
    "bstar",
    "dfs",
    "dijkstra",
    "flood",
    "floyd",
    "fmm",
    "fringe",
    "gbfs",
    "gbls",
    "ida",
    "iddfs",
    "jps",
    "lbfs",
    "lpa",
    "rand",
    "rand_lifo",
    "spfa",
    "theta",
]

run_algs = {
    "astar": "a_star(grid)",
    "beam": "beam_search(grid, 50)",
    "bellford": "bell_ford(grid, 1)",
    "bestfs": "best_fs(grid)",
    "bfs": "bfs(grid)",
    "biastar": "bi_a_star(grid)",
    "bisearch": "bi_search(grid)",
    "bstar": "b_star(grid)",
    "dfs": "dfs(grid)",
    "dijkstra": "dijkstra(grid)",
    "flood": "flood_fill(grid)",
    "floyd": "floyd_warshall(grid)",
    "fmm": "fmm(grid)",
    "fringe": "fringe_search(grid)",
    "gbfs": "gbfs(grid)",
    "gbls": "gbls(grid)",
    "ida": "ida_star(grid)",
    "iddfs": "iddfs(grid, len(grid.grid) * len(grid.grid[0]))",
    "jps": "jps(grid)",
    "lbfs": "lbfs(grid)",
    "lpa": "lpa_star(grid)",
    "rand": "rand_walk(grid)",
    "rand_lifo": "rand_lifo(grid)",
    "spfa": "spfa(grid)",
    "theta": "theta_star(grid)",
}


def algorithm(grid: object, algorithm: str, *args):
    """
    Select and run the specified pathfinding algorithm.

    Args:
        grid (Grid): An object representing the current grid
        algorithm (str): name of the algorithm to use

    Returns:
        None
    """
    if algorithm in run_algs:
        eval(run_algs[algorithm])
    else:
        a_star(grid)
