## Assignment 4: Heuristic Search

#### Part 1
- Generate a random weighted connected graph with 10 million cities with designated start and goal cities. 
- Implement Best First Search, Hill Climbing and A* search for searching the goal city in the graph if a path from start city to goal city exists. 
- Execute the experiment 10 times for different random graph initialization. 
- Also, plot the searching time and required memory to compare the above algorithms.
- Your code should be able to visualize the search path during the search.

Note: 
- You may generate a map with 10 million random cities. 
- Absolute or Euclidean distances can be used as heuristics. 
- In the weighted graph case, you may use random distances as heuristics. 
- You can compute optimal heuristics using Dijkstra approach. 
- You may also add gaussian noise in the optimal distances to create a heuristic.

#### Part 2
- Implement a modified search strategy which uses hill climbing in alternate steps and beam search with beam width 3 for the remaining steps for the above generated graph and compare with standard hill climbing and beam search. 
- Your code should be able to visualize the search path during the search.

#### Deadline
Submit the assignment with codes and reports by **Nov 12, 2018**.