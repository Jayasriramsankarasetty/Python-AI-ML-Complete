"""
Topic:
Advanced NumPy Operations: Vectorization, Broadcasting, Masking, and Matrix Multiplication

Importance:
AI/ML models (like Neural Networks) propagate matrices of features and weight parameters.
Replacing nested loops with vectorized broadcast math and matrix dot products speeds up
calculations by multiple orders of magnitude.

This file covers:
- Vectorization performance comparison (loops vs np.dot)
- Broadcasting rules and examples
- Boolean Indexing & Masking
- Array Reshaping & Transposing
- Matrix Multiplication (dot, @ operator)
"""

import numpy as np
import time

# ==========================================
# 1. Loop vs Vectorization Benchmarking
# ==========================================
print("--- Loop vs Vectorization Benchmarking ---")
size = 1000000
a = np.random.rand(size)
b = np.random.rand(size)

# Loop calculation (Dot product)
start_time = time.perf_counter()
dot_loop = 0
for i in range(size):
    dot_loop += a[i] * b[i]
loop_duration = time.perf_counter() - start_time
print(f"Loop dot product:        {dot_loop:.4f} | Time taken: {loop_duration:.6f} seconds")

# Vectorized NumPy calculation
start_time = time.perf_counter()
dot_vectorized = np.dot(a, b)
vectorized_duration = time.perf_counter() - start_time
# Protect against division by zero
speedup = loop_duration / max(vectorized_duration, 1e-9)
print(f"Vectorized dot product:  {dot_vectorized:.4f} | Time taken: {vectorized_duration:.6f} seconds")
print(f"Speedup Factor:          {speedup:.2f}x faster!")

# ==========================================
# 2. Broadcasting
# ==========================================
print("\n--- Broadcasting ---")
# Broadcasting allows NumPy to perform arithmetic on arrays of different shapes.
# Criteria: Two dimensions are compatible if:
# 1. They are equal, OR
# 2. One of them is 1.

# Example: Adding a scalar (shape: ()) to a 1D array (shape: (3,))
arr_1 = np.array([1, 2, 3])
print("Array:", arr_1)
print("Array + 10 (Scalar Broadcast):", arr_1 + 10)  # [11, 12, 13]

# Example: Adding a 1D row vector (shape: (3,)) to a 2D matrix (shape: (2, 3))
matrix_2d = np.array([[10, 20, 30], [40, 50, 60]])
row_vector = np.array([1, 2, 3])
print("Matrix:\n", matrix_2d)
print("Row vector:", row_vector)
# row_vector is stretched to shape (2, 3) to match matrix_2d
print("Matrix + Row Vector:\n", matrix_2d + row_vector)

# ==========================================
# 3. Boolean Indexing & Masking
# ==========================================
print("\n--- Boolean Masking ---")
data = np.array([[5, 12, 8], [21, 3, 14]])
print("Data:\n", data)

# Check elements > 10
mask = data > 10
print("Boolean Mask (element > 10):\n", mask)

# Filter elements using the mask
filtered_data = data[mask]
print("Filtered elements (flattened):", filtered_data)

# In-place substitution using mask: Cap all values > 10 to 10
data[data > 10] = 10
print("Data capped at 10:\n", data)

# ==========================================
# 4. Reshaping & Transposing
# ==========================================
print("\n--- Reshaping & Transposing ---")
flat_arr = np.arange(12)  # [0, 1, 2, ..., 11] (shape (12,))
print("Flat array:", flat_arr)

# Reshape to 3 rows and 4 columns
matrix_3x4 = flat_arr.reshape(3, 4)
print("Reshaped 3x4 matrix:\n", matrix_3x4)

# Reshape using -1 (infer dimension automatically)
matrix_2x6 = flat_arr.reshape(2, -1)  # row size 2, NumPy computes column size as 6
print("Reshaped 2x6 matrix:\n", matrix_2x6)

# Transposing a matrix (swap rows and columns)
transposed_matrix = matrix_3x4.T
print("Transposed 4x3 matrix:\n", transposed_matrix)  # shape becomes (4, 3)

# ==========================================
# 5. Matrix Multiplication
# ==========================================
print("\n--- Matrix Multiplication ---")
# Let A be a 2x3 matrix, and B be a 3x2 matrix
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

print("A Shape:", A.shape, " | B Shape:", B.shape)

# Dot product / Matrix multiplication:
# Method A: np.dot
dot_res = np.dot(A, B)
# Method B: @ operator (standard Python operator since 3.5)
matmul_res = A @ B

print("Matrix multiplication output:\n", matmul_res)
print("Output Shape:", matmul_res.shape)  # expected (2, 2)

"""
Key Takeaways:
- NumPy vectorization pushes loop math down to low-level C compilation routines, executing 100x+ faster than Python loops.
- Broadcasting stretches dimensions of size 1 to match the sizes of adjacent arrays.
- Boolean indexing allows selecting and editing subset slices without writing filter loops.
- Reshape returns a view of the array; passing -1 lets NumPy automatically calculate one dimension.
- Matrix multiplication requires matched inner dimensions: `(M x N) @ (N x P) -> M x P`. Use `A @ B` or `np.dot(A, B)`.

Interview Relevance:
- What is broadcasting? (It is the mechanism that allows NumPy to work with arrays of different shapes during arithmetic operations. The smaller array is broadcast across the larger array so they have compatible shapes).
- Difference between `*` and `@` in NumPy? (The asterisk `*` performs element-wise multiplication. The `@` operator or `np.dot` performs standard matrix dot product multiplication).
- What does `.reshape(2, -1)` mean? (Tells NumPy to reshape the array to have 2 rows, and automatically compute the required number of columns to fit the size).

AI/ML Relevance:
- Fully Connected Layers: Dense layers in deep learning calculate forward activations as `Z = X @ W + b`, where X is features, W is weights, and b is bias vector broadcasted.
- Activation Functions: Applying Relu thresholding is implemented as a boolean mask `X[X < 0] = 0`.
"""
