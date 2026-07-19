# Data Structures & Algorithms: Trees (Module 08)

A Tree is a non-linear, hierarchical data structure consisting of nodes connected by edges. The top node is the **root**, and nodes with no children are **leaves**.
Trees are vital for expressing hierarchical dependencies (like directory structures or decision trees).

---

## Tree Traversals Overview

* **Inorder** (Left $\to$ Root $\to$ Right):
  * Traversing a Binary Search Tree (BST) inorder yields elements in **sorted ascending order**.
* **Preorder** (Root $\to$ Left $\to$ Right):
  * Useful for copying trees or prefix expression generation.
* **Postorder** (Left $\to$ Right $\to$ Root):
  * Useful for deleting trees or suffix expression generation.
* **Level Order** (BFS):
  * Traverses nodes level-by-level using a queue.

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/trees/solutions.py), we implement the following three key problems:

1. **Binary Tree Traversals (Inorder, Preorder, Postorder)**:
   * Perform depth-first tree traversals recursively.
2. **Maximum Depth of Binary Tree**:
   * Calculate height level limits using Depth First Search (DFS) recursion.
3. **Validate Binary Search Tree (BST)**:
   * Assert if a binary tree satisfies the BST property using range boundary limits.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
