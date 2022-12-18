# Pathfinding/Graph Search Algorithms

This is a Python (3.10+) implementation and visualization of various pathfinding algorithms.

The graph used is an undirected, unweighted, strongly connected graph.

The visualization is implemented using PyGame. Credits to [Tech With Tim](https://www.youtube.com/watch?v=JtiK0DOeI4A).

A maze generator is implemented, however, it only has one correct path from start to end node. The implementation is based on [this](https://github.com/OrWestSide/python-scripts/blob/master/maze.py).

![A* + Maze](./resources/astar_maze.gif)

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

- Press <kbd>B</kbd> to go to previous algorithm in list
- Press <kbd>N</kbd> to go to next algorithm in list
- Press <kbd>Q</kbd> to exit
- Press <kbd>C</kbd> to clear grid
- <kbd>Left Shift</kbd> + <kbd>Left Click</kbd> to place a forbbiden node after placing Start and End nodes
- <kbd>Left Click</kbd> to place Start, then End, then Obstacles
- <kbd>Right Click</kbd> to remove Start, End, or Obstacles

After an algorithm has run:

- <kbd>W</kbd>, <kbd>Left Click</kbd>, or <kbd>Right Click</kbd> to clear the Algorithm Mark-up

While an algorithm is running:
- Press <kbd>S</kbd> key to stop the algorithm

## Node Types

- Start: where the search algorithm will start
- End: where the search algorithm is trying to get to
- Obstacle: a position the algorithms avoid
- Forbidden: a position certain algorithms avoid
- Check/Uncheck: markup for visualizing the algorithm
- Path: markup for visualizing the found path
- Default: a position that can be traversed

## Algorithm Progress

```
Currently implemented algorithms (10/34):

- A*
- Bellman Ford's Algorithm
- Best First Search
- Breadth First Search (BFS)
- B*
- Depth First Search (DFS)
- Dijkstra's Algorithms
- Greedy Best First Search (GBFS)
- Random Walk
- Theta*

Currently looking at:

- None

Planned algorithms (Going to look at them):

- α–β pruning

- Beam Search
- Bidirectional search
- Branch & bound

- Concurrent Dijkstra

- D*

- Fast Iterative Method
- Fast Marching Method
- Fast Sweeping Method
- Floyd-Warshall's algorithm
- Fringe search

- Greedy Best Line Search

- Iterative Deepening (IDA*)
- Iterative Deepening DFS (IDDFS)

- Johnson's
- Jump Point Search (JPS)

- Kruskal's

- Lexicographic BFS
- Lifelong Planning A* (LPA*)

- SMA*
- SSS*
- SUB

- Viterbi algorithm

- Yen's k-Shortest Paths
```
