# Data Structures & Algorithms: Sliding Window (Module 08)

The sliding window technique optimizes sub-sequence queries over linear collections.
Instead of recalculating overlapping sub-segments (which takes $O(N^2)$), we maintain a sliding window bound and adjust pointers in $O(N)$ time.

---

## Window Structures

1. **Fixed Size Window**:
   * The window has a constant size $K$. We initialize the sum/metric of the first window, and then slide it by adding the new element and removing the old one.
2. **Variable Size Window**:
   * The window boundary expands and contracts dynamically based on constraints (e.g. unique characters). Pointers adjust depending on value states.

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/sliding_window/solutions.py), we implement the following three classic sliding window problems:

1. **Maximum Sum Subarray of Size K** (Fixed Size):
   * Return the maximum sum value of any contiguous sub-segment of length $K$.
2. **Longest Substring Without Repeating Characters** (Variable Size):
   * Find the length of the longest substring containing entirely unique characters.
3. **Minimum Window Substring** (Variable Size - Hard):
   * Find the shortest substring of $S$ containing all characters of target $T$.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
