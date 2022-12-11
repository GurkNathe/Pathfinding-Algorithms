# Pathfinding/Graph Search Algorithms

This is a Python (3.10+) implementation and visualization of various pathfinding algorithms.

The graph used is an undirected, unweighted, strongly connected graph.

Currently implemented algorithms (7/32):

- A\*
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

- Yen's k-Shortest Paths

The visualization is implemented using PyGame. Credits to [Tech With Tim](https://www.youtube.com/watch?v=JtiK0DOeI4A).

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

## A\* pathfinding algorithm:

The A\* algorithm was created and shown [here](https://www.youtube.com/watch?v=JtiK0DOeI4A) by Tech With Tim.

The A\* algorithm is a type of best-first search algorithm that uses a combination of a heuristic function and the cost of each path to determine the most efficient path to take. 

The algorithm works by starting at the start point and exploring possible paths in a way that prioritizes paths that are likely to lead to the end point. It does this by using a heuristic function to estimate the cost of each path, and then selecting the path with the lowest estimated cost. 

As the algorithm continues to explore paths, it updates the estimated cost of each path based on the actual cost of the path and the heuristic function. This allows the algorithm to continually refine its search and find the shortest path to the end point.

## Breadth First Search (BFS) pathfinding algorithm:


BFS works by starting at a given vertex and exploring all of its neighbors before moving on to any of their neighbors. This means that the algorithm will visit all of the vertices in a given layer of the graph before moving on to the next layer. This continues until all vertices in the graph have been visited or the desired vertex has been found.

To implement BFS, a queue is typically used to store the vertices that are yet to be visited. We start by adding the starting vertex to the queue, and then we repeatedly take the next vertex from the queue, visit it, and add all of its unvisited neighbors to the queue. This process continues until the queue is empty, at which point all vertices in the graph have been visited.

## Depth First Search (DFS) pathfinding algorithm:


DFS works by starting at a given vertex and exploring as far as possible along each branch before backtracking. This means that the algorithm will visit all of the vertices in a given branch of the graph before moving on to the next branch. This continues until all vertices in the graph have been visited or the desired vertex has been found.

To implement DFS, a stack is typically used to store the vertices that are yet to be visited. We start by adding the starting vertex to the stack, and then we repeatedly take the next vertex from the stack, visit it, and add all of its unvisited neighbors to the stack. This process continues until the stack is empty, at which point all vertices in the graph have been visited.

## Dijkstra's pathfinding algorithm:


Dijkstra's pathfinding algorithm is a type of best-first search algorithm that uses a priority queue to store the vertices that are yet to be visited. The algorithm works by starting at the starting vertex and exploring all of its neighbors, updating the cost of each path based on the actual cost of the path and the current estimated cost of the path. As the algorithm continues to explore paths, it updates the estimated cost of each path and selects the path with the lowest estimated cost. This allows the algorithm to continually refine its search and find the shortest path to the end point.

To implement Dijkstra's algorithm, we first initialize a priority queue and add the starting vertex to it. We then repeatedly take the next vertex from the priority queue, visit it, and add all of its unvisited neighbors to the priority queue. When adding a vertex to the priority queue, we update the estimated cost of the path to that vertex based on the actual cost of the path and the current estimated cost of the path. This process continues until the end vertex is reached or all vertices in the graph have been visited.

## Greedy Best First Search (GBFS) pathfinding algorithm:


The greedy best-first search (GBFS) algorithm is a type of best-first search algorithm that uses a heuristic function to prioritize the exploration of paths that are likely to lead to the end point. It works by starting at the start point and exploring possible paths in a way that prioritizes paths with the lowest estimated cost. This means that the algorithm will always choose the path with the lowest estimated cost, regardless of whether that path actually leads to the end point.

To implement GBFS, we first initialize a priority queue and add the starting vertex to it. We then repeatedly take the next vertex from the priority queue, visit it, and add all of its unvisited neighbors to the priority queue. When adding a vertex to the priority queue, we update the estimated cost of the path to that vertex based on the heuristic function. This process continues until the end vertex is reached or all vertices in the graph have been visited.

## Random Walk pathfinding algorithm:

The random walk algorithm is a type of pathfinding algorithm that uses a random exploration strategy to find a path between two points. It works by starting at the start point and randomly selecting one of the available neighbors to explore. This process is repeated until the end point is reached or all possible paths have been explored.

## Theta\* pathfinding algorithm:

Like A*, Theta* uses a combination of a heuristic function and the cost of each path to determine the most efficient path to take. However, unlike A*, Theta* uses a more advanced search strategy that allows it to find the shortest path to the end point more efficiently.

To implement Theta*, we first initialize a priority queue and add the starting vertex to it. We then repeatedly take the next vertex from the priority queue, visit it, and add all of its unvisited neighbors to the priority queue. When adding a vertex to the priority queue, we update the estimated cost of the path to that vertex based on the actual cost of the path and the current estimated cost of the path. Additionally, we use a special search strategy that allows us to prune the search space and avoid exploring paths that are unlikely to lead to the end point. This process continues until the end vertex is reached or all vertices in the graph have been visited.