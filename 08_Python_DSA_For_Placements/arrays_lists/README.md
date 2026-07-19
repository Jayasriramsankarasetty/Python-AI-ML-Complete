# Data Structures & Algorithms: Arrays and Lists (Module 08)

Arrays/Lists are contiguous memory data structures that support $O(1)$ random access.
Mastering operations like sliding windows, two-pointers, and in-place updates on arrays is the foundation of cracking placement coding rounds.

---

## Operations Time Complexity Overview

| Operation | Best Case | Worst Case | Reason |
| :--- | :--- | :--- | :--- |
| **Lookup by Index** | $O(1)$ | $O(1)$ | Direct offset mathematical memory lookup. |
| **Search by Value** | $O(1)$ *(if at index 0)* | $O(N)$ | Linear search through elements. |
| **Insertion at End** | $O(1)$ *(amortized)* | $O(N)$ *(if list needs resize)* | Appending to end doesn't require index shifts. |
| **Insertion in Middle** | $O(1)$ *(at end)* | $O(N)$ | Requires shifting subsequent elements in memory. |
| **Deletion** | $O(1)$ *(at end)* | $O(N)$ | Requires shifting elements left to maintain contiguity. |

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/arrays_lists/solutions.py), we implement the following four classic problems:

1. **Second Largest Element**:
   * Single-pass scan to find the second largest value in an array without sorting.
2. **Rotate Array by $K$ Steps**:
   * Rotate array to the right by $K$ positions in-place using the reversal algorithm.
3. **Move Zeros to the End**:
   * Move all 0's to the end while preserving the relative ordering of non-zero elements.
4. **Merge Two Sorted Arrays**:
   * Combine two sorted arrays into a new consolidated sorted array in linear time.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
