"""
Topic:
Generators in Python

Importance:
Generators are simple syntax tools to write iterators.
By using the 'yield' keyword, a generator returns an element, pauses execution,
and resumes right where it left off on next() calls.
This allows processing infinite streams or multi-gigabyte files with a memory footprint of O(1).

This file covers:
- Generator functions vs standard functions
- The yield keyword
- Generator Expressions (using parentheses ())
- Profiling memory benefits
- Practical ML application: Memory-safe dataset streaming generator
"""

import sys

# ==========================================
# 1. Generator Functions & Yield
# ==========================================
# A normal function finishes completely and returns a single value.
# A generator pauses its state and yields multiple values over time.

def count_up_to(limit):
    print("Generator activated...")
    count = 1
    while count <= limit:
        # yield returns value and suspends execution state
        yield count
        count += 1
    print("Generator completed.")

print("--- Testing Generator Function ---")
# Calling generator function does NOT run the code; it returns a generator object!
counter = count_up_to(3)
print("Generator Object:", counter)

# Run generator using next()
print("First next():", next(counter))
print("Second next():", next(counter))
print("Third next():", next(counter))

# Next call raises StopIteration
# print(next(counter))

# ==========================================
# 2. Generator Expressions
# ==========================================
# Like list comprehensions, but with round brackets () instead of square brackets [].
# They yield values lazily instead of instantiating lists in memory.

print("\n--- Generator Expressions ---")
# List comprehension (creates list of squares in memory immediately)
list_squares = [x ** 2 for x in range(1000)]

# Generator expression (creates generator object immediately, squares computed on demand)
gen_squares = (x ** 2 for x in range(1000))

print(f"Memory size of List Comprehension: {sys.getsizeof(list_squares)} bytes")
print(f"Memory size of Generator Expression: {sys.getsizeof(gen_squares)} bytes")

# ==========================================
# 3. Hands-on ML Use-Case: Memory-Safe Dataset Line Streamer
# ==========================================
# When preprocessing text corpus files that are too large for RAM (e.g. 5GB texts),
# generators yield lines one by one.
print("\n--- Practical ML Use-Case: Large Dataset Streamer ---")

# Step 1: Create a mock large dataset file
mock_dataset_path = "mock_text_corpus.txt"
with open(mock_dataset_path, "w") as file:
    file.write("line 1: natural language processing patterns\n")
    file.write("line 2: recurrent neural networks training\n")
    file.write("line 3: transformer architectures pre-training\n")

# Step 2: Define generator function to stream text lines
def stream_dataset_lines(filepath):
    with open(filepath, "r") as file:
        for line in file:
            # Yield clean tokens list per line
            yield line.strip().lower().split()

print("Streaming cleaned tokens line-by-line:")
streamer = stream_dataset_lines(mock_dataset_path)

for idx, tokens in enumerate(streamer):
    print(f"  Line {idx + 1} processed tokens: {tokens}")

"""
Key Takeaways:
- Generators are built using functions containing `yield` or using parentheses `()`.
- They save state automatically, resuming execution when `next()` is called.
- Generators are memory-efficient: they consume O(1) memory, making them perfect for streaming large datasets.

Interview Relevance:
- What is the difference between `yield` and `return`? (`return` terminates the function and returns a value; `yield` returns a value, pauses the function execution, and retains local state for subsequent calls).
- What is a generator expression? (An inline generator syntax: `(expression for item in iterable)`).
- Why are generators useful in Python? (They provide a simple way to create iterators, saving memory by generating elements lazily on demand).

AI/ML Relevance:
- Large Text Corpora: When training LLMs (like GPT structures), corpus documents are streamed dynamically from disk using custom text line generators.
- Custom Image Batch loaders: Reading image files from disk one-by-one to prepare training batches utilizes generator yield mechanisms.
"""
