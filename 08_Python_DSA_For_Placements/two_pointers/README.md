# Data Structures & Algorithms: Two Pointers (Module 08)

The two-pointer technique uses two pointer markers to scan a linear data structure (an array, list, or string) concurrently. This approach typically optimizes space complexity to $O(1)$ and reduces search times from $O(N^2)$ to $O(N)$.

---

## Two Pointer Approaches

1. **Opposite Ends (Left and Right)**:
   * Pointers start at indices $0$ and $N-1$, moving inward.
   * *Typical Use-Cases*: Checking palindromes, container boundaries search, target sum search.
2. **Fast & Slow Runners**:
   * Pointers start at the same side but move at different velocities.
   * *Typical Use-Cases*: Removing duplicates, finding middle of linked lists, cycle detection.

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/two_pointers/solutions.py), we implement the following three classic two-pointer problems:

1. **Valid Palindrome**:
   * Verify if a string reads identically forwards/backwards, ignoring non-alphanumeric text in $O(N)$ time.
2. **Container With Most Water**:
   * Find two boundary lines in an array that trap the maximum area volume.
3. **Remove Duplicates from Sorted Array**:
   * Remove duplicate values in-place from a sorted array.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
