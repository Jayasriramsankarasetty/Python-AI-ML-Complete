"""
Topic:
String Coding Problems

Importance:
Strings represent sequence collections of text. Solving string problems reinforces
casing normalization, token separation, word manipulations, and sub-sequence parsing.

This file covers:
- Problem 1: Valid Anagram
- Problem 2: Reverse Words in a String
- Problem 3: Longest Palindromic Substring
"""

# =====================================================================
# PROBLEM 1: Valid Anagram
# =====================================================================
# Problem Statement:
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.
# An Anagram is a word formed by rearranging the letters of a different word,
# using all the original letters exactly once.
#
# Approach:
# Hash Map Frequency Counter:
# If string lengths differ, they cannot be anagrams (return False).
# Create a frequency count mapping dictionary.
# Loop through both strings: increment counts for s, decrement counts for t.
# If all final counts are 0, return True; else False.
#
# Time Complexity: O(N) - where N is the length of strings
# Space Complexity: O(1) - auxiliary space is bounded because alphabet size is constant (e.g. 26 characters)
#
# Common Interview Variations:
# 1. Group Anagrams: Given an array of strings, group anagrams together (solved using sorted keys dict).
# 2. Find All Anagrams in a String (solved using sliding window and target count array).

def is_anagram(s, t):
    if len(s) != len(t):
        return False
        
    char_counts = {}
    
    # Increment for s, decrement for t
    for i in range(len(s)):
        char_counts[s[i]] = char_counts.get(s[i], 0) + 1
        char_counts[t[i]] = char_counts.get(t[i], 0) - 1
        
    # Check if any count is non-zero
    for count in char_counts.values():
        if count != 0:
            return False
            
    return True


# =====================================================================
# PROBLEM 2: Reverse Words in a String
# =====================================================================
# Problem Statement:
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s
# will be separated by at least one space. Return a string of the words in
# reverse order concatenated by a single space.
#
# Approach:
# 1. Split the string by whitespace. In Python, s.split() automatically handles
#    multiple adjacent spaces and trims leading/trailing spaces.
# 2. Reverse the list of token words.
# 3. Join the list back together with a single space separator.
#
# Time Complexity: O(N) - where N is the length of string
# Space Complexity: O(N) - to store word list tokens
#
# Common Interview Variations:
# 1. Reverse words in-place (if input is list of characters, solved by reversing individual words then whole array).
# 2. Reverse individual words in a string (e.g., "the sky" -> "eht yks").

def reverse_words(s):
    # s.split() handles multiple spaces and strips automatically
    words = s.split()
    # Reverse list of words in-place
    words.reverse()
    # Join with single space
    return " ".join(words)


# =====================================================================
# PROBLEM 3: Longest Palindromic Substring
# =====================================================================
# Problem Statement:
# Given a string s, return the longest palindromic substring in s.
#
# Approach:
# Expand Around Center:
# A palindrome mirrors around its center. A string of length N has 2N - 1 possible centers:
# - Odd length centers: single character centers (i)
# - Even length centers: space between adjacent characters (i, i+1)
# For each center, we expand outwards as long as matching characters are found.
# Track and update the maximum length boundaries.
#
# Time Complexity: O(N^2) - expanding from each center takes up to O(N)
# Space Complexity: O(1) - constant auxiliary space
#
# Common Interview Variations:
# 1. Count Palindromic Substrings (returns count instead of actual substring).
# 2. Longest Palindromic Subsequence (solved using 2D dynamic programming).

def expand_around_center(s, left, right):
    # Expands outwards as long as bounds are valid and characters match
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Returns start and end indices of the palindrome
    # (Note: left+1 and right-1 are the actual palindrome bounds because the loop exited after decrement/increment)
    return left + 1, right - 1

def longest_palindrome(s):
    if not s:
        return ""
        
    start = 0
    end = 0
    
    for i in range(len(s)):
        # Case A: Odd length palindrome (centered on character i)
        l1, r1 = expand_around_center(s, i, i)
        
        # Case B: Even length palindrome (centered between i and i+1)
        l2, r2 = expand_around_center(s, i, i + 1)
        
        # Update bounds if a longer palindrome is found
        if (r1 - l1) > (end - start):
            start = l1
            end = r1
            
        if (r2 - l2) > (end - start):
            start = l2
            end = r2
            
    return s[start : end + 1]


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Valid Anagram
    str1_a = "anagram"
    str1_b = "nagaram"
    print("=======================================")
    print("Problem 1: Valid Anagram")
    print(f"Inputs: '{str1_a}', '{str1_b}'")
    print(f"Output: {is_anagram(str1_a, str1_b)}")
    
    # Test Problem 2: Reverse Words
    str_sentence = "  the sky   is blue  "
    print("\n=======================================")
    print("Problem 2: Reverse Words in a String")
    print(f"Input: '{str_sentence}'")
    print(f"Output: '{reverse_words(str_sentence)}'")
    
    # Test Problem 3: Longest Palindrome Substring
    str_palindrome = "babad"
    print("\n=======================================")
    print("Problem 3: Longest Palindromic Substring")
    print(f"Input: '{str_palindrome}'")
    print(f"Output: '{longest_palindrome(str_palindrome)}'")
    print("=======================================")

"""
Key Takeaways:
- String operations in Python instantiate new strings because of immutability.
- Comparing character frequencies can be optimized to O(N) time and O(1) space using standard key-counters.
- Expand-around-center checks O(2N) centers in O(N^2) worst-case time, bypassing dynamic programming memory overheads.

Interview Relevance:
- String manipulation is a key topic in placement tests.
- Know how Python handles string allocations (string pool reference memory).
- Always verify whitespace parsing requirements (trimming, double spacing).

AI/ML Relevance:
- NLP Normalization: Clean string parsing (removing punctuation, lowercasing, word reversals) is required to parse sentences for bag-of-words classifications.
- Regex Tokenization: Text sequences are prepared by splitting string arrays into list vocab structures.
"""
