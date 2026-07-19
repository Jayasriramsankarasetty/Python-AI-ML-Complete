"""
Topic:
Computational Complexity Classes (Big-O Examples)

Importance:
Analyzing time complexity enables software developers and data engineers to write algorithms
that scale efficiently. It is a mandatory screening filter in technical coding assessments.

This file covers:
- O(1) Constant Time
- O(log N) Logarithmic Time (Binary Search step demo)
- O(N) Linear Time (Single loop scan)
- O(N log N) Linearithmic Time (Built-in Sort)
- O(N^2) Quadratic Time (Nested loops pairs scan)
- O(2^N) Exponential Time (Double branch recursive Fibonacci)
"""

import time
import math

# ==========================================
# 1. O(1) Constant Time
# ==========================================
# Time taken is independent of input size N.

def constant_access(data_list):
    # Accessing first element or lookup is O(1)
    step_count = 1
    return data_list[0], step_count

# ==========================================
# 2. O(log N) Logarithmic Time
# ==========================================
# Input size N is divided by a constant factor (usually 2) at each step.

def binary_search_steps(n):
    # Simulates binary search dividing target search space
    steps = 0
    temp = n
    while temp > 1:
        temp //= 2
        steps += 1
    return steps

# ==========================================
# 3. O(N) Linear Time
# ==========================================
# Time taken increases proportionally with N.

def linear_scan(n):
    steps = 0
    for i in range(n):
        steps += 1
    return steps

# ==========================================
# 4. O(N log N) Linearithmic Time
# ==========================================
# Happens when sorting arrays (using Merge Sort or Heap Sort).
# We simulate N operations, each taking log N steps.

def linearithmic_simulation(n):
    steps = 0
    for i in range(n):
        # Nested loop runs log(N) times
        k = n
        while k > 1:
            k //= 2
            steps += 1
    return steps

# ==========================================
# 5. O(N^2) Quadratic Time
# ==========================================
# Time taken increases quadratically with N (nested loops over N).

def quadratic_pairs(n):
    steps = 0
    for i in range(n):
        for j in range(n):
            steps += 1
    return steps

# ==========================================
# 6. O(2^N) Exponential Time
# ==========================================
# Growth doubles with each addition to input size N.
# Represented by naive recursive Fibonacci.

def recursive_fibonacci(n, steps_dict):
    steps_dict["count"] += 1
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1, steps_dict) + recursive_fibonacci(n - 2, steps_dict)

# ==========================================
# Execution & Complexity Comparison Benchmark
# ==========================================
if __name__ == "__main__":
    # Test input sizes
    test_n = 10
    mock_list = list(range(test_n))
    
    print(f"=== COMPLEXITY METRIC STEPS FOR N = {test_n} ===")
    
    # 1. O(1)
    res_val, steps_o1 = constant_access(mock_list)
    print(f"O(1) Constant Access Steps: {steps_o1}")
    
    # 2. O(log N)
    steps_olog = binary_search_steps(test_n)
    print(f"O(log N) Logarithmic steps: {steps_olog}")
    
    # 3. O(N)
    steps_on = linear_scan(test_n)
    print(f"O(N) Linear scan steps: {steps_on}")
    
    # 4. O(N log N)
    steps_onlog = linearithmic_simulation(test_n)
    print(f"O(N log N) Linearithmic steps: {steps_onlog}")
    
    # 5. O(N^2)
    steps_on2 = quadratic_pairs(test_n)
    print(f"O(N^2) Quadratic pairs steps: {steps_on2}")
    
    # 6. O(2^N)
    fib_steps = {"count": 0}
    recursive_fibonacci(test_n, fib_steps)
    print(f"O(2^N) Exponential recursive steps: {fib_steps['count']}")
    
    print("\n=== COMPARING COMPUTATIONAL GROWTH SCALES ===")
    sizes = [10, 100, 1000]
    for size in sizes:
        print(f"Input Size (N): {size}")
        print(f"  O(1)   -> 1 step")
        print(f"  O(logN)-> {math.ceil(math.log2(size))} steps")
        print(f"  O(N)   -> {size} steps")
        print(f"  O(N^2) -> {size ** 2} steps")
        # O(2^N) for 100 exceeds universe scale (30 digits), so we skip calculating it for large size
        if size <= 20:
            print(f"  O(2^N) -> {2 ** size} steps")
        print()

"""
Key Takeaways:
- Time complexity is an approximation of operations growth, not exact cpu runtime seconds.
- O(log N) is extremely fast and scales exceptionally well to billions of records.
- Avoid nesting loops unless necessary, as nesting O(N) loops yields O(N^2), which slows down for inputs > 10,000.

Interview Relevance:
- Be prepared to trace loop execution bounds to calculate Big-O complexity.
- How do you optimize an O(N^2) problem? (Look for O(N log N) sorting approaches or O(N) checks using auxiliary sets/dictionaries for O(1) lookups).
- What is the complexity of sorting an array? (O(N log N) average/worst case).

AI/ML Relevance:
- Deep Learning Operations: Forward pass convolutions across width W and height H of images run in O(W * H) per layer.
- Recommendation Systems: Pairwise distance checks (like cosine similarity) across M users and N movies scales as O(M * N), requiring indexing optimizations (like FAISS) to search in O(log M) time.
"""
