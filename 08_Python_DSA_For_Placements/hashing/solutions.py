"""
Topic:
Hashing Coding Problems using Dictionaries and Sets

Importance:
Hashing optimizes nested lookup tasks (reducing O(N^2) checks to O(N)) by trading
memory space for time. This is a critical pattern in technical coding interviews.

This file covers:
- Problem 1: Two Sum
- Problem 2: Subarray Sum Equals K
- Problem 3: Group Anagrams
"""

# =====================================================================
# PROBLEM 1: Two Sum
# =====================================================================
# Problem Statement:
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# Approach:
# We iterate through the array, tracking visited elements in a dictionary:
# - Calculate 'complement' = target - current_val.
# - If complement is already in the dictionary, return [dict[complement], current_index].
# - Else, store current_val in dictionary matching its index: dict[current_val] = current_index.
#
# Time Complexity: O(N) - single pass scan with O(1) average lookup
# Space Complexity: O(N) - hash map stores up to N elements
#
# Common Interview Variations:
# 1. Two Sum II - Input array is sorted (can be solved using two-pointer O(N) time, O(1) space).
# 2. 3Sum (finding unique triplets summing to 0, solved using sorting + two pointers).

def two_sum(nums, target):
    seen = {}  # maps value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    return []


# =====================================================================
# PROBLEM 2: Subarray Sum Equals K
# =====================================================================
# Problem Statement:
# Given an array of integers nums and an integer k, return the total number of
# continuous subarrays whose sum equals to k.
#
# Approach:
# Prefix Sum Mapping:
# We maintain a running prefix sum ('current_sum') and a hash map tracking how many
# times each prefix sum has appeared.
# - If (current_sum - k) exists in our hash map, it means there are prefix subarrays
#   that can be subtracted from the current subarray to yield sum k. We add their frequency count to our result.
# - Store or update the frequency of 'current_sum' in the hash map.
#
# Time Complexity: O(N) - single pass scan
# Space Complexity: O(N) - to store prefix sum counts
#
# Common Interview Variations:
# 1. Longest Subarray with Sum K (stores first index of prefix sum instead of counts).
# 2. Largest Subarray with 0 Sum (solved similarly using prefix sums).

def subarray_sum_equals_k(nums, k):
    # Map stores prefix_sum -> frequency count
    # Initialize with {0: 1} to handle case where prefix sum itself is exactly k
    prefix_sums = {0: 1}
    count = 0
    current_sum = 0
    
    for num in nums:
        current_sum += num
        
        # Check if matching remainder prefix sum exists
        if (current_sum - k) in prefix_sums:
            count += prefix_sums[current_sum - k]
            
        # Update prefix sum count
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        
    return count


# =====================================================================
# PROBLEM 3: Group Anagrams
# =====================================================================
# Problem Statement:
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
#
# Approach:
# Hash Map Grouping:
# Anagrams have identical characters. Sorting an anagram yields the same string.
# We create a dictionary where:
# - Key: Sorted character tuple or sorted string representing the anagram root.
# - Value: A list of original strings matching that key.
# Iterating through words, we sort each, check/insert into dict, and return dict.values().
#
# Time Complexity: O(N * L log L) - where N is length of strs list, and L is max length of a string
# Space Complexity: O(N * L) - auxiliary space to store grouped lists
#
# Common Interview Variations:
# 1. Group Shifted Strings (group words that can be shifted to match, solved by grouping difference counts).
# 2. Find All Anagrams in a String (solved using character array matches).

def group_anagrams(strs):
    grouped = {}
    
    for word in strs:
        # Sort characters to establish canonical key (tuple format is hashable)
        sorted_key = tuple(sorted(word))
        
        if sorted_key not in grouped:
            grouped[sorted_key] = []
        grouped[sorted_key].append(word)
        
    return list(grouped.values())


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Two Sum
    nums_1 = [2, 7, 11, 15]
    target_1 = 9
    print("=======================================")
    print("Problem 1: Two Sum")
    print(f"Input array: {nums_1} | Target: {target_1}")
    print(f"Output Indices: {two_sum(nums_1, target_1)}")
    
    # Test Problem 2: Subarray Sum Equals K
    nums_2 = [1, 1, 1]
    k_val = 2
    print("\n=======================================")
    print("Problem 2: Subarray Sum Equals K")
    print(f"Input: {nums_2} | K: {k_val}")
    print(f"Output Count: {subarray_sum_equals_k(nums_2, k_val)}")
    
    # Test Problem 3: Group Anagrams
    words_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("\n=======================================")
    print("Problem 3: Group Anagrams")
    print(f"Input: {words_list}")
    print(f"Output groups:\n  {group_anagrams(words_list)}")
    print("=======================================")

"""
Key Takeaways:
- Hashing reduces loop searches from nested combinations O(N^2) to single scans O(N).
- Mapping remainder complements (like `target - val` or `prefix_sum - K`) resolves matching sum conditions.
- Canonical representations (like sorting characters to group anagrams) are standard hash keys.

Interview Relevance:
- Dictionaries are Python's built-in implementation of Hash Tables. Know that operations are O(1) average but can degrade to O(N) if collisions occur.
- Be comfortable explaining space-time trade-offs.

AI/ML Relevance:
- Vocabulary mappings: Categorical token text identifiers map words to dense vector embed tables using token-to-index dict mapping lookups.
- Key-Value lookups: Transformer Attention caching stores intermediate state matrices using key index dictionary bindings.
"""
