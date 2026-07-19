# Data Structures & Algorithms: Graphs Basics (Module 08)

A Graph is a non-linear data structure consisting of a finite set of vertices (or nodes) and a set of edges connecting them. Graphs are used to model networks (like social connections, routes, or dependencies).

---

## Graph Representation Comparison

| Method | Space Complexity | Add Vertex | Add Edge | Check Edge | Typical Use-Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Adjacency Matrix** | $O(V^2)$ | $O(V^2)$ | $O(1)$ | $O(1)$ | Dense graphs (many edges). |
| **Adjacency List** | $O(V + E)$ | $O(1)$ | $O(1)$ | $O(V)$ | Sparse graphs (fewer edges). |

---

## Graph Traversal Algorithms

* **Breadth-First Search (BFS)**:
  * Explores neighbors level-by-level using a **Queue**.
  * Finds the **shortest path** in unweighted graphs.
  * Time Complexity: $O(V + E)$, Space Complexity: $O(V)$.
* **Depth-First Search (DFS)**:
  * Explores as deep as possible along each branch before backtracking, using **Recursion** (call stack).
  * Used for cycle detection, topological sorting, and path connectivity.
  * Time Complexity: $O(V + E)$, Space Complexity: $O(V)$.

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/graphs_basics/solutions.py), we implement:

1. **Graph Representation (Adjacency List)**:
   * Class structure utilizing dictionary mapping lists.
2. **Breadth-First Search (BFS)**:
   * Level-order queue traversal starting from source node.
3. **Depth-First Search (DFS)**:
   * Recursive graph branch traversal starting from source node.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
