"""
Topic:
Sorting Algorithms

Importance:
Sorting organizes lists sequentially, which is a mandatory optimization precursor
for searching and partitioning. Knowing how to write and analyze Bubble, Merge,
and Quick sort builds deep algorithmic complexity intuition.

This file covers:
- Problem 1: Bubble Sort (Optimized)
- Problem 2: Merge Sort (Stable, Divide & Conquer)
- Problem 3: Quick Sort (In-Place, Partition-Based)
"""

# =====================================================================
# PROBLEM 1: Bubble Sort (Optimized)
# =====================================================================
# Problem Statement:
# Sort an array of integers in ascending order using the Bubble Sort algorithm.
#
# Approach:
# We pass through the array multiple times. In each pass, we compare adjacent elements
# and swap them if they are in the wrong order.
# Optimization:
# Maintain a boolean flag 'swapped'. If a pass completes without making any swaps,
# the array is already sorted, and we can terminate early.
#
# Time Complexity:
# - Best Case: O(N) (array is already sorted)
# - Average/Worst Case: O(N^2) (nested loop sweeps)
# Space Complexity: O(1) - in-place swapping
#
# Common Interview Variations:
# 1. Selection Sort (finds minimum element in each pass and swaps with boundary).
# 2. Insertion Sort (places element in its correct position relative to sorted prefix).

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no elements were swapped in inner loop, array is sorted
        if not swapped:
            break


# =====================================================================
# PROBLEM 2: Merge Sort
# =====================================================================
# Problem Statement:
# Sort an array of integers in ascending order using the Merge Sort algorithm.
#
# Approach:
# Divide and Conquer:
# 1. If list length <= 1, return it.
# 2. Split array into left and right halves: mid = len(arr) // 2.
# 3. Recursively call merge_sort on left and right halves.
# 4. Merge the two sorted halves back together in sorted order.
#
# Time Complexity: O(N log N) - for all cases (best, average, worst)
# Space Complexity: O(N) - auxiliary memory used for merging halves
#
# Common Interview Variations:
# 1. Merge two sorted arrays.
# 2. Count Inversions in an array (solved by modifying the merge step).

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    # Recursively sort left and right partitions
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge sorted partitions
    return merge_sorted_helper(left_half, right_half)

def merge_sorted_helper(left, right):
    merged = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= maintains stable sort
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    # Append remaining
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# =====================================================================
# PROBLEM 3: Quick Sort
# =====================================================================
# Problem Statement:
# Sort an array of integers in ascending order using the Quick Sort algorithm.
#
# Approach:
# Partition-Based Divide & Conquer:
# 1. Pick a pivot element (e.g. the last element of the partition).
# 2. Rearrange the array: place all elements smaller than pivot to the left,
#    and all elements larger than pivot to the right.
# 3. Recursively apply Quick Sort to the left and right sub-arrays.
#
# Time Complexity:
# - Average Case: O(N log N)
# - Worst Case: O(N^2) (occurs if array is already sorted and we pick extreme elements as pivot)
# Space Complexity: O(log N) - recursion stack memory
#
# Common Interview Variations:
# 1. K-th Largest Element (Quick Select algorithm, average time O(N)).
# 2. Sort colors (Dutch National Flag partition, O(N) time, O(1) space).

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Swap pivot into its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_recursive(arr, low, high):
    if low < high:
        # Partition index
        p_idx = partition(arr, low, high)
        
        # Sort left and right partitions
        quick_sort_recursive(arr, low, p_idx - 1)
        quick_sort_recursive(arr, p_idx + 1, high)

def quick_sort(arr):
    quick_sort_recursive(arr, 0, len(arr) - 1)


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Bubble Sort
    list_1 = [64, 34, 25, 12, 22, 11, 90]
    print("=======================================")
    print("Problem 1: Bubble Sort (Optimized)")
    print(f"Input before: {list_1}")
    bubble_sort(list_1)
    print(f"Output after: {list_1}")
    
    # Test Problem 2: Merge Sort
    list_2 = [38, 27, 43, 3, 9, 82, 10]
    print("\n=======================================")
    print("Problem 2: Merge Sort (Stable)")
    print(f"Input before: {list_2}")
    sorted_res = merge_sort(list_2)
    print(f"Output after: {sorted_res}")
    
    # Test Problem 3: Quick Sort
    list_3 = [10, 7, 8, 9, 1, 5]
    print("\n=======================================")
    print("Problem 3: Quick Sort (In-Place)")
    print(f"Input before: {list_3}")
    quick_sort(list_3)
    print(f"Output after: {list_3}")
    print("=======================================")

"""
Key Takeaways:
- Bubble sort is simple but inefficient O(N^2) for large lists. The swap flag optimizes sorted inputs to O(N).
- Merge sort guarantees O(N log N) runtime but requires auxiliary memory O(N) to merge partitions.
- Quick sort is fast in practice and works in-place, but its pivot selection strategy must be robust to avoid O(N^2) worst case.

Interview Relevance:
- Know the difference between stable and unstable sorting.
- Be prepared to discuss recursion stack space and partition steps in-place.

AI/ML Relevance:
- KNN classification: Slicing the nearest K neighbors from a distance matrix uses sorting indexes.
- Non-Maximum Suppression (NMS): Object detection pipelines (like YOLO) sort box prediction confidence scores to remove overlapping duplicate boxes.
"""
