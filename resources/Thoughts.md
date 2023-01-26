## Reason for writing

While programming this project, I have learned a lot about graph search and path finding algorithms, and I wanted to share some of my opinions and thoughts about them, in relation to this project.

## Process

A lot of what went in to this project was researching what algorithms there are and how to translate them into something that can be used in a grid-based graph.

I used resources like Wikipedia, and ChatGPT for a lot of the algorithms, and explainations. Most algorithm pages on Wikipedia have a pseudocode section, which is helpful when the mathematical notation doesn't quite make sense. ChatGPT, while currently looked at with suspicion by some, is a great resource for learning and as a tool for assisting in development. The only gripe I have to say about ChatGPT is that you can't be 100% certain what it spits out is correct without validating it against another source, like Wikipedia, or primary sources like the papers where the algorithms were published.

Another resource that I tried to use is YouTube. However, most of the algorithms on YouTube (pathfinding algorithms) are either A*, BFS, DFS, or Dijkstra's algorithm. I could scarely find the other algorithms I implemented here, and ones I'm going to implement, on YouTube. There were some videos that went over the concept of the algorithm, like Bellman-Ford, and Floyd-Warshall, but they didn't provide either usable psuedocode or actual code for the algorithm. This is a personal opinion of mine, but if you want to do a deep dive on pathfinding algorithms, I would suggest using other resources than YouTube. However, if you're just looking to get started or just a cursory overview of pathfinding algorithms, then YouTube is a good resource.

## Algorithm Discussion

While implementing these algorithms, I relized there is an issue with the project environment. By this I mean, not every algorithm can display its own strenths. The biggest losers of this simulation are the algorithms that are ment to be run once and the results used multiple times. For example, the Floyd-Warshall algorithm. If you look at the example test result in the `main/testing/results` folder, you will see that there are > one billion node checks. In the environment that I have set up, all data from the previous run is deleted, so the distance matrix that is created isn't reused. So, every run, on a default generated maze, the Floyd-Warshall algorithm will have to run > one billion checks. However, if data were saved from a previous run, the Floyd-Warshall algorithm would only have to do those checks once and the shortest path could be found in linear time (O(|V|)). On the other end of the spectrum, the algorithms that are most suited to this environment are ones that are ment to be run without any preprocessing, like A*, BFS, and Dijkstra. 

If I were to reimplement this, or modify this program, I would add something like a caching function to store precomputed information that would speed up algorithm runtime.

---

This program is mainly designed as a learning tool, rather than anything practical. However, most of the algorithms have practical applications. 

I think the easiest demonstration would be a GPS application. Many of the concepts in the algorithms implemented here are used for GPS applications. If we look at Theta*, we can see it gives turn points. This is congruent to what many GPS applications do where it tells you to turn at X street. 

--TBC