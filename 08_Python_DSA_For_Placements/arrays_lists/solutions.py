"""
Topic:
Array and List Coding Problems

Importance:
Arrays represent the fundamental datatypes for organizing collections in memory.
Solving array problems builds two-pointer logic, in-place update intuition, and index boundary handling.

This file covers:
- Problem 1: Second Largest Element
- Problem 2: Rotate Array by K Steps (in-place)
- Problem 3: Move Zeros to the End (in-place)
- Problem 4: Merge Two Sorted Arrays
"""

# =====================================================================
# PROBLEM 1: Second Largest Element in an Array
# =====================================================================
# Problem Statement:
# Given an array of integers, find and return the second largest element.
# If no second largest element exists (e.g. array size < 2 or all elements equal), return -1.
#
# Approach:
# We maintain two variables: 'largest' and 'second_largest', initially set to float('-inf').
# We scan the array:
# - If current element x is greater than 'largest', update 'second_largest' to 'largest', and 'largest' to x.
# - Else if x is greater than 'second_largest' and x is not equal to 'largest', update 'second_largest' to x.
#
# Time Complexity: O(N) - single pass scan
# Space Complexity: O(1) - constant auxiliary memory
#
# Common Interview Variations:
# 1. Find the second smallest element in an array.
# 2. Find the K-th largest/smallest element (solved using Sorting O(N log N) or Min-Heap O(N log K)).

def find_second_largest(arr):
    if len(arr) < 2:
        return -1
        
    largest = second_largest = float('-inf')
    
    for x in arr:
        if x > largest:
            second_largest = largest
            largest = x
        elif x > second_largest and x != largest:
            second_largest = x
            
    return second_largest if second_largest != float('-inf') else -1


# =====================================================================
# PROBLEM 2: Rotate Array by K Steps (Right Rotation)
# =====================================================================
# Problem Statement:
# Given an array, rotate it to the right by K steps, where K is non-negative.
# The modification should be done in-place (O(1) auxiliary space).
#
# Approach:
# Reversal Algorithm:
# 1. Normalize K: K = K % N (since rotating N times returns the original array).
# 2. Reverse the entire array.
# 3. Reverse the first K elements.
# 4. Reverse the remaining N-K elements.
#
# Time Complexity: O(N) - reversing elements visits each index constant times
# Space Complexity: O(1) - in-place swapping
#
# Common Interview Variations:
# 1. Rotate the array to the left by K steps.
# 2. Rotate a 2D matrix by 90 degrees (Transpose + Reverse columns).

def reverse_sub_array(arr, start, end):
    """Helper function to reverse sub-array in-place"""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, k):
    n = len(arr)
    if n == 0:
        return
        
    k = k % n  # Normalize k
    
    # Step A: Reverse the entire array
    reverse_sub_array(arr, 0, n - 1)
    # Step B: Reverse the first k elements
    reverse_sub_array(arr, 0, k - 1)
    # Step C: Reverse the remaining elements
    reverse_sub_array(arr, k, n - 1)


# =====================================================================
# PROBLEM 3: Move Zeros to the End
# =====================================================================
# Problem Statement:
# Given an integer array, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements. Do this in-place.
#
# Approach:
# Two-Pointer Partition:
# We maintain a 'non_zero_idx' pointer at 0.
# We iterate through the array with a scanner index 'i':
# - If arr[i] is non-zero, swap arr[i] with arr[non_zero_idx], and increment non_zero_idx.
# This pushes all zeros to the right of non_zero_idx.
#
# Time Complexity: O(N) - single pass scan
# Space Complexity: O(1) - in-place swapping
#
# Common Interview Variations:
# 1. Move all negative numbers to one side of the array (preserving or not preserving order).
# 2. Dutch National Flag Problem (Sort 0s, 1s, and 2s in-place).

def move_zeros(arr):
    non_zero_idx = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_idx], arr[i] = arr[i], arr[non_zero_idx]
            non_zero_idx += 1


# =====================================================================
# PROBLEM 4: Merge Two Sorted Arrays
# =====================================================================
# Problem Statement:
# Given two sorted integer arrays, merge them into a single sorted array.
#
# Approach:
# Two-Pointer Comparison:
# Initialize two pointers, 'i' at start of arr1, and 'j' at start of arr2.
# Compare elements and append the smaller one to a result list.
# Once one array is exhausted, append the remaining elements of the other array.
#
# Time Complexity: O(M + N) - where M and N are lengths of arr1 and arr2
# Space Complexity: O(M + N) - space for storing merged output list
#
# Common Interview Variations:
# 1. Merge sorted arrays in-place (arr1 has extra size buffer at end for arr2).
# 2. Merge K sorted arrays/lists (solved efficiently using Min-Heap / Priority Queue).

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0
    
    # Compare elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    # Append remaining elements
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
        
    return merged


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Second Largest
    list_1 = [12, 35, 1, 10, 34, 1]
    print("=======================================")
    print("Problem 1: Second Largest Element")
    print(f"Input: {list_1}")
    print(f"Output: {find_second_largest(list_1)}")
    
    # Test Problem 2: Rotate Array
    list_2 = [1, 2, 3, 4, 5, 6, 7]
    k_steps = 3
    print("\n=======================================")
    print("Problem 2: Rotate Array by K steps")
    print(f"Input: {list_2} | K: {k_steps}")
    rotate_array(list_2, k_steps)
    print(f"Output (Rotated): {list_2}")
    
    # Test Problem 3: Move Zeros
    list_3 = [0, 1, 0, 3, 12, 0]
    print("\n=======================================")
    print("Problem 3: Move Zeros to the End")
    print(f"Input: {list_3}")
    move_zeros(list_3)
    print(f"Output (Moved): {list_3}")
    
    # Test Problem 4: Merge Sorted Arrays
    list_4_a = [1, 3, 5, 7]
    list_4_b = [2, 4, 6, 8, 10]
    print("\n=======================================")
    print("Problem 4: Merge Sorted Arrays")
    print(f"Input A: {list_4_a} | Input B: {list_4_b}")
    merged_res = merge_sorted_arrays(list_4_a, list_4_b)
    print(f"Output (Merged): {merged_res}")
    print("=======================================")

"""
Key Takeaways:
- Two-pointer techniques (using start/end indices) optimize space complexity from O(N) to O(1) in-place.
- Reversal algorithms bypass the need for shifting elements or creating extra buffer lists for rotation tasks.
- Modulo division (`K = K % N`) prevents index overflow errors during rotation boundaries.

Interview Relevance:
- Array manipulations are the baseline of almost all technical screen rounds.
- Focus on explaining the space complexity optimization from O(N) to O(1) (in-place swaps).
- Handle index boundary edge cases (like empty arrays, single elements, or duplicate values).

AI/ML Relevance:
- Vector/Matrix Operations: Tensors are represented as high-dimensional arrays. Permuting dimensions (like transposing image channels) uses array indexing calculations.
- Shuffling Datasets: Custom dataset loaders shuffle data elements using index swap variables similar to the zero-moving partition code.
"""
