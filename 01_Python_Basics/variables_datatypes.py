"""
Topic:
Variables and Datatypes in Python

Importance:
Variables are fundamental storage units. Understanding data types is critical
for structured programming, data preprocessing, and setting up parameters in ML pipelines.

This file covers:
- Python dynamic typing & variable naming rules
- Basic built-in datatypes: Integer, Float, String, Boolean
- Multiple assignments and type inference
- Storing machine learning hyperparameters as a practical example
"""

# ==========================================
# 1. Defining Variables & Dynamic Typing
# ==========================================

# Python is dynamically typed. We don't need to declare variable types.
# The type is determined automatically at runtime when a value is assigned.

model_name = "RandomForestClassifier"  # String (str)
epochs = 100                            # Integer (int)
learning_rate = 0.01                    # Float (float)
is_gpu_enabled = True                   # Boolean (bool)

# Let's inspect their types using type()
print("--- Types of Variables ---")
print("model_name type:", type(model_name))
print("epochs type:", type(epochs))
print("learning_rate type:", type(learning_rate))
print("is_gpu_enabled type:", type(is_gpu_enabled))

# Dynamic typing allows us to change the type of a variable by reassigning it
learning_rate = "High"  # Now learning_rate is a string
print("\nReassigned learning_rate type:", type(learning_rate))

# Resetting it back to float for further examples
learning_rate = 0.01

# ==========================================
# 2. Variable Naming Conventions (PEP 8)
# ==========================================
# Rules for valid variable names:
# - Must start with a letter or underscore (_)
# - Can contain letters, numbers, and underscores (a-z, A-Z, 0-9, _)
# - Cannot start with a number
# - Case-sensitive (model_name and Model_Name are different)
# - Cannot use reserved keywords (e.g., if, else, for, True)

# Valid names:
batch_size = 32         # Snake case (recommended for Python variables)
_temp_val = 0.5         # Starts with underscore (often used for internal variables)
features2d = True       # Numbers are allowed but not at the start

# Invalid names (Uncommenting these will raise SyntaxError):
# 2d_features = True
# model-name = "SVM"
# for = 5

# ==========================================
# 3. Multiple Assignments
# ==========================================
# Assigning different values to multiple variables in a single line
x, y, z = 10, 20, 30
print(f"\nMultiple Assignments: x = {x}, y = {y}, z = {z}")

# Assigning the same value to multiple variables
accuracy = val_accuracy = 0.95
print(f"Same value: accuracy = {accuracy}, val_accuracy = {val_accuracy}")

# ==========================================
# 4. Hands-on ML Use-Case: Model Config
# ==========================================
# Imagine configuring a neural network training run
print("\n--- Practical ML Configuration Example ---")
dataset_path = "data/housing.csv"
num_samples = 15000
train_test_split_ratio = 0.8
normalization_active = True

# Printing information with basic string concatenation / formatting
print("Training Dataset Path: " + dataset_path)
print("Total number of dataset samples:", num_samples)
print("Percentage of training data:", train_test_split_ratio * 100, "%")
print("Is input normalization active?", normalization_active)

"""
Key Takeaways:
- Variables do not need declaration; they are created when assigned a value.
- Python is dynamically typed, meaning a variable's type can change during execution.
- PEP 8 recommends using 'snake_case' (all lowercase separated by underscores) for variable names.
- The type() function is used to inspect the class/datatype of any value or variable.

Interview Relevance:
- Explain dynamic typing and how Python manages memory references.
- Discuss the rules of variable naming and PEP 8 guidelines.
- What is the output of checking the type of a variable that hasn't been defined? (NameError)

AI/ML Relevance:
- Hyperparameter tuning: In ML/DL pipelines, configuration parameters (like learning rates, optimizer states, epoch counts) are stored as variables.
- Knowing the datatype (e.g. converting inputs to floats for neural nets) is essential to avoid shape and dtype runtime crashes in NumPy and PyTorch.
"""
