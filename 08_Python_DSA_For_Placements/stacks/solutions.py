"""
Topic:
Stack Coding Problems

Importance:
Stacks implement LIFO structures. Working with stacks develops state backtracking logic,
custom data class designs, and monotonic stack optimizations which are standard in placements.

This file covers:
- Problem 1: Valid Parentheses
- Problem 2: Min Stack Class Design
- Problem 3: Next Greater Element I (Monotonic Stack)
"""

# =====================================================================
# PROBLEM 1: Valid Parentheses
# =====================================================================
# Problem Statement:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
#
# Approach:
# LIFO Stack:
# We maintain a list acting as a stack.
# We map closing brackets to their matching opening brackets: {')': '(', '}': '{', ']': '['}.
# Iterate through characters in s:
# - If character is a closing bracket:
#   - Pop the top of the stack (if empty, pop a dummy val like '#').
#   - Check if popped element matches character's opening bracket. If not, return False.
# - If opening bracket, push it to stack.
# After loop, return True if stack is empty; else False.
#
# Time Complexity: O(N) - single pass scan
# Space Complexity: O(N) - stack stores up to N elements
#
# Common Interview Variations:
# 1. Minimum Add to Make Parentheses Valid.
# 2. Longest Valid Parentheses (solved using stacks tracking indices).

def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            # Pop top element if stack is not empty; else use dummy value
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
            
    return not stack


# =====================================================================
# PROBLEM 2: Min Stack Class Design
# =====================================================================
# Problem Statement:
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time O(1).
# Implement the MinStack class:
# - MinStack() initializes the stack object.
# - void push(int val) pushes the element val onto the stack.
# - void pop() removes the element on the top of the stack.
# - int top() gets the top element of the stack.
# - int getMin() retrieves the minimum element in the stack.
#
# Approach:
# Two Stacks Strategy:
# We maintain two standard lists:
# - 'main_stack': stores all elements.
# - 'min_stack': stores historical minimum values.
# When pushing val:
# - Push val to main_stack.
# - Push min(val, top of min_stack) to min_stack.
# When popping:
# - Pop from both main_stack and min_stack.
#
# Time Complexity: O(1) for all operations
# Space Complexity: O(N) - two stacks store up to N elements
#
# Common Interview Variations:
# 1. Design a Max Stack (retrieving the maximum element in O(1) time).
# 2. Design a Stack supporting getMin() with O(1) auxiliary space (using a mathematical diff variable).

class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        
    def push(self, val):
        self.main_stack.append(val)
        # Push to min_stack
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
            
    def pop(self):
        if self.main_stack:
            self.main_stack.pop()
            self.min_stack.pop()
            
    def top(self):
        return self.main_stack[-1] if self.main_stack else None
        
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None


# =====================================================================
# PROBLEM 3: Next Greater Element I
# =====================================================================
# Problem Statement:
# Given an array nums, find the next greater element for each element.
# The Next Greater Element of an element x is the first greater element to its right.
# If it does not exist, return -1 for this element.
#
# Approach:
# Monotonic Stack:
# We scan nums from right to left, maintaining a stack of elements that decreases monotonically.
# - For current element x:
#   - Pop elements from stack while they are <= x (since they can never be the next greater element for values to the left of x).
#   - If stack is not empty, next greater element for x is the top of the stack; else it is -1.
#   - Push x to the stack.
# We construct the results list matching indices.
#
# Time Complexity: O(N) - each element is pushed and popped at most once
# Space Complexity: O(N) - stack and hash map store up to N elements
#
# Common Interview Variations:
# 1. Daily Temperatures (return array of days to wait for warmer temperature, solved by storing indices in monotonic stack).
# 2. Next Greater Element II (input array is circular, solved by scanning array twice).

def next_greater_element(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        x = nums[i]
        
        # Pop elements smaller than or equal to current element
        while stack and stack[-1] <= x:
            stack.pop()
            
        # Top of stack is next greater element
        if stack:
            res[i] = stack[-1]
            
        # Push current element
        stack.append(x)
        
    return res


# ==========================================
# Execution Verification
# ==========================================
if __name__ == "__main__":
    # Test Problem 1: Valid Parentheses
    str_1 = "()[]{}"
    str_2 = "(]"
    print("=======================================")
    print("Problem 1: Valid Parentheses")
    print(f"Input: '{str_1}' | Output: {is_valid_parentheses(str_1)}")
    print(f"Input: '{str_2}' | Output: {is_valid_parentheses(str_2)}")
    
    # Test Problem 2: Min Stack
    print("\n=======================================")
    print("Problem 2: Min Stack Class Design")
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"Pushed: -2, 0, -3")
    print(f"getMin() output: {min_stack.getMin()}")  # returns -3
    min_stack.pop()
    print("Popped top element")
    print(f"top() output: {min_stack.top()}")        # returns 0
    print(f"getMin() output: {min_stack.getMin()}")  # returns -2
    
    # Test Problem 3: Next Greater Element I
    nums_list = [4, 5, 2, 25]
    print("\n=======================================")
    print("Problem 3: Next Greater Element (Monotonic Stack)")
    print(f"Input nums: {nums_list}")
    print(f"Output list: {next_greater_element(nums_list)}")
    print("=======================================")

"""
Key Takeaways:
- LIFO stacks maintain structural checks like bracket matching sequences.
- Min Stack uses a parallel historical minima stack to provide O(1) operations.
- Monotonic stacks prune elements that can never serve as answers, reducing quadratic scans O(N^2) to linear time O(N).

Interview Relevance:
- Monotonic stacks (increasing/decreasing order of elements in stack) are high-frequency patterns for tracking nearby ranges/extrema.
- Always check empty stack states before peeking/popping to prevent index errors.

AI/ML Relevance:
- AST Parsing: Code compiler engines parse nested Python blocks (syntax tokens) using structural stack layers.
- Backpropagation Trace: Neural network graph engines cache intermediate gradient activations in stacks to compute backwards updates.
"""
