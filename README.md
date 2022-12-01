# Pathfinding Algorithms

This is a Python (3.10+) implementation and visualization of various pathfinding algorithms.

The graph used is an undirected, unweighted, strongly connected graph.

Currently implemented algorithms:

- A\*
- Random Walk

Planned algorithms:

- Dijkstra's algorithm
- Yen's k-Shortest Paths\*
- Breadth First Search (BFS)
- Depth First Search (DFS)

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

- Left or Right click to clear the Algorithm Mark-up

## A\* pathfinding algorithm:

The A\* algorithm was created and shown [here](https://www.youtube.com/watch?v=JtiK0DOeI4A) by Tech With Tim.

--- Add explanation ---

## Random Walk pathfinding algorithm:

To stop algorithm while it is running press the "S" key.

--- Add explanation ---
