"""
Topic:
Graph Representation and Traversals (BFS & DFS)

Importance:
Graphs model complex relationships. Traversals like BFS and DFS are foundational
for pathfinding, cycle checks, dependencies resolutions, and parsing model layers.

This file covers:
- Graph implementation using Adjacency List
- Problem 1: Graph Representation & Insertion
- Problem 2: Breadth-First Search (BFS) Traversal
- Problem 3: Depth-First Search (DFS) Traversal
"""

from collections import deque

# =====================================================================
# PROBLEM 1: Graph Representation (Adjacency List)
# =====================================================================
# Problem Statement:
# Implement a Graph class representing an undirected graph using an Adjacency List.
# The class should support:
# - add_vertex(u): Adds a vertex u.
# - add_edge(u, v): Adds an undirected edge between u and v.
#
# Approach:
# We use a dictionary where keys are vertices and values are lists storing adjacent neighbor vertices.
# Since it is undirected, `add_edge(u, v)` adds v to u's list, and u to v's list.
#
# Time Complexity:
# - add_vertex: O(1)
# - add_edge: O(1)
# Space Complexity: O(V + E) - where V is vertices count, and E is edges count
#
# Common Interview Variations:
# 1. Directed Graph Representation (edges only go from source to destination).
# 2. Weighted Graph Representation (stores tuple of neighbor and weight: `(neighbor, weight)`).

class Graph:
    def __init__(self):
        # Dictionary representing adjacency list: vertex -> list of neighbor vertices
        self.adj_list = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            
    def add_edge(self, u, v):
        # Ensure vertices exist in graph
        self.add_vertex(u)
        self.add_vertex(v)
        
        # Add undirected links
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def __repr__(self):
        return str(self.adj_list)


# =====================================================================
# PROBLEM 2: Breadth-First Search (BFS)
# =====================================================================
# Problem Statement:
# Implement Breadth-First Search (BFS) starting from a source node in an undirected graph.
# Return a list of vertices in the order they were visited.
#
# Approach:
# Queue-Based Level Order:
# We maintain a queue of nodes to visit, and a set of visited nodes to avoid cyclic loops.
# 1. Initialize queue with source node, add source to visited set.
# 2. Loop while queue is not empty:
#    - Pop node from front of queue. Record it in visited order.
#    - For each neighbor of node:
#      - If neighbor is not visited, add to visited set, and append to queue.
#
# Time Complexity: O(V + E) - each vertex is enqueued/dequeued once, and neighbors checked
# Space Complexity: O(V) - queue and visited set store at most V elements
#
# Common Interview Variations:
# 1. Find the shortest path between source and target in an unweighted graph (track parent pointers during BFS).
# 2. BFS on a 2D grid matrix (Lee Algorithm / Knight's Tour).

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    order = []
    
    while queue:
        curr = queue.popleft()
        order.append(curr)
        
        # Visit all adjacent neighbors
        for neighbor in graph.adj_list.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return order


# =====================================================================
# PROBLEM 3: Depth-First Search (DFS)
# =====================================================================
# Problem Statement:
# Implement Depth-First Search (DFS) starting from a source node in an undirected graph.
# Return a list of vertices in the order they were visited.
#
# Approach:
# Recursive DFS:
# Maintain a recursive helper `dfs_recursive(vertex, visited, order)`:
# - Add vertex to visited set, record in visited order.
# - For each neighbor of vertex:
#   - If neighbor is not visited, recursively call `dfs_recursive(neighbor)`.
#
# Time Complexity: O(V + E) - visits each vertex and edge once
# Space Complexity: O(V) - recursion stack memory stores active vertices
#
# Common Interview Variations:
# 1. Cycle Detection in Directed/Undirected graph.
# 2. Topological Sort (find dependencies resolution order in DAGs).
# 3. Find Connected Components count.

def dfs(graph, start_vertex):
    visited = set()
    order = []
    
    def dfs_recursive(vertex):
        visited.add(vertex)
        order.append(vertex)
        
        for neighbor in graph.adj_list.get(vertex, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
                
    dfs_recursive(start_vertex)
    return order


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Graph Representation
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    print("=======================================")
    print("Problem 1: Graph Representation (Adjacency List)")
    print(f"Graph representation:\n  {g}")
    
    # Test Problem 2: BFS Traversal
    print("\n=======================================")
    print("Problem 2: Breadth-First Search (BFS)")
    print(f"BFS Order starting at vertex 0: {bfs(g, 0)}")
    
    # Test Problem 3: DFS Traversal
    print("\n=======================================")
    print("Problem 3: Depth-First Search (DFS)")
    print(f"DFS Order starting at vertex 0: {dfs(g, 0)}")
    print("=======================================")

"""
Key Takeaways:
- Adjacency Lists are space-efficient O(V+E) for sparse graphs compared to Adjacency Matrices O(V^2).
- BFS uses a Queue (FIFO) to explore nodes level-by-level, finding shortest paths in unweighted graphs.
- DFS uses Recursion (LIFO) to explore branches as deep as possible, which is useful for connectivity and topological sorting.
- Always track a 'visited' set to prevent infinite loops in cyclic graphs.

Interview Relevance:
- If a problem deals with connections, networks, grids, or dependencies, frame it as a Graph.
- Choose BFS for shortest path, and DFS for path connectivity or cycle checking.

AI/ML Relevance:
- Computational Graphs: Deep learning frameworks (like PyTorch and TensorFlow) represent models as Directed Acyclic Graphs (DAGs) of operations, using topological sorting to sequence forward passes.
- Knowledge Graphs: Entity relationships (similar to Google Search Graph) map entities to neighbor properties using adjacency lists.
"""
