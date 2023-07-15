# Algorithm explanation documentation

<strong/> Disclaimer: A large portion of the documentation below was generated using ChatGPT, take what is written here with a grain of salt since ChatGPT is not infallible.</strong>

# Table of contents
1. [A*](#a-pathfinding-algorithm)
2. [Beam Search](#beam-search)
3. [Bellman-Ford's Algorithm](#bellman-fords-pathfinding-algorithm)
4. [Best First Search](#best-first-search-pathfinding-algorithm)
4. [Bidirectional Search Algorithms](#bidirectional-search-algorithms)
4. [Bidirectional Search](#bidirectional-search-pathfinding-algorithm)
5. [Breadth First Search](#breadth-first-search-bfs-pathfinding-algorithm)
5. [Branch & Bound](#branch--bound-pathfinding-algorithm)
6. [B*](#b-pathfinding-algorithm)
7. [Depth First Search](#depth-first-search-dfs-pathfinding-algorithm)
8. [Dijkstra's Algorithm](#dijkstras-pathfinding-algorithm)
8. [Fast Marching Method](#fast-marching-method)
9. [Flood Fill Algorithm](#flood-fill-algorithm)
9. [Floyd-Warshall's Algorithm](#floyd-warshalls-algorithm)
10. [Greedy Best-First Search](#greedy-best-first-search-gbfs-pathfinding-algorithm)
11. [Greedy Best Line Search](#greedy-best-line-search-gbls-pathfinding-algorithm)
11. [Iterative Deepening A*](#iterative-deepening-a-pathfinding-algorithm)
11. [Iterative Deepening DFS](#iterative-deepening-dfs-pathfinding-algorithm)
11. [Jump Point Search](#jump-point-search-jps-pathfinding-algorithm)
11. [Lexicographic BFS](#lexicographic-bfs-pathfinding-algorithm)
11. [Lifelong Planning A*](#lifelong-planning-a-pathfinding-algorithm)
12. [Random Walk Algorithm](#random-walk-pathfinding-algorithm)
13. [Theta*](#theta-pathfinding-algorithm)

## A\* pathfinding algorithm:

The A\* algorithm implemented here was created and shown [here](https://www.youtube.com/watch?v=JtiK0DOeI4A) by Tech With Tim.

The A\* algorithm is a type of best-first search algorithm that uses a combination of a heuristic function and the cost of each path to determine the most efficient path to take.

The algorithm works by starting at the start point and exploring possible paths in a way that prioritizes paths that are likely to lead to the end point. It does this by using a heuristic function to estimate the cost of each path, and then selecting the path with the lowest estimated cost.

As the algorithm continues to explore paths, it updates the estimated cost of each path based on the actual cost of the path and the heuristic function. This allows the algorithm to continually refine its search and find the shortest path to the end point.

## Beam Search:

Beam search is a heuristic search algorithm that is used to explore a graph by expanding the most promising nodes in a limited set, rather than exploring all nodes in the graph.

The basic operation of beam search in a graph is similar to that in a tree, with a few key differences:

1. Root node: The search begins at a root node, which is the starting point for the search.

2. Beam: The beam is a fixed-size list of the most promising nodes that are currently being explored. The beam is initialized with the root node, and new nodes are added to the beam as they are expanded.

3. Expansion: To expand a node, the search generates a list of child nodes that are reachable from the current node and have not already been visited. The cost of reaching each child node is also computed, which can be used to guide the search.

4. Prioritization: The nodes in the beam are prioritized based on some heuristic function that estimates the distance from the current node to a goal node. The most promising nodes are expanded first, while less promising nodes are discarded.

5. Termination: The search terminates when a goal node is found or when the search space has been exhausted. If a goal is found, the path to the goal is reconstructed and returned. If no goal was found, an empty path is returned.

By following these steps, beam search is able to efficiently explore a large search space by prioritizing the expansion of the most promising nodes, while still limiting the number of nodes that are explored. This can help the search to find a solution more quickly, compared to a brute-force search algorithm that explores all nodes in the graph.

An important aspect to note is the beam size. If the beam size is too small, the search may terminate before it can reach the goal. However, if it is too large, the search becomes more computationally intensive. For this implementation, most large beam sizes are fine for the default size grid, and won't impact performance, in general.

## Bellman-Ford's pathfinding algorithm:

The Bellman-Ford's pathfinding algorithm works by initially setting the distance from the source node to all other nodes in the graph to infinity, and the predecessor for all nodes to null. It then repeatedly relaxes the edges in the graph, updating the distance and predecessor values for each node. This is repeated for each node in the graph, until all distances and predecessors have been correctly updated.

Here's a high-level overview of the algorithm:

1. Set the distance from the source node to all other nodes in the graph to infinity, and the predecessor for all nodes to null.
2. For each node in the graph, do the following:
   - Relax the edges leaving the current node.
   - Update the distance and predecessor values for each neighbor of the current node if a shorter path is found.
3. Repeat step 2 for each node in the graph, until all distances and predecessors have been correctly updated.

Once the algorithm has completed, the distance and predecessor values for each node in the graph will contain the correct shortest path information. These values can then be used to reconstruct the shortest path from the source node to any other node in the graph.

In this implementation of Bellman-Ford's algorithm, there is no check for negative edge weights/cycles. This is due to the nature of this implementation, where each weight between two nodes is always 1, and never negative. So, in this environment, the strengths of this algorithm aren't effectively displayed.

## Best-First Search pathfinding algorithm:

Best first search is a type of search algorithm that uses a heuristic evaluation function to prioritize the nodes in the search space. The algorithm starts at the starting node and explores the neighbor nodes in order of their estimated cost to the goal. The estimated cost of a node is calculated using a heuristic function, which provides an estimate of the minimum cost from the current node to the goal. This allows the algorithm to focus on the most promising nodes first, and avoid exploring parts of the search space that are unlikely to lead to the goal.

The algorithm continues to explore the neighbor nodes and expand the search space until the goal is reached, or until all possible paths have been explored. If the goal is found, the algorithm returns the minimum cost path from the start to the goal. If no path is found, the algorithm returns failure.

Best first search can be implemented using a priority queue to store the nodes that need to be explored. The priority queue is ordered by the estimated cost of each node, with the node that has the lowest estimated cost being at the top of the queue. The algorithm then repeatedly takes the top node from the queue, expands it to explore its neighbor nodes, and adds the neighbor nodes to the queue. This process continues until the goal is reached or the queue is empty.

## Bidirectional Search Algorithms:

I plan on implementing a section for bidirectional algorithms in the future (i.e., all algorithms can be run bidirectionally).

Birdirectional search can greatly improve the performance of the algorithm, however, generally it requires additional memory (close to double the memory without any optimization), which can actually slow the algorithm down. At the time of writing this, I just implemented the A* algorithm for bidirectional algorithms. When testing, the original A* algorithm was 2.83x faster then the bidirectional version (2.5112e-3 vs 7.0988e-3), and it only performed 4 extra node checks (302 vs 298 with a total node count of 1170). I haven't tried testing both algorithms with a significantly large grid, however, from this initial test, it appears that bidirectional search is slower in searching for a target and then reporting the path than the standard version.

The only other bidirectional algorithm implemented as of writing this is the Breadth-First Search (BFS) algorithm. Compared to the A* version, the BFS version was faster when compared to the original BFS algorithm, where the original was 1.24x faster than the bidirectional version (1.0871e-3 vs 1.3469e-3). However, the node checks were significantly different where there was a difference of 146 node checks between the two versions (566 vs 420 with a total node count of 1170). 

So, it seems like either a diffence in optimization or simply due to the nature of the algorithms and memory requirements.

Another thing to note about bidirectional algorithms in the context of this project is that the main body of the algorithm can't be run on seperate threads due to the nature of how the visualization is rendered. When it's threaded it causes a jittery effect because each thread is trying to rerender the window, which causes visual issues. This is the main reason why the bidirectional algorithm isn't split into separate threads for start and end.

## Bidirectional Search pathfinding algorithm:

Bidirectional search is an algorithm that allows you to find the shortest path between two nodes in a graph by simultaneously searching from both the starting node and the ending node. It is a variant of the breadth-first search algorithm that can significantly reduce the time complexity of the search in some cases.

Here's how it works:

1. Initialize two queues, one for each direction of the search (i.e., from the starting node and from the ending node).
2. Enqueue the starting node and the ending node into their respective queues.
3. While both queues are not empty:
   1. Dequeue a node from each queue and process it.
   2. For each neighbor of the node that was just dequeued from the starting node queue, check if it has already been visited from the other direction. If it has, then a path has been found and the search can be stopped. If it has not, then add it to the starting node queue.
   3. For each neighbor of the node that was just dequeued from the ending node queue, check if it has already been visited from the other direction. If it has, then a path has been found and the search can be stopped. If it has not, then add it to the ending node queue.
4. If a path was found, then reconstruct it from the visited nodes.

One of the key benefits of bidirectional search is that it can significantly reduce the time complexity of the search, especially in cases where the two nodes are relatively close to each other. In such cases, the search will typically find a path much faster than a traditional breadth-first search, since it is searching from both ends of the path at the same time. However, it is important to note that bidirectional search can be more complex to implement and may require more memory than a traditional breadth-first search.

## Branch & Bound pathfinding algorithm:

The idea behind Branch and Bound is to divide the problem into smaller sub-problems and solve them independently, keeping track of the best solution found so far, and then use this information to prune the search space.

Here's a general description of the Branch and Bound algorithm for the shortest path problem:

1. Initialize the best path found so far as infinity.

2. Create a priority queue (or a heap) of subproblems to explore, starting with the initial subproblem.

3. While the priority queue is not empty:

   a. Get the subproblem with the highest priority (i.e., the smallest lower bound).

   b. If the lower bound of the subproblem is greater than the best path found so far, prune the subproblem and move on to the next one.

   c. Otherwise, solve the subproblem and update the best path found so far if a better path is found.

   d. Create new subproblems by branching on a variable (i.e., selecting a new edge to add to the current path) and add them to the priority queue.

4. Return the best path found.

The lower bound of a subproblem is the length of the shortest path from the current node to the destination node that passes through any of the unexplored nodes. This lower bound is used to prune the search space by eliminating subproblems that cannot possibly yield a better solution than the best path found so far.

Branching is done by selecting an unexplored node and creating two new subproblems, one in which the node is added to the path and one in which it is not. The priority of each subproblem is determined by its lower bound.

By using a combination of pruning and branching, the Branch and Bound algorithm can efficiently search the space of all possible paths and find the shortest path.

## Breadth First Search (BFS) pathfinding algorithm:

BFS works by starting at a given vertex and exploring all of its neighbors before moving on to any of their neighbors. This means that the algorithm will visit all of the vertices in a given layer of the graph before moving on to the next layer. This continues until all vertices in the graph have been visited or the desired vertex has been found.

To implement BFS, a queue is typically used to store the vertices that are yet to be visited. We start by adding the starting vertex to the queue, and then we repeatedly take the next vertex from the queue, visit it, and add all of its unvisited neighbors to the queue. This process continues until the queue is empty, at which point all vertices in the graph have been visited.

## B\* pathfinding algorithm:

The B\* algorithm is a modified version of the A\* algorithm. The major difference between is in the heuristic used in the B\* algorithm.

The B\* algorithm uses a modified version of the Manhattan distance formula, where there is a blocking penalty. The blocking penalty is determined by the number of neighbors around the current node in all walkable directions (i.e., not including directions that have obstacles) that have already been checked/visited. In this case, the blocking penalty is the count of checked neighbors and is directly added to the final value in the distance formula. There are other ways to implement the blocking penalty, such as weighting the penalty to either increase or decrease the impact it has on the algorithm's results.

I don't believe this bears resemblance to the B\* algorithm designed to traverse B\*-trees, however, I'm still going to call this B\* (Blocking A\*) for the sake of confusion.

## Depth First Search (DFS) pathfinding algorithm:

DFS works by starting at a given vertex and exploring as far as possible along each branch before backtracking. This means that the algorithm will visit all of the vertices in a given branch of the graph before moving on to the next branch. This continues until all vertices in the graph have been visited or the desired vertex has been found.

To implement DFS, a stack is typically used to store the vertices that are yet to be visited. We start by adding the starting vertex to the stack, and then we repeatedly take the next vertex from the stack, visit it, and add all of its unvisited neighbors to the stack. This process continues until the stack is empty, at which point all vertices in the graph have been visited.

## Dijkstra's pathfinding algorithm:

Dijkstra's pathfinding algorithm is a type of best-first search algorithm that uses a priority queue to store the vertices that are yet to be visited. The algorithm works by starting at the starting vertex and exploring all of its neighbors, updating the cost of each path based on the actual cost of the path and the current estimated cost of the path. As the algorithm continues to explore paths, it updates the estimated cost of each path and selects the path with the lowest estimated cost. This allows the algorithm to continually refine its search and find the shortest path to the end point.

To implement Dijkstra's algorithm, we first initialize a priority queue and add the starting vertex to it. We then repeatedly take the next vertex from the priority queue, visit it, and add all of its unvisited neighbors to the priority queue. When adding a vertex to the priority queue, we update the estimated cost of the path to that vertex based on the actual cost of the path and the current estimated cost of the path. This process continues until the end vertex is reached or all vertices in the graph have been visited.

## Fast Marching Method:

The fast marching method (FMM) is a numerical method created by James Sethian for solving boundary value problems of the Eikonal equation. In the context of this simulation, the Eikonal equation resolves to 1 for every node in the grid. So, the traversal of the grid will be almost identical to other graph travesal algorithms like Dijkstra's, and the explanation for Dijkstra's above is sufficient to figure out how the FMM works in the context of this simulation.

Typically, the FMM is used in distance mapping, heat mapping, and other problems that can utilize the Eikonal equation. In this application, however, the benefits of the FMM are minimized due to the constraints of the simulation. In a uniform cost grid, there is no change in the way the "wave front" propogates through the grid. Essentially, you can think of a drop of water entering a bigger body of water. If there are no obstructions, when the water drop enters the water, the ripple in the water will have an indistinguishable shape to any random water drop entering that body of water, given identical water drop conditions. This simulation can be thought of as the body of water without obstructions, so the "ripple" will propogate the same way every time.

## Flood Fill algorithm:

The goal of the flood fill algorithm is to explore all reachable areas of a grid starting from a given initial position. It works by iteratively expanding from the initial position and visiting neighboring cells until all reachable cells have been explored, or until the stopping condition is met.

Here is a step-by-step explanation of the flood fill algorithm:

1. Create a distances data structure to hold the distance associated with a position in the grid (a dictionary is used here).

2. Create a priority queue to iterate through the grid in lowest distance first order.

3. Start at the initial position (also known as the seed position) in the grid. In the case of the implementation here, that is the grid end node.

4. Get current cell to be explored and mark it as visited.

5. Check the neighboring cells of the current position. For each neighboring cell, check if it is unvisited.

6. If a neighboring cell is unvisited, update its distance value and add it to the queue.

7. Repeat steps 4-6 until all reachable cells have been visited.

The exploration method used is the same as for BFS. The Flood Fill algorithm can be implemented using basically any graph traversal method, however, efficiency can be affected as a result.

## Floyd-Warshall's algorithm

The Floyd-Warshall algorithm is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights (but with no negative cycles). It works by dynamically constructing a shortest-paths tree for a weighted, directed graph.

The algorithm maintains a matrix `dist` of shortest distances between every pair of vertices. Initially, this matrix is filled with the weights of the edges between each pair of vertices, with a value of infinity for pairs of vertices that are not directly connected by an edge. The algorithm then iteratively relaxes the distances between all pairs of vertices by using the following formula:

`dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

where `i`, `j`, and `k` are indices representing vertices in the graph.

This formula essentially says that the distance between vertex `i` and vertex `j` can be improved by going through an intermediate vertex `k`. The algorithm repeatedly applies this formula until it reaches a fixed point, at which point the matrix `dist` will contain the shortest distances between all pairs of vertices.

The Floyd-Warshall algorithm has a time complexity of O(|V|<sup>3</sup>). It is important to note that this algorithm is not suitable for graphs with negative cycles, as the distances between pairs of vertices can become arbitrarily large in this case.

In the case of the grid implementation here, due to weights being equal and positive between every connection, the algorithm doesn't display its strengths. So, the negative case is irrelevant for this demonstration.

## Greedy Best-First Search (GBFS) pathfinding algorithm:

The greedy best-first search (GBFS) algorithm is a type of best-first search algorithm that uses a heuristic function to prioritize the exploration of paths that are likely to lead to the end point. It works by starting at the start point and exploring possible paths in a way that prioritizes paths with the lowest estimated cost. This means that the algorithm will always choose the path with the lowest estimated cost, regardless of whether that path actually leads to the end point.

To implement GBFS, we first initialize a priority queue and add the starting vertex to it. We then repeatedly take the next vertex from the priority queue, visit it, and add all of its unvisited neighbors to the priority queue. When adding a vertex to the priority queue, we update the estimated cost of the path to that vertex based on the heuristic function. This process continues until the end vertex is reached or all vertices in the graph have been visited.

## Greedy Best-Line Search (GBLS) pathfinding algorithm:

The greedy best-line search (GBLS) is a modified version of the greedy best-first search algorithm that prioritizes the exploration of neighbors in the direction of the last chosen neighbor, as long as the estimated distance to the goal is shorter than the current node.

The algorithm works by starting at the starting node and exploring all of its neighbors. For each neighbor, it calculates an estimated distance to the goal node based on a heuristic function. If the neighbor is the goal node, the search stops and the path is reconstructed. If the neighbor is not the goal, the algorithm continues to explore the neighbors of the chosen neighbor in the same direction as long as the estimated distance is shorter than the current node. If the estimated distance becomes longer, or if there are no more neighbors in that direction, the algorithm will explore other neighbors as well.

This modified version of the algorithm may be useful in certain cases where there is a clear path in a particular direction that is likely to lead to the goal, and where other factors (such as obstacles or constraints) are not as important. However, it is important to note that this modified version of the algorithm may not always find the shortest path to the goal, because it is still a greedy algorithm that does not consider other factors that may affect the overall length of the path.

## Iterative Deepening DFS pathfinding algorithm:

Iterative Deepening Depth-First Search (IDDFS) is an extension of the Depth-First Search (DFS) algorithm that is designed to find the optimal path between a start node and a goal node in a graph.

Like DFS, IDDFS works by starting at the start node and exploring as far as possible along each branch before backtracking. However, unlike DFS, which continues to explore until it reaches the goal node or exhausts all possibilities, IDDFS imposes a depth limit on the search and increases the depth limit iteratively.

At each iteration of the algorithm, the depth limit is increased by one, and the search is restarted from the start node. This process is repeated until the goal node is found or the depth limit becomes greater than the maximum depth of the graph.

IDDFS has a time complexity of O(b<sup>d</sup>), where b is the branching factor (the average number of children per node) and d is the depth of the goal node. IDDFS is not guaranteed to find the optimal path between the start and goal nodes, but it can be used as a baseline for comparison with other pathfinding algorithms.

## Iterative Deepening A\* pathfinding algorithm:

Iterative Deepening A\* (IDA\*) is an extension of the A\* algorithm that is designed to find the optimal path between a start node and a goal node in a graph. Like the A\* algorithm, IDA\* uses a combination of a heuristic function and a cost function to guide the search towards the goal node.

The IDA\* algorithm works by iteratively increasing a depth limit on the search and starting the search from the start node each time the depth limit is increased. At each iteration of the algorithm, the search is conducted using the A\* algorithm, with the depth limit serving as a threshold on the cost of the path.

If the cost of the path exceeds the depth limit at any point during the search, the search is terminated and the depth limit is increased. This process is repeated until the goal node is found or the depth limit becomes greater than the maximum possible cost of a path between the start and goal nodes.

IDA\* has a time complexity of O(b<sup>d</sup>), where b is the branching factor (the average number of children per node) and d is the depth of the goal node. IDA\* is guaranteed to find the optimal path between the start and goal nodes if the heuristic function is admissible (it never overestimates the cost to reach the goal node) and the cost of the edges is non-negative.

## Jump Point Search (JPS) pathfinding algorithm:

Jump Point Search involves identifying certain nodes called jump points which can help to prune the search space and reduce the time complexity of the algorithm. To find jump points, the algorithm needs to recursively search along certain directions to identify nodes that provide a direct path to the goal. When a jump point is identified, the algorithm can skip over all other nodes along that direction and jump directly to the next jump point, which reduces the number of nodes that need to be explored.

1. Start by initializing the open set with the start node and setting its g-value to zero.
2. While the open set is not empty, select the node with the lowest f-value and remove it from the open set.
3. For each neighbor of the current node, calculate its g-value as the sum of the current node's g-value and the cost of moving from the current node to the neighbor. If the neighbor is not yet in the open set, add it and calculate its f-value. If the neighbor is already in the open set, update its g-value and f-value if the new path to the neighbor is shorter.
4. If the neighbor is the goal node, return the path that led to it.
5. Identify jump points in each of the eight possible directions from the current node and recursively search along those directions until a jump point is found.
6. If a jump point is found, add it to the open set and calculate its g-value and f-value. If the jump point is the goal node, return the path that led to it.
7. Repeat steps 2-6 until the goal node is found or the open set is empty.

## Lexicographic BFS pathfinding algorithm:

The Lexicographic Breadth-First Search (LexBFS) algorithm is a variant of the standard breadth-first search (BFS) algorithm that orders the vertices in the graph in a specific way. Given an undirected graph and a starting vertex, LexBFS generates a list of the vertices of the graph in lexicographic order, starting from the starting vertex.

The main advantage of using LexBFS for the shortest path problem is that it guarantees that the distances of the vertices are non-decreasing as the algorithm progresses. This is important because it allows us to use the distances of the vertices to make sure that we are always considering the shortest path to each vertex.

To solve the shortest path problem using LexBFS, we can follow the following steps:

1. Run LexBFS on the graph to get the order of the vertices.
2. Initialize a dictionary to store the distances of the vertices from the starting vertex. Set the distance of the starting vertex to 0, and the distances of all other vertices to infinity.
3. Iterate through the vertices in the order produced by LexBFS. For each vertex, update the distances of its neighbors using the distance of the vertex itself. This ensures that the distances of the vertices are non-decreasing as we go through the vertices in the order produced by LexBFS.
4. When we reach the ending vertex, the distance of the ending vertex is the shortest path distance from the starting vertex to the ending vertex. We can then use the parent pointers produced by LexBFS to reconstruct the shortest path from the starting vertex to the ending vertex.

## Lifelong Planning A\* pathfinding algorithm:

The Lifelong Planning A\* (LPA\*) algorithm is a variant of the well-known A\* search algorithm that is designed to efficiently update the optimal path in a graph as changes are made to the graph over time. LPA\* is a popular algorithm for planning and pathfinding in dynamic environments, where the underlying graph can change frequently.

In contrast to A\*, which assumes a fixed graph and recomputes the optimal path from scratch whenever changes occur, LPA\* keeps track of the current best path from the start node to each node in the graph, and updates these paths as necessary when the graph changes. LPA\* maintains two values for each node: the "g-value", which is the cost of the best path found so far from the start node to that node, and the "rhs-value", which is the cost of the second-best path. These values are used to determine which nodes to expand during the search.

LPA\* uses a heuristic function to estimate the cost of the remaining path to the goal from each node, and expands nodes with the lowest "key-value", which is a combination of the g-value and the heuristic estimate. When the graph changes, LPA\* updates the g- and rhs-values of the affected nodes, and re-expands nodes whose key-values have changed.

Despite the ability to handle dynamic environments, the algorithm implemented here is in a static environment, so performance and graph traversal will be almost identical to the A\* algorithm.

## Random Walk pathfinding algorithm:

The random walk algorithm is a type of pathfinding algorithm that uses a random exploration strategy to find a path between two points. It works by starting at the start point and randomly selecting one of the available neighbors to explore. This process is repeated until the end point is reached or all possible paths have been explored.

## Theta\* pathfinding algorithm:

Like A*, Theta* uses a combination of a heuristic function and the cost of each path to determine the most efficient path to take. However, unlike A*, Theta* uses a more advanced search strategy that allows it to find the shortest path to the end point more efficiently.

To implement Theta\*, we first initialize a priority queue and add the starting vertex to it. We then repeatedly take the next vertex from the priority queue, visit it, and add all of its unvisited neighbors to the priority queue. When adding a vertex to the priority queue, we update the estimated cost of the path to that vertex based on the actual cost of the path and the current estimated cost of the path. Additionally, we use a special search strategy that allows us to prune the search space and avoid exploring paths that are unlikely to lead to the end point. This process continues until the end vertex is reached or all vertices in the graph have been visited.
