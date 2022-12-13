# Pathfinding/Graph Search Algorithms

This is a Python (3.10+) implementation and visualization of various pathfinding algorithms.

The graph used is an undirected, unweighted, strongly connected graph.

The visualization is implemented using PyGame. Credits to [Tech With Tim](https://www.youtube.com/watch?v=JtiK0DOeI4A).

![Best First Search](./resources/Best-First-Search.gif)

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

- Press "Q" to exit
- Press "C" to clear grid
- Left click to place Start, then End, then Obstacles
- Right click to remove Start, End, or Obstacles

After an algorithm has run:

- "W", Left, or Right click to clear the Algorithm Mark-up

While an algorithm is running:
- Press "S" key to stop the algorithm

## Algorithm Progress

```
Currently implemented algorithms (9/34):

- A\*
- Bellman Ford's Algorithm
- Best First Search
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Dijkstra's Algorithms
- Greedy Best First Search (GBFS)
- Random Walk
- Theta\*

Currently looking at:

- None

Planned algorithms (Going to look at them):

- α–β pruning

- B\*
- Beam Search
- Bidirectional search
- Branch & bound

- Concurrent Dijkstra

- D\*

- Fast Iterative Method
- Fast Marching Method
- Fast Sweeping Method
- Floyd-Warshall's algorithm
- Fringe search

- Greedy Best Line Search

- Iterative Deepening (IDA\*)
- Iterative Deepening DFS (IDDFS)

- Johnson's
- Jump Point Search (JPS)

- Kruskal's

- Lexicographic BFS
- Lifelong Planning A* (LPA*)

- SMA\*
- SSS\*
- SUB

- Viterbi algorithm

- Yen's k-Shortest Paths
```
