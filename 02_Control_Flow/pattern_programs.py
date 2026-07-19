"""
Topic:
Pattern Programs using Nested Loops

Importance:
Pattern programs are classic placement screening challenges.
They test your spatial logic, index manipulation, nested loop mastery,
and granular control over console layouts.

This file covers:
- Pattern 1: Right-Angled Triangle of Stars
- Pattern 2: Inverted Right-Angled Triangle
- Pattern 3: Pyramid / Equilateral Triangle Pattern
- Pattern 4: Number Triangle
- Pattern 5: Matrix Grid / Multi-dimensional indexing (ML concept link)
"""

# ==========================================
# Pattern 1: Right-Angled Triangle of Stars
# ==========================================
# *
# * *
# * * *
# * * * *
print("--- Pattern 1: Right-Angled Triangle ---")
n = 4  # Number of rows
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # Newline after each row

# ==========================================
# Pattern 2: Inverted Right-Angled Triangle
# ==========================================
# * * * *
# * * *
# * *
# *
print("\n--- Pattern 2: Inverted Right-Angled Triangle ---")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# ==========================================
# Pattern 3: Pyramid / Equilateral Triangle
# ==========================================
#    *
#   * *
#  * * *
# * * * *
print("\n--- Pattern 3: Pyramid Pattern ---")
for i in range(1, n + 1):
    # Print leading spaces
    for space in range(n - i):
        print(" ", end="")
    # Print stars separated by space
    for star in range(i):
        print("*", end=" ")
    print()

# ==========================================
# Pattern 4: Number Triangle
# ==========================================
# 1
# 1 2
# 1 2 3
# 1 2 3 4
print("\n--- Pattern 4: Number Triangle ---")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# ==========================================
# Pattern 5: Matrix Grid (Practical Index Mapping)
# ==========================================
# Generating a 2D coordinate grid (X, Y coordinates)
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
print("\n--- Pattern 5: Coordinate Index Grid ---")
rows = 3
cols = 3
for r in range(rows):
    for c in range(cols):
        print(f"({r},{c})", end=" ")
    print()

"""
Key Takeaways:
- Outer loop generally controls the rows; inner loop(s) control the columns/elements in each row.
- `print(..., end=" ")` overrides the default newline, enabling printing on the same row.
- Mathematical functions or step-parameters (like range(n, 0, -1)) help control descending patterns.

Interview Relevance:
- Interviewers use pattern tasks to test if a candidate can convert a visual matrix pattern into clean loop logic.
- Pay attention to off-by-one errors in range() limits.
- How can you construct a string-based pyramid using multiplication? (E.g., `print(" " * (n - i) + "* " * i)`). This is a great Python-specific shortcut!

AI/ML Relevance:
- 2D coordinate generation is essential when processing pixels in images (e.g. convolution kernels shifting across width and height grids).
- Meshgrids: When visualizing classification decision boundaries, ML engineers construct grids of inputs using nested loop concepts (though optimized using NumPy's `meshgrid`).
"""
