"""
Topic:
Queue and Deque Coding Problems

Importance:
Queues implement FIFO structures. Working with deques (double-ended queues) builds
skills in sliding window optimizations, buffer scheduling, and streams processing.

This file covers:
- Problem 1: Implement Queue using Stacks
- Problem 2: First Unique Character in a String
- Problem 3: Sliding Window Maximum (Monotonic Deque)
"""

from collections import deque

# =====================================================================
# PROBLEM 1: Implement Queue using Stacks
# =====================================================================
# Problem Statement:
# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal queue
# (push, pop, peek, empty).
#
# Approach:
# Two Stacks ('input_stack', 'output_stack'):
# - push(x): Push x onto input_stack.
# - pop():
#   - If output_stack is empty, pop all elements from input_stack and push them to output_stack
#     (this reverses the elements' order, making LIFO behave like FIFO).
#   - Pop from output_stack.
# - peek(): Similar to pop(), but returns the top of output_stack without removing it.
# - empty(): Return True if both stacks are empty; else False.
#
# Time Complexity:
# - push(): O(1)
# - pop() / peek(): O(1) amortized (each element is moved between stacks at most once)
# - empty(): O(1)
# Space Complexity: O(N) - to store elements in stacks
#
# Common Interview Variations:
# 1. Implement Stack using Queues (solved similarly by using one or two queues).
# 2. Design a circular queue (using array index offsets).

class QueueUsingStacks:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
        
    def push(self, x):
        self.input_stack.append(x)
        
    def _shift_stacks(self):
        # Shift elements only if output_stack is empty
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
                
    def pop(self):
        self._shift_stacks()
        return self.output_stack.pop() if self.output_stack else None
        
    def peek(self):
        self._shift_stacks()
        return self.output_stack[-1] if self.output_stack else None
        
    def empty(self):
        return not self.input_stack and not self.output_stack


# =====================================================================
# PROBLEM 2: First Unique Character in a String
# =====================================================================
# Problem Statement:
# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.
#
# Approach:
# Queue and Hash Map:
# We maintain a frequency hash map for characters, and a queue containing tuples of (char, index).
# - We scan the string character-by-character:
#   - Increment its count in the frequency map.
#   - Push (char, index) to the queue.
# - Pop elements from the front of the queue if their frequency count in our map is > 1.
# - The character at the front of the queue after this cleanup is our first unique character.
#
# Time Complexity: O(N) - single pass scan
# Space Complexity: O(1) - auxiliary map and queue store at most constant alphabet size (e.g. 26 characters)
#
# Common Interview Variations:
# 1. First non-repeating character in a stream of characters (solved online using queues).
# 2. Find first unique number in a stream of integers.

def first_uniq_char(s):
    char_counts = {}
    queue = deque()
    
    for idx, char in enumerate(s):
        char_counts[char] = char_counts.get(char, 0) + 1
        queue.append((char, idx))
        
        # Clean up queue: remove characters from front if they are duplicates
        while queue and char_counts[queue[0][0]] > 1:
            queue.popleft()
            
    return queue[0][1] if queue else -1


# =====================================================================
# PROBLEM 3: Sliding Window Maximum
# =====================================================================
# Problem Statement:
# Given an integer array nums and a sliding window of size k, return the max sliding window.
#
# Approach:
# Monotonic Double-ended Queue (Deque):
# We maintain a deque ('q') storing indices of elements. The deque is kept monotonically decreasing:
# - For each element nums[i] at index i:
#   - Remove indices from the front of the deque if they fall outside the current window (i.e. index < i - k + 1).
#   - Remove indices from the back of the deque if their corresponding values nums[idx] <= nums[i]
#     (since they can never be the maximum in any window containing nums[i]).
#   - Append index i to the back of the deque.
# - The element at nums[q[0]] is the maximum for the current window. Record it once window reaches size k.
#
# Time Complexity: O(N) - each element index is appended and popped from the deque at most once
# Space Complexity: O(K) - deque stores at most K elements inside the window
#
# Common Interview Variations:
# 1. Sliding Window Minimum (maintains a monotonically increasing deque).
# 2. Longest continuous subarray with absolute difference less than or equal to limit (solved using max and min deques).

def max_sliding_window(nums, k):
    n = len(nums)
    if n == 0 or k == 0:
        return []
        
    q = deque()  # stores indices
    res = []
    
    for i in range(n):
        # Remove elements out of window range from front
        if q and q[0] < i - k + 1:
            q.popleft()
            
        # Remove elements smaller than current element from back
        while q and nums[q[-1]] <= nums[i]:
            q.pop()
            
        # Append current index
        q.append(i)
        
        # Record max element of current window
        if i >= k - 1:
            res.append(nums[q[0]])
            
    return res


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Queue using Stacks
    print("=======================================")
    print("Problem 1: Implement Queue using Stacks")
    my_queue = QueueUsingStacks()
    my_queue.push(1)
    my_queue.push(2)
    print("Pushed elements: 1, 2")
    print(f"peek() output: {my_queue.peek()}")  # returns 1
    print(f"pop() output: {my_queue.pop()}")    # returns 1
    print(f"empty() output: {my_queue.empty()}")  # returns False
    
    # Test Problem 2: First Unique Character
    str_val = "loveleetcode"
    print("\n=======================================")
    print("Problem 2: First Unique Character in a String")
    print(f"Input: '{str_val}'")
    idx = first_uniq_char(str_val)
    print(f"Output index: {idx} (character: '{str_val[idx]}' if index != -1)")
    
    # Test Problem 3: Sliding Window Maximum
    nums_list = [1, 3, -1, -3, 5, 3, 6, 7]
    k_window = 3
    print("\n=======================================")
    print("Problem 3: Sliding Window Maximum")
    print(f"Input nums: {nums_list} | K: {k_window}")
    print(f"Output list: {max_sliding_window(nums_list, k_window)}")
    print("=======================================")

"""
Key Takeaways:
- Standard Python lists are inefficient as queues because `pop(0)` is O(N); `collections.deque` provides O(1) operations.
- Two stacks achieve O(1) amortized FIFO behavior by reversing elements on demand.
- Monotonic deques prune indices of values that are smaller and older than new elements, keeping sliding window lookups O(1).

Interview Relevance:
- Deques are powerful structures when elements must be added or removed from both ends.
- Be comfortable explaining how the monotonic queue maintains ordered index states.

AI/ML Relevance:
- Data Batch Streaming: Buffer scheduling pipelines load text documents into GPU memory queues sequentially.
- Message Brokers: Real-time prediction tasks queue inference queries in FIFO structures before feeding them to host GPUs.
"""
