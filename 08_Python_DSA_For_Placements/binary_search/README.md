# Data Structures & Algorithms: Binary Search (Module 08)

Binary search is an $O(\log N)$ search optimization that operates by repeatedly dividing the search interval in half. Beyond searching indices of sorted lists, the binary search framework can be applied to find optimal solutions across a range of possible answers (Binary Search on Answer).

---

## Binary Search Paradigms

1. **Standard Index Search**:
   * Locating an exact value or boundary limit (lower/upper bound) in a pre-sorted array.
2. **Binary Search on Slopes**:
   * Navigating peaks/troughs on unsorted arrays by comparing adjacent gradients (mid vs mid+1).
3. **Binary Search on Answer Range**:
   * Searching for the minimum or maximum parameter value that satisfies a constraint (e.g. eating speed, shipping capacity), where the bounds are defined by `[min_possible_ans, max_possible_ans]`.

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/binary_search/solutions.py), we implement the following three advanced binary search problems:

1. **First and Last Position of Element in Sorted Array**:
   * Locate the start and end indices of duplicate target values in $O(\log N)$ time.
2. **Find Peak Element**:
   * Return the index of any local maximum in an unsorted array in $O(\log N)$ time.
3. **Koko Eating Bananas** (Binary Search on Answer):
   * Determine the minimum eating speed `K` required to consume all piles of bananas within `H` hours.

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
