# Algorithm explanation documentation

## A\* pathfinding algorithm:

The A\* algorithm was created and shown [here](https://www.youtube.com/watch?v=JtiK0DOeI4A) by Tech With Tim.

The A\* algorithm is a type of best-first search algorithm that uses a combination of a heuristic function and the cost of each path to determine the most efficient path to take. 

The algorithm works by starting at the start point and exploring possible paths in a way that prioritizes paths that are likely to lead to the end point. It does this by using a heuristic function to estimate the cost of each path, and then selecting the path with the lowest estimated cost. 

As the algorithm continues to explore paths, it updates the estimated cost of each path based on the actual cost of the path and the heuristic function. This allows the algorithm to continually refine its search and find the shortest path to the end point.

## Bellman-Ford's pathfinding algorithm:

The Bellman-Ford's pathfinding algorithm works by initially setting the distance from the source node to all other nodes in the graph to infinity, and the predecessor for all nodes to null. It then repeatedly relaxes the edges in the graph, updating the distance and predecessor values for each node. This is repeated for each node in the graph, until all distances and predecessors have been correctly updated.

Here's a high-level overview of the algorithm:

1. Set the distance from the source node to all other nodes in the graph to infinity, and the predecessor for all nodes to null.
2. For each node in the graph, do the following:
    - Relax the edges leaving the current node.
    - Update the distance and predecessor values for each neighbor of the current node if a shorter path is found.
3. Repeat step 2 for each node in the graph, until all distances and predecessors have been correctly updated.

Once the algorithm has completed, the distance and predecessor values for each node in the graph will contain the correct shortest path information. These values can then be used to reconstruct the shortest path from the source node to any other node in the graph.

In this implementation of Bellman-Ford's algorithm, there is no check for negative edge weights/cycles. This is due to the nature of this implementation, where each weight between two nodes is always 1, and never negative.

## Best-First Search pathfinding algorithm:

Best first search is a type of search algorithm that uses a heuristic evaluation function to prioritize the nodes in the search space. The algorithm starts at the starting node and explores the neighbor nodes in order of their estimated cost to the goal. The estimated cost of a node is calculated using a heuristic function, which provides an estimate of the minimum cost from the current node to the goal. This allows the algorithm to focus on the most promising nodes first, and avoid exploring parts of the search space that are unlikely to lead to the goal.

The algorithm continues to explore the neighbor nodes and expand the search space until the goal is reached, or until all possible paths have been explored. If the goal is found, the algorithm returns the minimum cost path from the start to the goal. If no path is found, the algorithm returns failure.

Best first search can be implemented using a priority queue to store the nodes that need to be explored. The priority queue is ordered by the estimated cost of each node, with the node that has the lowest estimated cost being at the top of the queue. The algorithm then repeatedly takes the top node from the queue, expands it to explore its neighbor nodes, and adds the neighbor nodes to the queue. This process continues until the goal is reached or the queue is empty.


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