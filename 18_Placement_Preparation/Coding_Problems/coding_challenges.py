"""
Topic:
Placement Prep - Coding Challenges (Top 5 DSA)

Importance:
Data Structures and Algorithms (DSA) form the core of technical coding rounds.
This file implements 5 high-frequency coding problems with optimized structures.

This file covers:
1. Two Sum (O(N) Hash Map)
2. Valid Parentheses (Stack)
3. Binary Search (O(log N) Binary search)
4. Merge Intervals (O(N log N) Sorting)
5. Valid Anagram (Hash Map counts)
- Automatic verification assertions
"""

# ==========================================
# 1. Two Sum
# ==========================================
# Problem: Given an array of integers 'nums' and an integer 'target', 
# return indices of the two numbers such that they add up to target.
# Complexity: O(N) Time, O(N) Space.
def two_sum(nums, target):
    seen = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
    return []

# ==========================================
# 2. Valid Parentheses
# ==========================================
# Problem: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# Complexity: O(N) Time, O(N) Space.
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else "#"
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return len(stack) == 0

# ==========================================
# 3. Binary Search
# ==========================================
# Problem: Given a sorted array of integers and a target value, 
# return the index of the target if found. Otherwise, return -1.
# Complexity: O(log N) Time, O(1) Space.
def binary_search(nums, target) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ==========================================
# 4. Merge Intervals
# ==========================================
# Problem: Given an array of intervals where intervals[i] = [start, end], 
# merge all overlapping intervals and return an array of the non-overlapping intervals.
# Complexity: O(N log N) Time, O(N) Space.
def merge_intervals(intervals):
    if not intervals:
        return []
    # Sort intervals by start value
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]
        # If current interval overlaps with the last merged, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    return merged

# ==========================================
# 5. Valid Anagram
# ==========================================
# Problem: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Complexity: O(N) Time, O(1) Space (since character set is fixed size, e.g. 26).
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1
    return True

# ==========================================
# 6. Verification Assertion Tests
# ==========================================
def verify_challenges():
    print("=======================================")
    print("Running Algorithmic Challenge Tests:")
    print("=======================================")
    
    # 1. Test Two Sum
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("[OK] Two Sum Passed!")
    
    # 2. Test Valid Parentheses
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    print("[OK] Valid Parentheses Passed!")
    
    # 3. Test Binary Search
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    print("[OK] Binary Search Passed!")
    
    # 4. Test Merge Intervals
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    print("[OK] Merge Intervals Passed!")
    
    # 5. Test Valid Anagram
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    print("[OK] Valid Anagram Passed!")
    print("=======================================")
    print("All Algorithmic Tests Executed Successfully!")
    print("=======================================")

if __name__ == "__main__":
    verify_challenges()
