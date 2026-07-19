# Data Structures & Algorithms: Queues (Module 08)

A Queue is a linear data structure that follows the **First In First Out (FIFO)** protocol.
Operations are performed at opposite ends: insertion (enqueue) at the tail, and removal (dequeue) at the head. A Deque (Double Ended Queue) allows $O(1)$ operations at both ends.

---

## Queue Operations Complexities

| Operation | Time Complexity | Space Complexity | Reason |
| :--- | :--- | :--- | :--- |
| **Enqueue** (Insert at Tail) | $O(1)$ | $O(1)$ | Adds to the end of the line. |
| **Dequeue** (Remove from Head) | $O(1)$ | $O(1)$ | Removes from front (uses `collections.deque` for $O(1)$ removals). |
| **Peek / Front** (View Head) | $O(1)$ | $O(1)$ | Accesses index 0 elements. |

*Note: In Python, using standard lists for queues (`list.pop(0)`) is inefficient, taking $O(N)$ time because all subsequent elements must be shifted in memory. Always use `collections.deque` which is implemented as a doubly-linked list providing true $O(1)$ operations.*

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/queues/solutions.py), we implement the following three classic queue problems:

1. **Implement Queue using Stacks**:
   * Build a FIFO queue class using two LIFO stacks.
2. **First Unique Character in a String**:
   * Scans string and returns the first character appearing exactly once using a queue tracker.
3. **Sliding Window Maximum**:
   * Find the maximum values for each window position of size $K$ using a **Monotonic Deque**.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
