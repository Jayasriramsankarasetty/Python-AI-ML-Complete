# Data Structures & Algorithms: Hashing (Module 08)

Hashing maps data keys to array indices via a hash function, allowing average $O(1)$ time complexity for lookup, insert, and delete operations.
Understanding how to trade memory space for time using dictionaries (Hash Maps) and sets (Hash Sets) is a key interview strategy.

---

## Hash Map Operations Complexities

| Operation | Average Case | Worst Case | Reason |
| :--- | :--- | :--- | :--- |
| **Insertion** | $O(1)$ | $O(N)$ | $O(1)$ hash map lookup, drops to $O(N)$ on hash collision chains. |
| **Deletion** | $O(1)$ | $O(N)$ | Removes key entry after hash location calculation. |
| **Search (Lookup)** | $O(1)$ | $O(N)$ | Finds value directly matching key hash offset. |

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/hashing/solutions.py), we implement the following three classic hashing interview problems:

1. **Two Sum**:
   * Find two numbers that sum up to a target value, returning their indices in $O(N)$ time.
2. **Subarray Sum Equals K**:
   * Calculate the number of continuous subarrays that sum up to $K$ using prefix sum maps.
3. **Group Anagrams**:
   * Group list strings sharing identical characters together.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
