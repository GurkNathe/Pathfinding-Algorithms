import time
import csv
from os import system, name, path

from testing.AStar import a_star
from testing.BeamSearch import beam_search
from testing.BellmanFord import bell_ford
from testing.BestFS import best_fs
from testing.BFS import bfs
from testing.bidirectional.AStar import bi_a_star
from testing.bidirectional.BFS import bi_search
from testing.BStar import b_star
from testing.DFS import dfs
from testing.Dijkstra import dijkstra
from testing.FloydWarshall import floyd_warshall
from testing.FloodFill import flood_fill
from testing.FastMarching import fmm
from testing.Fringe import fringe_search
from testing.GBFS import gbfs
from testing.GBLS import gbls
from testing.IDAStar import ida_star
from testing.IDDFS import iddfs
from testing.JPS import jps
from testing.LexicographicBFS import lbfs
from testing.LPAStar import lpa_star
from testing.RandomLIFO import rand_lifo
from testing.RandomWalk import rand_walk
from testing.SPFA import spfa
from testing.ThetaStar import theta_star
from testing.RP import get_unvisited_nodes

from Algorithms import ALGORITHMS, run_algs
from Node import Node


def testing(grid: object):
    """
    Main function for testing

    Args:
        grid (Grid): An object representing the current grid

    Returns:
        None
    """

    # Clear grid of any potential markup
    grid.clear_grid()

    for row in grid.grid:
        for node in row:
            node.update_neighbors(grid.grid)

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

    # Clear the terminal of all text
    clear()

    print("Testing Algorithms...")

    # Creates a new CSV file using the current time
    with open(
        path.join(
            path.dirname(__file__),
            f"testing/results/{int(time.time())}.csv",
        ),
        "w",
        newline="",
    ) as myfile:
        wr = csv.writer(myfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)

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
                f"Total Open Nodes: {len(get_unvisited_nodes(grid.start))}",
            ]
        ]

        for alg in ALGORITHMS:
            # Clear grid after every run
            grid.clear_grid()

            for row in grid.grid:
                for node in row:
                    node.update_neighbors(grid.grid)

            # Run and get statistics for ran algorithm
            start_time = time.perf_counter()
            num_visited_nodes, path_size = algorithm(grid, alg)
            end_time = time.perf_counter()

            # Used for handling Theta* turn points
            # ! Will most likely change in the future when more data is being collected 
            # ! from each algorithm
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
            # ? Unreplicable error with printing the completion animation
            completion += 1
            index = int((completion / len(ALGORITHMS)) * len(animation))

            if alg == ALGORITHMS[-1]:
                break

            print(
                f" {int(100 * (completion / len(ALGORITHMS)))}% {animation[index]} \r",
                flush=True,
                end="",
            )

        print(f"100% {animation[9]} \rTesting Finished!\n", flush=True, end="")

        wr.writerows(algo_data)
        grid.clear_grid()


def clear():
    # For Windows
    if name == "nt":
        _ = system("cls")
    # For MacOS and Linux
    else:
        _ = system("clear")


def algorithm(grid: object, algorithm: str):
    """
    Select and run the specified pathfinding algorithm.

    Args:
        grid (Grid): An object representing the current grid
        algorithm (str): name of the algorithm to use

    Returns:
        int: The number of nodes visited in the algorithm
        int or tuple: Length of path found; number of turning points
    """
    return eval(run_algs[algorithm])
