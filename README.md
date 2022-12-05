# Pathfinding/Graph Search Algorithms

This is a Python (3.10+) implementation and visualization of various pathfinding algorithms.

The graph used is an undirected, unweighted, strongly connected graph.

Currently implemented algorithms:

- A\*
- Random Walk
- Dijkstra's Algorithms
- Breadth First Search (BFS)
- Depth First Search (DFS)

Currently looking at:

- Best First Search

Planned algorithms (Going to look at them):

- α–β pruning

- B\*
- Basic Theta\*
- Beam Search
- Bellman Ford's Algorithm
- Bidirectional search
- Branch & bound

- Concurrent Dijkstra

- D\*

- Fast Iterative Method
- Fast Marching Method
- Fast Sweeping Method
- Floyd-Warshall's algorithm
- Fringe search

- Iterative Deepening (IDA\*)
- Iterative Deepening DFS (IDDFS)

- Johnson's
- Jump Point Search (JPS)

- Kruskal's

- Lexicographic BFS
- Lifelong Planning A* (LPA*)

- SMA\*
- SUB

- Yen's k-Shortest Paths

The visualization is implemented using PyGame. Credits to [Tech With Tim](https://www.youtube.com/watch?v=JtiK0DOeI4A).

## Command line arguments

There are three optional command line arguments: width, # rows, algorithm type.

```
width >= 2
rows >= 2
algorithm = astar, bfs, dfs, dijkstra, rand, yen
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

## A\* pathfinding algorithm:

The A\* algorithm was created and shown [here](https://www.youtube.com/watch?v=JtiK0DOeI4A) by Tech With Tim.

--- Add explanation ---

## Random Walk pathfinding algorithm:

To stop algorithm while it is running press the "S" key.

From the starting node choose a random neighbor node to check.
If the node is the end, stop; if the node isn't the end, choose a random neighbor of it and repeat until the end is reached.

This algorithm is literally randomly guessing a route from start to end, it is by no means ment to be taken serious and was just something fun to look at.

## Breadth First Search (BFS) pathfinding algorithm:

To stop algorithm while it is running press the "S" key.

--- Add explanation ---

## Depth First Search (DFS) pathfinding algorithm:

To stop algorithm while it is running press the "S" key.

--- Add explanation ---

## Dijkstra's pathfinding algorithm:

To stop algorithm while it is running press the "S" key.

--- Add explanation ---
