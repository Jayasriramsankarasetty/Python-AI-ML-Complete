# Data Structures & Algorithms: Linked Lists (Module 08)

A Linked List is a linear data structure where elements are not stored in contiguous memory locations. Instead, each element (node) contains data and a pointer (reference) pointing to the next node.

---

## Linked List vs Array Complexity Overview

| Operation | Linked List (Singly) | Array (Dynamic List) | Reason |
| :--- | :--- | :--- | :--- |
| **Lookup by Index** | $O(N)$ | $O(1)$ | Linked lists must traverse sequentially from head. |
| **Insert at Beginning** | $O(1)$ | $O(N)$ | Linked lists only redirect pointers; arrays must shift elements. |
| **Insert at End** | $O(1)$ *(if tail is kept)* / $O(N)$ | $O(1)$ *(amortized)* | Reaches end to append. |
| **Deletion** | $O(1)$ *(once node is found)* | $O(N)$ | Alters pointer links instead of shifting memory bounds. |

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/linked_lists/solutions.py), we implement the following three classic linked list problems:

1. **Reverse a Singly Linked List**:
   * Reverse the link direction of a singly linked list in-place in $O(N)$ time.
2. **Linked List Cycle Detection**:
   * Determine if a linked list contains a cycle using Floyd's Tortoise and Hare algorithm.
3. **Merge Two Sorted Linked Lists**:
   * Merge two sorted linked lists by splicing pointer nodes in-place.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
