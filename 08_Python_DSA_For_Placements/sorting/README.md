# Data Structures & Algorithms: Sorting (Module 08)

Sorting rearranges elements of a list in a specific order (ascending or descending).
Different sorting algorithms make trade-offs between speed, auxiliary memory space, and stability.

---

## Sorting Algorithms Complexity Comparison

| Algorithm | Best Case Time | Average Case Time | Worst Case Time | Space Complexity | Stable? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(N)$ *(optimized)* | $O(N^2)$ | $O(N^2)$ | $O(1)$ | **Yes** |
| **Merge Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | **Yes** |
| **Quick Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N^2)$ | $O(\log N)$ | **No** |

*Note: A sorting algorithm is **stable** if it preserves the relative order of items with equal values.*

---

## Practiced Problems

Inside [solutions.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/08_Python_DSA_For_Placements/sorting/solutions.py), we implement the following three key sorting algorithms:

1. **Bubble Sort**:
   * Repeatedly swap adjacent elements if out of order, optimized with early stopping flags.
2. **Merge Sort**:
   * Divide array into halves recursively, sort, and merge them in stable order.
3. **Quick Sort**:
   * Partition array using pivot markers (unstable, in-place sorting).

---

## How to Run the Solutions
Execute the Python script:
```bash
python solutions.py
```
