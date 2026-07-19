# Data Structures & Algorithms: Recursion & Backtracking (Module 08)

Recursion solves problems by breaking them down into smaller sub-problems of the same type. Backtracking is an algorithmic technique that uses recursion to search for solutions incrementally. It builds a state and, if a constraint is violated, "backtracks" (reverts the last state change) to try alternative paths.

---

## Recursion vs Backtracking Comparison

* **Recursion**:
  * Function calls itself to solve sub-problems.
  * Must define a **Base Case** (termination constraint) and **Recursive Step** (state progression).
  * E.g. Calculating factorials, traversing binary trees.
* **Backtracking**:
  * Systematic search of state spaces (state tree traversal).
  * Explores branches recursively. If a branch fails constraint validation, it prunes the search space by reverting changes (popping variables) and backtracking.
  * E.g. Finding all subsets, solving Sudoku, N-Queens placement.

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/recursion_backtracking/solutions.py), we implement the following three key problems:

1. **Generate Parentheses**:
   * Generate all combinations of $N$ pairs of valid brackets using open/close bracket constraints.
2. **Permutations**:
   * Output all possible arrangements of a list of distinct integers.
3. **N-Queens**:
   * Position $N$ queens on an $N \times N$ chessboard such that no two queens attack each other.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
