"""
Topic:
Advanced Binary Search Problems

Importance:
Binary Search is a flexible framework that extends beyond searching arrays to checking
boundaries (first/last index), searching peaks on gradients, and searching parameter values
on answer ranges.

This file covers:
- Problem 1: First and Last Position of Element in Sorted Array
- Problem 2: Find Peak Element
- Problem 3: Koko Eating Bananas (Binary Search on Answer)
"""

# =====================================================================
# PROBLEM 1: First and Last Position of Element in Sorted Array
# =====================================================================
# Problem Statement:
# Given an array of integers nums sorted in non-decreasing order, find the starting
# and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
#
# Approach:
# Two Binary Searches:
# Write a helper binary search function `find_bound(is_first)`:
# - If nums[mid] == target:
#   - If searching first position (is_first=True): we want to see if there is another matching
#     target on the left: set right = mid - 1. Record mid as potential first bound.
#   - If searching last position (is_first=False): check right side: set left = mid + 1. Record mid.
# - If nums[mid] < target: left = mid + 1.
# - Otherwise: right = mid - 1.
# Run helper twice to get [first, last].
#
# Time Complexity: O(log N) - two binary search sweeps
# Space Complexity: O(1) - constant memory
#
# Common Interview Variations:
# 1. Count occurrences of target in sorted array (calculated as last - first + 1).
# 2. Search Insertion Position (LeetCode 35).

def find_bound(nums, target, is_first):
    left, right = 0, len(nums) - 1
    bound = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            bound = mid
            if is_first:
                right = mid - 1  # check left side
            else:
                left = mid + 1   # check right side
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return bound

def search_range(nums, target):
    first = find_bound(nums, target, is_first=True)
    last = find_bound(nums, target, is_first=False)
    return [first, last]


# =====================================================================
# PROBLEM 2: Find Peak Element
# =====================================================================
# Problem Statement:
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
# You must write an algorithm that runs in O(log n) time.
#
# Approach:
# Binary Search on Gradient:
# If nums[mid] < nums[mid + 1], it means a peak must lie on the right side of mid
# (since the array rises from mid to mid+1). We set left = mid + 1.
# Otherwise, the gradient drops or is equal (nums[mid] >= nums[mid + 1]), meaning
# a peak lies on the left side (including mid itself). We set right = mid.
# The search loop converges at a local peak index.
#
# Time Complexity: O(log N) - search space divided by 2
# Space Complexity: O(1) - constant memory
#
# Common Interview Variations:
# 1. Find minimum in rotated sorted array.
# 2. Peak Index in a Mountain Array (strictly rising then strictly falling).

def find_peak_element(nums):
    left = 0
    right = len(nums) - 1
    
    # Notice: we terminate when left == right, converging on the peak
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] < nums[mid + 1]:
            # Peak lies to the right
            left = mid + 1
        else:
            # Peak lies to the left (including mid)
            right = mid
            
    return left


# =====================================================================
# PROBLEM 3: Koko Eating Bananas
# =====================================================================
# Problem Statement:
# There are n piles of bananas, the i-th pile has piles[i] bananas. The guards will return in h hours.
# Koko wants to find the minimum integer eating speed k (bananas/hour) such that she can
# eat all the bananas within h hours.
#
# Approach:
# Binary Search on Answer Range:
# The minimum possible speed is 1. The maximum possible speed is max(piles)
# (at which she finishes all piles in exactly len(piles) hours).
# Set left = 1, right = max(piles).
# Loop while left < right:
# - mid represents current speed candidate.
# - Calculate hours required at speed 'mid': sum(ceil(pile / mid) for pile in piles).
# - If total hours <= h, speed 'mid' is feasible. Try to find a smaller speed: right = mid.
# - Otherwise, speed 'mid' is too slow: set left = mid + 1.
# Return left.
#
# Time Complexity: O(N log(M)) - where N is len(piles), and M is max(piles)
# Space Complexity: O(1) - constant memory
#
# Common Interview Variations:
# 1. Capacity to Ship Packages Within D Days (LeetCode 1011).
# 2. Split Array Largest Sum (LeetCode 410).

def is_feasible_speed(piles, speed, h):
    import math
    hours = 0
    for pile in piles:
        hours += math.ceil(pile / speed)
    return hours <= h

def min_eating_speed(piles, h):
    left = 1
    right = max(piles)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if is_feasible_speed(piles, mid, h):
            right = mid  # try to find a smaller feasible speed
        else:
            left = mid + 1  # speed is too slow, increase speed
            
    return left


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: First and Last Position
    nums_1 = [5, 7, 7, 8, 8, 10]
    target_1 = 8
    print("=======================================")
    print("Problem 1: First & Last Position in Sorted Array")
    print(f"Input: {nums_1} | Target: {target_1}")
    print(f"Output Range: {search_range(nums_1, target_1)}")
    
    # Test Problem 2: Find Peak Element
    nums_2 = [1, 2, 1, 3, 5, 6, 4]
    print("\n=======================================")
    print("Problem 2: Find Peak Element")
    print(f"Input: {nums_2}")
    peak_idx = find_peak_element(nums_2)
    print(f"Output Peak Index: {peak_idx} (Element value: {nums_2[peak_idx]})")
    
    # Test Problem 3: Koko Eating Bananas
    piles_list = [3, 6, 7, 11]
    hours_limit = 8
    print("\n=======================================")
    print("Problem 3: Koko Eating Bananas (Binary Search on Answer)")
    print(f"Piles: {piles_list} | Hours Limit: {hours_limit}")
    print(f"Minimum eating speed: {min_eating_speed(piles_list, hours_limit)} bananas/hour")
    print("=======================================")

"""
Key Takeaways:
- Helper flags (`is_first`) allow using a single binary search core structure to locate left and right bounds.
- Peak element searching on unsorted arrays proves binary search only requires an ordering check (slopes), not a fully sorted array.
- Binary search on answer ranges solves optimization problems by checking feasibility of bounds iteratively.

Interview Relevance:
- If a problem asks to find the minimum/maximum of something under a constraint, consider "Binary Search on Answer".
- Pay attention to division rounding limits (using math.ceil).

AI/ML Relevance:
- Hyperparameter search: In automated ML (AutoML), parameters (like finding the optimal weight decay threshold value) are located using binary search bounds checking.
- Quantization limits: Finding optimal bits boundaries to quantize float weights to integers uses binary search iterations.
"""
