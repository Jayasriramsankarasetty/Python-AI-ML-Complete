"""
Topic:
NumPy Array Basics

Importance:
Arrays (ndarrays) form the base datatypes of AI/ML. Understanding how to instantiate,
inspect attributes, index/slice segments, and perform statistical reductions is
mandatory for pre-processing feature arrays.

This file covers:
- Array creation methods (array, zeros, ones, arange, linspace)
- Key attributes (ndim, shape, dtype, size)
- Indexing & Slicing in 1D and 2D arrays
- Statistical reductions (mean, median, std, sum, min, max across axes)
"""

import numpy as np

# ==========================================
# 1. Array Creation Methods
# ==========================================
print("--- Array Creation Methods ---")

# From a Python list
arr_from_list = np.array([1, 2, 3, 4])
print("Array from list:", arr_from_list)

# Initialized with Zeros or Ones
zeros_arr = np.zeros(shape=(2, 3))  # 2D matrix of shape 2x3
ones_arr = np.ones(shape=(3, 2))
print("Zeros array:\n", zeros_arr)
print("Ones array:\n", ones_arr)

# Using arange (similar to Python's range)
arange_arr = np.arange(start=0, stop=10, step=2)  # [0, 2, 4, 6, 8]
print("Arange array:", arange_arr)

# Using linspace (linear spacing: N values evenly distributed between start and end)
linspace_arr = np.linspace(start=0, stop=1, num=5)  # [0.0, 0.25, 0.5, 0.75, 1.0]
print("Linspace array:", linspace_arr)

# ==========================================
# 2. Inspecting Array Attributes
# ==========================================
print("\n--- Array Attributes ---")
matrix_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)

print("Matrix:\n", matrix_2d)
print("Number of dimensions (ndim):", matrix_2d.ndim)  # expected 2
print("Shape of matrix (shape):     ", matrix_2d.shape) # expected (2, 3)
print("Data type of elements (dtype):", matrix_2d.dtype) # expected float32
print("Total number of elements (size):", matrix_2d.size) # expected 6

# ==========================================
# 3. Indexing & Slicing
# ==========================================
print("\n--- Indexing & Slicing ---")
# 1D array slicing
arr_1d = np.array([10, 20, 30, 40, 50])
print("1D slice s[1:4]:", arr_1d[1:4])  # [20, 30, 40]

# 2D matrix slicing: matrix[row_slice, col_slice]
# Matrix representation:
# [[10, 11, 12],
#  [20, 21, 22],
#  [30, 31, 32]]
arr_2d = np.array([[10, 11, 12], [20, 21, 22], [30, 31, 32]])

# Accessing a single element: row 1, col 2
print("Single element (row 1, col 2):", arr_2d[1, 2])  # 22

# Slicing: first 2 rows, last 2 columns
print("Sub-matrix (rows 0..1, cols 1..2):\n", arr_2d[:2, 1:])

# Fetching all elements of row index 0
print("Row 0 slice:", arr_2d[0, :])

# Fetching all elements of column index 1
print("Col 1 slice:", arr_2d[:, 1])

# ==========================================
# 4. Statistical Reductions (Across Axes)
# ==========================================
print("\n--- Statistical Reductions ---")
# Matrix:
# [[1, 2],
#  [3, 4]]
data = np.array([[1, 2], [3, 4]])

# Sum of entire array
print("Global Sum:", np.sum(data))  # 10

# Sum along axis 0 (downwards, column compressions)
# [1+3, 2+4] = [4, 6]
print("Sum along Axis 0 (Columns sum):", np.sum(data, axis=0))

# Sum along axis 1 (horizontal, row compressions)
# [1+2, 3+4] = [3, 7]
print("Sum along Axis 1 (Rows sum):   ", np.sum(data, axis=1))

# Mean, Median, and Standard Deviation
print("Global Mean: ", np.mean(data))
print("Global Median:", np.median(data))
print("Global StdDev:", np.std(data))

"""
Key Takeaways:
- NumPy arrays (`ndarrays`) are homogeneous (all elements have the same dtype).
- Slicing 2D arrays follows the `matrix[row_slice, col_slice]` syntax.
- Compression operations (like sum, mean) specify `axis=0` to compress columns, and `axis=1` to compress rows.

Interview Relevance:
- Why are NumPy arrays faster than Python lists? (NumPy allocates elements in contiguous memory blocks and uses homogenous datatypes to compile efficient C code, avoiding dynamic type lookup checks).
- What happens when you slice a NumPy array? (It returns a *view* of the original array rather than a copy, meaning editing the slice edits the original array. Use `arr.copy()` to force copying).
- Explain axis parameter: What does `axis=0` calculate in a 2D matrix? (Calculates operations vertically down columns).

AI/ML Relevance:
- Dataset Slicing: Separating a dataset matrix into features `X` and labels `y` uses column slicing (`X = dataset[:, :-1]`, `y = dataset[:, -1]`).
- Normalization: Calculating column means and standard deviations to scale input data is done via `np.mean(X, axis=0)`.
"""
