"""
Topic:
Searching Coding Problems

Importance:
Searching is the core of query resolution. Optimizing searches from linear time O(N)
to logarithmic time O(log N) is highly valued in technical coding loops.

This file covers:
- Problem 1: Linear Search
- Problem 2: Binary Search (Iterative)
- Problem 3: Search in a Rotated Sorted Array
"""

# =====================================================================
# PROBLEM 1: Linear Search
# =====================================================================
# Problem Statement:
# Given an array of integers nums and a target value target, search for target.
# If it exists, return its index; otherwise, return -1.
#
# Approach:
# We sequentially scan the array elements from index 0 to N-1.
# If nums[i] matches target, return index i. If loop completes, return -1.
#
# Time Complexity: O(N) - worst-case scan is N elements
# Space Complexity: O(1) - only loop variables tracked
#
# Common Interview Variations:
# 1. Search in a 2D matrix (scans row by row, or binary searches if matrix is sorted).
# 2. Find all occurrences of target in an unsorted array.

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# =====================================================================
# PROBLEM 2: Binary Search (Iterative)
# =====================================================================
# Problem Statement:
# Given a sorted integer array nums (in ascending order) and a target value target,
# search for target using binary search. If it exists, return its index; otherwise, return -1.
#
# Approach:
# Iterative Binary Search:
# We maintain two pointers, 'left' at 0 and 'right' at len(nums) - 1.
# Loop while left <= right:
# - Calculate midpoint: mid = left + (right - left) // 2 (to prevent integer overflow).
# - If nums[mid] equals target, return mid.
# - If nums[mid] < target, target lies in right half: set left = mid + 1.
# - Otherwise, target lies in left half: set right = mid - 1.
# Return -1 if loop exits without match.
#
# Time Complexity: O(log N) - search space is divided by 2 at each step
# Space Complexity: O(1) - constant memory
#
# Common Interview Variations:
# 1. Recursive Binary Search (takes O(log N) space due to call stack).
# 2. Find first/last position of element in sorted array (lower_bound / upper_bound).

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1


# =====================================================================
# PROBLEM 3: Search in a Rotated Sorted Array
# =====================================================================
# Problem Statement:
# Given a sorted integer array nums (distinct values) that is rotated at an unknown pivot
# index beforehand, search for a target value. Return its index if found; else -1.
#
# Approach:
# Modified Binary Search:
# Even in a rotated sorted array, splitting the array in half guarantees that
# at least one of the halves (left or right) is sorted.
# 1. Calculate mid.
# 2. If nums[mid] == target, return mid.
# 3. Check if Left Half is sorted (nums[left] <= nums[mid]):
#    - If target lies in left sorted range (nums[left] <= target < nums[mid]):
#      Search left: right = mid - 1.
#    - Else, search right: left = mid + 1.
# 4. Otherwise, Right Half must be sorted:
#    - If target lies in right sorted range (nums[mid] < target <= nums[right]):
#      Search right: left = mid + 1.
#    - Else, search left: right = mid - 1.
#
# Time Complexity: O(log N) - binary divisions maintained
# Space Complexity: O(1) - constant memory
#
# Common Interview Variations:
# 1. Search in Rotated Sorted Array II (array contains duplicates).
# 2. Find minimum element in rotated sorted array.

def search_rotated_array(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
            
        # Case A: Left half is sorted
        if nums[left] <= nums[mid]:
            # Target lies inside left sorted partition bounds
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Case B: Right half is sorted
        else:
            # Target lies inside right sorted partition bounds
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Linear Search
    nums_1 = [4, 2, 1, 9, 7]
    target_1 = 9
    print("=======================================")
    print("Problem 1: Linear Search")
    print(f"Input: {nums_1} | Target: {target_1}")
    print(f"Output Index: {linear_search(nums_1, target_1)}")
    
    # Test Problem 2: Binary Search
    nums_2 = [1, 3, 5, 7, 9, 11]
    target_2 = 9
    print("\n=======================================")
    print("Problem 2: Binary Search (Iterative)")
    print(f"Input: {nums_2} | Target: {target_2}")
    print(f"Output Index: {binary_search(nums_2, target_2)}")
    
    # Test Problem 3: Search in Rotated Sorted Array
    nums_3 = [4, 5, 6, 7, 0, 1, 2]
    target_3 = 0
    print("\n=======================================")
    print("Problem 3: Search in a Rotated Sorted Array")
    print(f"Input: {nums_3} | Target: {target_3}")
    print(f"Output Index: {search_rotated_array(nums_3, target_3)}")
    print("=======================================")

"""
Key Takeaways:
- Binary Search runs in logarithmic O(log N) time, making it highly optimal for sorted datasets.
- To avoid integer overflow in other languages, calculate mid as `left + (right - left) // 2` instead of `(left + right) // 2`.
- Rotated sorted array search relies on identifying which half of the array is sorted at each step.

Interview Relevance:
- If an array is sorted, always consider binary search or two-pointer options first.
- Handle search boundary index checks cleanly.

AI/ML Relevance:
- Hyperparameter Tuning: Grid-search parameter values are searched using search indices.
- Vector Similarity Quantization: Searching nearest neighbors in database clusters (like FAISS index splits) uses binary search trees to perform lookups in O(log N) time.
"""
