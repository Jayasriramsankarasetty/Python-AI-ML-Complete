"""
Topic:
Two-Pointer Coding Problems

Importance:
The two-pointer technique optimizes memory footprint by replacing intermediate lists
with index variables, reducing time complexity from O(N^2) to O(N).

This file covers:
- Problem 1: Valid Palindrome
- Problem 2: Container With Most Water
- Problem 3: Remove Duplicates from Sorted Array
"""

# =====================================================================
# PROBLEM 1: Valid Palindrome
# =====================================================================
# Problem Statement:
# Given a string s, return True if it is a palindrome, or False otherwise,
# after converting all uppercase letters into lowercase letters and removing
# all non-alphanumeric characters.
#
# Approach:
# Opposite Ends Pointers:
# Initialize 'left' = 0 and 'right' = len(s) - 1.
# Loop while left < right:
# - If s[left] is not alphanumeric, increment left.
# - If s[right] is not alphanumeric, decrement right.
# - Otherwise, if lowercase characters don't match, return False.
#   Increment left and decrement right.
# Return True if loop completes.
#
# Time Complexity: O(N) - single pass scan
# Space Complexity: O(1) - in-place comparison without creating extra string copies
#
# Common Interview Variations:
# 1. Valid Palindrome II (allows deleting at most one character to make it a palindrome).
# 2. Minimum additions to make string palindrome.

def is_valid_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Move pointers inward if pointing to non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Compare lowercase values
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True


# =====================================================================
# PROBLEM 2: Container With Most Water
# =====================================================================
# Problem Statement:
# Given an integer array height of length n. There are n vertical lines drawn
# such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water. Return the maximum amount of water.
#
# Approach:
# Greedy Two-Pointer Contraction:
# Initialize 'left' = 0 and 'right' = len(height) - 1.
# Calculate water volume at current bounds: (right - left) * min(height[left], height[right]).
# To maximize, we must greedily move the pointer pointing to the shorter line inward,
# hoping to find a taller boundary line that compensates for the decreased width.
#
# Time Complexity: O(N) - pointers contract exactly N steps combined
# Space Complexity: O(1) - only integer variables tracked
#
# Common Interview Variations:
# 1. Trapping Rain Water (calculates total water volume trapped between all blocks).
# 2. Maximum area of a histogram rectangle (solved using Monotonic Stacks).

def max_area(height):
    left = 0
    right = len(height) - 1
    max_val = 0
    
    while left < right:
        # Width represents index difference
        width = right - left
        # Height is determined by the shorter of the two lines
        current_height = min(height[left], height[right])
        
        # Calculate volume
        volume = width * current_height
        max_val = max(max_val, volume)
        
        # Shift the shorter boundary inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_val


# =====================================================================
# PROBLEM 3: Remove Duplicates from Sorted Array
# =====================================================================
# Problem Statement:
# Given an integer array nums sorted in non-decreasing order, remove the duplicates
# in-place such that each unique element appears only once. The relative order
# of the elements should be kept the same. Then return the number of unique elements.
#
# Approach:
# Fast & Slow Runners:
# We maintain a 'slow' pointer at 0 representing the index of the last unique element seen.
# We scan the array using a 'fast' pointer:
# - If nums[fast] is not equal to nums[slow], it means we found a new unique value.
#   Increment 'slow', copy nums[fast] to nums[slow], and continue scanning.
# Return slow + 1 (the count of unique elements).
#
# Time Complexity: O(N) - single pass scan
# Space Complexity: O(1) - in-place update
#
# Common Interview Variations:
# 1. Remove Duplicates II (allowing duplicates to appear at most twice).
# 2. Move Element (remove all instances of a target value in-place).

def remove_duplicates(nums):
    if not nums:
        return 0
        
    slow = 0
    for fast in range(1, len(nums)):
        # If new unique value is found, copy it to the next unique slot
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
            
    return slow + 1


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Valid Palindrome
    str_1 = "A man, a plan, a canal: Panama"
    print("=======================================")
    print("Problem 1: Valid Palindrome")
    print(f"Input string: '{str_1}'")
    print(f"Output Palindrome status: {is_valid_palindrome(str_1)}")
    
    # Test Problem 2: Container With Most Water
    heights_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("\n=======================================")
    print("Problem 2: Container With Most Water")
    print(f"Input heights: {heights_list}")
    print(f"Output Max Volume: {max_area(heights_list)}")
    
    # Test Problem 3: Remove Duplicates
    sorted_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("\n=======================================")
    print("Problem 3: Remove Duplicates from Sorted Array")
    print(f"Input array before: {sorted_nums}")
    unique_count = remove_duplicates(sorted_nums)
    print(f"Output Unique Count: {unique_count}")
    print(f"Output Array after (modified up to count): {sorted_nums[:unique_count]}")
    print("=======================================")

"""
Key Takeaways:
- Two-pointer contraction (opposite ends) solves boundary problems like max area volume in O(N) time.
- Slow-fast runners are ideal to shift elements in-place inside sorted arrays.
- Skipping non-valid indices inline prevents allocating secondary string copies.

Interview Relevance:
- Always ask if modifications should be in-place (O(1) auxiliary space).
- Clarify if inputs can be negative, empty, or unsorted (which might require O(N log N) sorting first).

AI/ML Relevance:
- Image Padding and Cropping: Scanning image coordinates outwards to check boundaries uses similar left/right index bounds checks.
- Vocabulary Indexing: Cleaning duplicate tokens from parsed documents inside text preprocessing pipelines uses slow-fast index updates to conserve memory.
"""
