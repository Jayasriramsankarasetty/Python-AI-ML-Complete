"""
Topic:
Sliding Window Coding Problems

Importance:
Sliding window optimization scans continuous arrays/strings dynamically, reducing
nested iteration search complexities from O(N^2) to linear O(N) time.

This file covers:
- Problem 1: Maximum Sum Subarray of Size K (Fixed Window)
- Problem 2: Longest Substring Without Repeating Characters (Variable Window)
- Problem 3: Minimum Window Substring (Variable Window - Hard)
"""

# =====================================================================
# PROBLEM 1: Maximum Sum Subarray of Size K
# =====================================================================
# Problem Statement:
# Given an array of integers nums and a number k, find the maximum sum of a
# contiguous subarray of size k.
#
# Approach:
# Fixed Size Sliding Window:
# 1. Calculate sum of first 'k' elements. Initialize 'max_sum' to this sum.
# 2. Iterate from index 'k' to len(nums) - 1:
#    - Add the current element (entering window) and subtract the element at index i - k (exiting window).
#    - Update 'max_sum' with the maximum of current sum and max_sum.
#
# Time Complexity: O(N) - single pass scan
# Space Complexity: O(1) - constant auxiliary space
#
# Common Interview Variations:
# 1. Minimum Sum Subarray of size K.
# 2. Maximum of all subarrays of size K (solved using Monotonic Deque).

def max_sub_array_of_size_k(nums, k):
    n = len(nums)
    if n < k or k <= 0:
        return 0
        
    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window across the array
    for i in range(k, n):
        # Subtract exiting element (nums[i-k]) and add entering element (nums[i])
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum


# =====================================================================
# PROBLEM 2: Longest Substring Without Repeating Characters
# =====================================================================
# Problem Statement:
# Given a string s, find the length of the longest substring without repeating characters.
#
# Approach:
# Variable Size Sliding Window:
# We maintain two pointers, 'left' at 0 and 'right' moving from 0 to len(s)-1.
# We track the last seen index of characters in a dictionary ('last_seen').
# - If s[right] is already in our dictionary and its last seen index is >= left:
#   Move 'left' pointer to last_seen[s[right]] + 1 (contract window).
# - Update last_seen[s[right]] = right.
# - Calculate current length = right - left + 1, and update 'max_len'.
#
# Time Complexity: O(N) - right pointer scans s; left pointer jumps forward
# Space Complexity: O(1) - hash map stores at most alphabet size characters (constant limit)
#
# Common Interview Variations:
# 1. Longest Substring with at most K distinct characters.
# 2. Longest Substring with at most 2 distinct characters.

def length_of_longest_substring(s):
    last_seen = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        char = s[right]
        
        # If character is seen inside current window, shrink the window
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
            
        last_seen[char] = right
        # Update maximum length
        max_len = max(max_len, right - left + 1)
        
    return max_len


# =====================================================================
# PROBLEM 3: Minimum Window Substring
# =====================================================================
# Problem Statement:
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates) is
# included in the window. If there is no such substring, return the empty string "".
#
# Approach:
# Sliding Window with contracting Left bound:
# 1. Create a frequency map of characters in 't' ('target_counts').
# 2. Maintain a 'window_counts' frequency map and a 'formed' counter tracking how many
#    unique characters in 't' have met their required counts inside the current window.
# 3. Slide 'right' pointer to expand window. When character counts match target, increment 'formed'.
# 4. While 'formed' equals the total unique characters in 't':
#    - Record the window coordinates if shorter than current minimum.
#    - Contract from the 'left' pointer by decrementing left character count.
#    - If character count drops below target requirement, decrement 'formed'.
#    - Increment 'left' pointer.
#
# Time Complexity: O(M + N) - where M is len(s) and N is len(t)
# Space Complexity: O(1) - unique counts dictionary stores at most constant alphabet size (e.g. 52 chars)
#
# Common Interview Variations:
# 1. Find all anagrams of string T inside string S.
# 2. Permutation in String (check if S2 contains a permutation of S1).

def min_window(s, t):
    if not s or not t:
        return ""
        
    # Count character frequencies in t
    target_counts = {}
    for char in t:
        target_counts[char] = target_counts.get(char, 0) + 1
        
    required = len(target_counts)
    
    # Left and right pointers
    left = 0
    right = 0
    
    # Track how many characters meet required frequency
    formed = 0
    window_counts = {}
    
    # Ans tuple: (window_length, left, right)
    ans = (float("inf"), None, None)
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # If frequency of current character matches target requirements, update formed
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1
            
        # Contract window as long as it contains all target characters
        while left <= right and formed == required:
            char_left = s[left]
            
            # Save smallest window
            if (right - left + 1) < ans[0]:
                ans = (right - left + 1, left, right)
                
            # Remove character from left of window
            window_counts[char_left] -= 1
            if char_left in target_counts and window_counts[char_left] < target_counts[char_left]:
                formed -= 1
                
            left += 1
            
        right += 1
        
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Max sum subarray size K
    nums_1 = [2, 1, 5, 1, 3, 2]
    k_val = 3
    print("=======================================")
    print("Problem 1: Max Sum Subarray of Size K")
    print(f"Input: {nums_1} | K: {k_val}")
    print(f"Output Max Sum: {max_sub_array_of_size_k(nums_1, k_val)}")
    
    # Test Problem 2: Longest substring unique characters
    str_2 = "abcabcbb"
    print("\n=======================================")
    print("Problem 2: Longest Substring Without Repeating Characters")
    print(f"Input: '{str_2}'")
    print(f"Output Length: {length_of_longest_substring(str_2)}")
    
    # Test Problem 3: Minimum Window Substring
    str_s = "ADOBECODEBANC"
    str_t = "ABC"
    print("\n=======================================")
    print("Problem 3: Minimum Window Substring")
    print(f"Input S: '{str_s}' | Target T: '{str_t}'")
    print(f"Output Window: '{min_window(str_s, str_t)}'")
    print("=======================================")

"""
Key Takeaways:
- Fixed sliding window operations are updated in O(1) time per slide by adding entering and subtracting exiting elements.
- Variable sliding window bounds are dynamically managed using frequency trackers.
- Expand-contract loop invariants are highly efficient, maintaining O(N) runtime regardless of contracting jumps.

Interview Relevance:
- Look for keywords like "contiguous subarray", "longest substring", or "minimum window" to identify sliding window problems.
- Always clarify window boundary constraints.

AI/ML Relevance:
- Sliding Kernel Convolutions: CNN layer filters slide across input pixel arrays with fixed width/stride settings similar to the fixed-size sliding window code.
- NLP Text Window: Training language models involves slicing token lists into context sequences (e.g. windows of 1024 tokens) to feed model inputs.
"""
