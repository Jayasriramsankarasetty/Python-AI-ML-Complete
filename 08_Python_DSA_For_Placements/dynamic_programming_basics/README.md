# Data Structures & Algorithms: Dynamic Programming Basics (Module 08)

Dynamic Programming (DP) is an algorithmic optimization technique that solves complex problems by breaking them down into simpler, overlapping subproblems. It saves the results of solved subproblems to avoid redundant calculations.

---

## Dynamic Programming Core Prerequisites

To solve a problem using DP, it must possess:
1. **Optimal Substructure**:
   * An optimal solution to the problem can be constructed from optimal solutions to its subproblems.
2. **Overlapping Subproblems**:
   * The recursive algorithm visits the same subproblems repeatedly, rather than generating new ones.

---

## DP Implementation Strategies

* **Top-Down (Memoization)**:
  * Solves recursively. Caches calculated subproblem outputs in a hash table or array.
* **Bottom-Up (Tabulation)**:
  * Solves iteratively. Starts from the base cases and fills up a multi-dimensional table (DP array) step-by-step.
  * Generally preferred in interviews due to lack of recursion stack memory overhead.

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/dynamic_programming_basics/solutions.py), we implement the following three classic DP problems:

1. **Climbing Stairs** (1D DP / Fibonacci):
   * Determine the number of unique combinations to climb $N$ steps using space-optimized variables.
2. **Coin Change** (1D DP Min-Tabulation):
   * Minimize the number of coins required to sum up to target `amount`.
3. **0/1 Knapsack Problem** (2D DP Tabulation):
   * Maximize item values placed inside a Knapsack of capacity $W$.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
