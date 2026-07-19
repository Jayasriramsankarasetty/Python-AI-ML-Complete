# Data Structures & Algorithms: Stacks (Module 08)

A Stack is a linear data structure that follows the **Last In First Out (LIFO)** protocol.
Operations are performed at one end (the top of the stack). Stacks are the core structures behind recursion, backtracking states, and parsing nested layouts.

---

## Stack Operations Complexities

| Operation | Time Complexity | Space Complexity | Reason |
| :--- | :--- | :--- | :--- |
| **Push** (Insert at Top) | $O(1)$ | $O(1)$ | Adds to the end of the dynamic list (amortized constant). |
| **Pop** (Delete from Top) | $O(1)$ | $O(1)$ | Removes from the end. |
| **Peek / Top** (View Top) | $O(1)$ | $O(1)$ | Accesses last element. |
| **IsEmpty** (Check Status) | $O(1)$ | $O(1)$ | Checks list length. |

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/stacks/solutions.py), we implement the following three classic stack problems:

1. **Valid Parentheses**:
   * Verify if braces are matched and closed in correct order using a LIFO tracking stack.
2. **Min Stack Design**:
   * Implement a stack class that retrieves the minimum element in constant $O(1)$ time.
3. **Next Greater Element I**:
   * Find the next greater element to the right of each array element in $O(N)$ time using a **Monotonic Stack**.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
