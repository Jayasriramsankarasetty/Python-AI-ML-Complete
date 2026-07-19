"""
Topic:
Recursion in Python

Importance:
Recursion is a programming technique where a function calls itself.
It is critical for tree-based machine learning algorithms (like Decision Trees, Random Forests)
and algorithms like QuickSort, MergeSort, and Graph traversals.

This file covers:
- Concept of base case vs recursive case
- Factorial calculation via recursion
- Fibonacci sequence via recursion
- Call stack and recursion depth limit
- Practical ML reference: Conceptual Decision Tree recursive binary splitting representation
"""

import sys

# ==========================================
# 1. Understanding Recursion & Factorial
# ==========================================
# Recursion requires:
# 1. Base Case: stops the recursive process (prevents infinite loop/StackOverflow).
# 2. Recursive Case: calls the function itself with modified arguments moving closer to the base case.

def compute_factorial(n):
    """
    Computes factorial of n recursively.
    Formula: n! = n * (n-1)!
    Base case: 0! or 1! = 1
    """
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    return n * compute_factorial(n - 1)

print("--- Basic Recursion: Factorial ---")
num = 5
print(f"Factorial of {num} is: {compute_factorial(num)}")  # 5 * 4 * 3 * 2 * 1 = 120

# ==========================================
# 2. Fibonacci Sequence Recursion
# ==========================================
# F(n) = F(n-1) + F(n-2)
# Base cases: F(0) = 0, F(1) = 1

def recursive_fibonacci(n):
    """
    Returns the n-th Fibonacci number.
    Note: This is O(2^N) - inefficient, but clean illustration of double recursion.
    """
    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive Case
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

print("\n--- Fibonacci Recursion ---")
n_terms = 7
print(f"The {n_terms}-th Fibonacci number is: {recursive_fibonacci(n_terms)}")

# ==========================================
# 3. Recursion Depth Limits
# ==========================================
# Python sets a recursion depth limit (typically 1000) to prevent stack overflow.

print("\n--- Recursion Depth limit ---")
print(f"Default recursion depth limit: {sys.getrecursionlimit()}")

# Uncommenting this will raise RecursionError:
# def infinite_recursion():
#     return infinite_recursion()
# infinite_recursion()

# ==========================================
# 4. Hands-on ML Concept: Recursive Tree Splitting
# ==========================================
# Decision Trees split datasets recursively based on logical conditions (like gini or entropy thresholds)
# until a stop condition (max depth, min samples) is reached.

def train_decision_tree_node(dataset, current_depth, max_depth=3):
    """
    Simulates training a decision tree node recursively.
    """
    indent = "  " * current_depth
    print(f"{indent}Checking Node at Depth {current_depth} with {len(dataset)} samples...")

    # Stop Condition (Base Case)
    if current_depth >= max_depth:
        print(f"{indent}---> Base Case met: Maximum Depth ({max_depth}) reached. Creating Leaf Node.")
        return

    # Simulate splitting the dataset into left and right branches
    mid = len(dataset) // 2
    left_split = dataset[:mid]
    right_split = dataset[mid:]

    print(f"{indent}Splitting node into Left ({len(left_split)}) and Right ({len(right_split)}) branches...")

    # Recursive steps: Train left and right sub-trees
    train_decision_tree_node(left_split, current_depth + 1, max_depth)
    train_decision_tree_node(right_split, current_depth + 1, max_depth)

print("\n--- Practical ML Concept: Decision Tree Training Simulation ---")
dummy_dataset = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9]
train_decision_tree_node(dummy_dataset, current_depth=0, max_depth=2)

"""
Key Takeaways:
- Every recursive function MUST have a base case to prevent stack overflow.
- Recursion utilizes the call stack where each call gets its own stack frame.
- While recursion makes logic code elegant, iterative solutions (using loops) are often faster and consume less memory.

Interview Relevance:
- Explain what happens if a recursive function does not have a base case. (It runs until the recursion depth limit is exceeded, throwing a RecursionError).
- What is the difference between direct and indirect recursion? (Direct: function calls itself directly. Indirect: function A calls function B, which calls function A).
- How do you increase the recursion limit in Python? (Use `sys.setrecursionlimit(limit)`).

AI/ML Relevance:
- Hierarchical models: Decision Trees partition features recursively.
- Graph Algorithms: Neural Network computational graph executions (like backpropagation) are recursively traversed.
- NLP structures: Parse trees for sentence parsing and grammatical analysis utilize recursive grammars.
"""
