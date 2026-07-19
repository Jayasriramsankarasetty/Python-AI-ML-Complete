# Numerical Python (NumPy) Guide

NumPy is the foundational library for scientific computing in Python. It provides a high-performance multidimensional array object (`ndarray`) and tools for working with these arrays. In AI and Machine Learning, almost all calculations (like weight updates, image matrices, and loss equations) rely on NumPy.

---

## Why is NumPy faster than standard Python Lists?

Standard Python lists can store elements of different datatypes. This flexibility requires Python to store type descriptors and reference pointers in memory for every element, adding significant overhead.
NumPy arrays are faster because:
1. **Contiguous Memory Allocation**:
   * Elements are stored side-by-side in memory. This improves cache localization and speeds up sequential reads.
2. **Homogenous Datatypes**:
   * All elements in an array have the same type, allowing CPU vector registers to apply SIMD (Single Instruction Multiple Data) calculations directly.
3. **No Overhead**:
   * Avoids type checking loops during execution.

---

## Axis Orientation

Understanding axes is crucial for matrix reduction operations (like summing values across rows or columns):
* **Axis 0 (Rows)**:
   * Directs vertically downwards. Running `np.sum(arr, axis=0)` compresses columns, outputting a value per column.
* **Axis 1 (Columns)**:
   * Directs horizontally to the right. Running `np.sum(arr, axis=1)` compresses rows, outputting a value per row.

---

## Files in this Folder

1. [numpy_basics.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/09_Python_Libraries_For_AI_ML/NumPy/numpy_basics.py):
   * Creating arrays, attributes (`shape`, `ndim`, `dtype`), indexing, and statistical operations.
2. [numpy_advanced.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/09_Python_Libraries_For_AI_ML/NumPy/numpy_advanced.py):
   * Speed benchmarks (loops vs vectorization), broadcasting rules, boolean masking, reshapes, and matrix multiplications.
