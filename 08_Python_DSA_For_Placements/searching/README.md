# Data Structures & Algorithms: Searching (Module 08)

Searching algorithms look for the presence of a target value within a collection. The two fundamental strategies are linear scanning and logarithmic divide-and-conquer partitions.

---

## Searching Algorithms Comparison

| Algorithm | Precondition | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | None | $O(1)$ *(if target is at start)* | $O(N)$ | $O(1)$ |
| **Binary Search** | Array must be **Sorted** | $O(1)$ *(if target is at middle)* | $O(\log N)$ | $O(1)$ |

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/searching/solutions.py), we implement the following three classic searching problems:

1. **Linear Search**:
   * Sequentially scans the array to locate the target element.
2. **Binary Search (Iterative)**:
   * Perform binary division bounds check to find target in a sorted list.
3. **Search in a Rotated Sorted Array**:
   * Find a target element inside an array that has been rotated at an unknown pivot index beforehand in $O(\log N)$ time.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
