# Pathfinding/Graph Search Algorithms ![License: MIT](https://img.shields.io/badge/License-GPL_3.0-red.svg)

This is a Python (3.10+) implementation and visualization of various pathfinding algorithms.

The graph used is a static, undirected, unweighted, strongly connected graph (aka, a grid that doesn't change while algorithm is running).

The visualization is implemented using PyGame. Credits to [Tech With Tim](https://www.youtube.com/watch?v=JtiK0DOeI4A).

A maze generator is implemented, however, it only has one correct path from start to end node. The implementation is based on [this](https://github.com/OrWestSide/python-scripts/blob/master/maze.py).

![A* + Maze](./resources/astar_maze.gif)

See the explanations for the implemented algorithms [here](./resources/Explanations.md).

## Command line arguments

There are three optional command line arguments: width, # rows, algorithm type.

```
width >= 2
rows >= 2
algorithm = astar, bfs, dfs, dijkstra, rand, yen [See line 8 of Algorithms.py for full list]
```

```
./pathfinding.py <width> <# rows> <algorithm type>
```

## Keydown Events

While an algorithm isn't running:

- Press <kbd>T</kbd> to test algorithms
- Press <kbd>B</kbd> to go to previous algorithm in list
- Press <kbd>N</kbd> to go to next algorithm in list
- Press <kbd>Q</kbd> to exit
- Press <kbd>C</kbd> to clear grid
- Press <kbd>G</kbd> to generate a new maze
- <kbd>Left Click</kbd> to place Start, then End, then Obstacles
- <kbd>Right Click</kbd> to remove Start, End, or Obstacles

After an algorithm has run:

- <kbd>W</kbd>, <kbd>Left Click</kbd>, or <kbd>Right Click</kbd> to clear the Algorithm Mark-up

While an algorithm is running:

- Press <kbd>S</kbd> key to stop the algorithm

## Testing

The testing function runs every implemented algorithm for the current grid. It outputs the time it took to run the algorithm and the number of node checks while running. The results are written into a CSV file, which can be found in the `main/testing/results` directory. An example output is given for a randomly generated maze, with default settings.

The testing will take longer as the visitable nodes increases. For my system, and a randomly generated maze on default settings, it takes ~4 minutes to run and save the data.

## Node Types

- Start: where the search algorithm will start
- End: where the search algorithm is trying to get to
- Obstacle: a position the algorithms avoid
- Check/Uncheck: markup for visualizing the algorithm
- Path: markup for visualizing the found path
- Default: a position that can be traversed

## Algorithm Progress

```
Currently implemented algorithms (17/33):

- A*
- Beam Search
- Bellman Ford's Algorithm
- Best First Search
- Bidirectional search
- Breadth First Search (BFS)
- B*
- Depth First Search (DFS)
- Dijkstra's Algorithms
- Floyd-Warshall's algorithm
- Greedy Best First Search (GBFS)
- Greedy Best Line Search (GBLS)
- Iterative Deepening (IDA*)
- Iterative Deepening DFS (IDDFS)
- Lexicographic BFS
- Random Walk
- Theta*

Currently looking at:

- None

Planned algorithms (Going to look at them):

- α–β pruning

- Branch & bound

- Concurrent Dijkstra

- Fast Iterative Method
- Fast Marching Method
- Fast Sweeping Method
- Fringe search

- Johnson's
- Jump Point Search (JPS)

- Kruskal's

- Lifelong Planning A* (LPA*)

- SMA*
- SSS*
- SUB

- Viterbi algorithm

- Yen's k-Shortest Paths
```

Possible Incorrectly Implemented algorithms:

- [B*](./resources/b_star.pdf)