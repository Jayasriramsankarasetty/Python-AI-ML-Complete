"""
Topic:
Modules and Packages in Python

Importance:
A module is a file containing Python definitions and statements. A package is a collection of modules.
ML pipelines import external packages (like NumPy, Pandas, Scikit-Learn) and built-in libraries
to structure directories, initialize random seeds, and compute math formulas.

This file covers:
- Importing entire modules (import math)
- Importing specific functions (from random import shuffle)
- Importing modules with aliases (import os as system_os)
- Structural package layout concept (the role of __init__.py)
- Practical ML application: Splitting a dataset using 'random' and computing metrics using 'math'
"""

# ==========================================
# 1. Importing Techniques
# ==========================================

# A. Importing entire module
import math
print("--- Standard Module Import ---")
print("Math Pi constant value:", math.pi)
print("Square root of 16:", math.sqrt(16))

# B. Importing specific functions (saves typing, loads only required namespace objects)
from random import shuffle, seed
print("\n--- Importing Specific Functions ---")
data_points = [10, 20, 30, 40, 50]
seed(42)  # Set seed for reproducible random outputs (crucial in ML)
shuffle(data_points)
print("Shuffled data list (seeded):", data_points)

# C. Importing modules with an alias (custom short-names)
import os as system_os
print("\n--- Aliased Imports ---")
# Get current working directory pathway
current_directory = system_os.getcwd()
print("Current directory:", current_directory)

# ==========================================
# 2. Package Structures (__init__.py)
# ==========================================
# A Package is a directory containing multiple sub-directories and modules.
# Structure example:
# my_ml_package/
#   ├── __init__.py      <-- Marks directory as an importable package (can be empty, or used for initializing package variables)
#   ├── preprocessing.py
#   └── modeling.py
#
# Import syntax: from my_ml_package.preprocessing import scale_features

# ==========================================
# 3. Hands-on ML Use-Case: Train-Test Split Simulator
# ==========================================
# Let's combine 'random' and 'math' modules to execute a raw 80-20 train-test split of a dataset.
print("\n--- Practical ML Use-Case: Random Data Splitting ---")

from random import sample

# Generate a mock dataset of 20 samples
raw_dataset = [f"sample_{i}" for i in range(1, 21)]
print(f"Original dataset (size {len(raw_dataset)}):\n  {raw_dataset}")

# Define split percentage
train_ratio = 0.8
num_train_samples = math.floor(len(raw_dataset) * train_ratio)  # 20 * 0.8 = 16

# Randomly sample indices for training set
seed(101)  # Set seed for reproducibility
train_set = sample(raw_dataset, num_train_samples)

# Test set contains items not selected for training
test_set = [item for item in raw_dataset if item not in train_set]

print(f"\nAfter Splitting (Seeded random sampling):")
print(f"  Training Set (Size {len(train_set)}):\n    {train_set}")
print(f"  Testing Set (Size {len(test_set)}):\n    {test_set}")

"""
Key Takeaways:
- A module is a single `.py` file; a package is a directory of modules.
- Use `from module import function` to call functions directly without using module name prefix.
- `import module as alias` shortens module calls.
- Historical check: Python 3.3+ no longer strictly requires `__init__.py` to recognize namespace packages, but it is still best practice for package initialization and backward compatibility.

Interview Relevance:
- What is the difference between a module and a package? (A module is a single Python file; a package is a folder containing a collection of modules and optionally an `__init__.py` file).
- How do you check all variables/functions defined in a module? (Use the `dir(module_name)` function).
- What does setting a random seed do in ML? (It locks the random number generator's initial state, making random functions like shuffle or sample return identical outputs on every run, ensuring reproducibility).

AI/ML Relevance:
- Reproducibility: ML code blocks begin by setting random seeds (`random.seed()`, `np.random.seed()`, `torch.manual_seed()`) to lock training iterations.
- Paths handling: Saving checkpoints requires joining folder paths safely using `os.path.join` to avoid platform-specific backslash/forward slash errors between Windows, macOS, and Linux servers.
"""
