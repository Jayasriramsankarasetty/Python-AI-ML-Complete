"""
Topic:
Typecasting (Type Conversion) in Python

Importance:
Python is strongly and dynamically typed. It does not allow operations on incompatible types
(e.g., adding a string and an integer) without explicit conversion. Understanding how to typecast
values is critical when loading dirty datasets, reading API request bodies, or preparing tensors for ML.

This file covers:
- Implicit Typecasting (automatic conversion by Python)
- Explicit Typecasting (using int(), float(), str(), bool())
- Boolean typecasting / understanding Truthy and Falsy values
- Practical ML context: Converting raw text label outputs into numerical target columns
"""

# ==========================================
# 1. Implicit Typecasting
# ==========================================
# Python automatically converts one data type to another if it's safe to prevent data loss.

int_val = 10     # int
float_val = 5.5  # float

# Adding an int and a float implicitly promotes the result to float
result = int_val + float_val
print("--- Implicit Typecasting ---")
print(f"Value: {result} | Type: {type(result)}")

# ==========================================
# 2. Explicit Typecasting
# ==========================================
# Manually converting variables to a desired type using built-in constructors.

print("\n--- Explicit Typecasting ---")

# A. String to Integer/Float
raw_sample_count = "150"
raw_learning_rate = "0.001"

# Converting to numerical formats
sample_count = int(raw_sample_count)
learning_rate = float(raw_learning_rate)

print(f"sample_count: {sample_count} | Type: {type(sample_count)}")
print(f"learning_rate: {learning_rate} | Type: {type(learning_rate)}")

# B. Numeric to String
id_number = 10134
string_id = str(id_number)
print(f"string_id: '{string_id}' | Type: {type(string_id)}")

# C. Handling conversion errors (Uncommenting this will raise ValueError)
# invalid_numeric_str = "12.34abc"
# val = float(invalid_numeric_str)

# ==========================================
# 3. Boolean Conversion (Truthy & Falsy)
# ==========================================
# Any value can be evaluated to a boolean.
# "Falsy" values in Python:
# - None
# - False
# - 0, 0.0 (Numeric zeros)
# - Empty sequences/collections: '', [], (), {}, set()
# Everything else evaluates to True ("Truthy").

print("\n--- Boolean Casting (Truthy / Falsy) ---")
print("bool(1) ->", bool(1))
print("bool(0) ->", bool(0))
print("bool('Hello') ->", bool("Hello"))
print("bool('') ->", bool(""))  # Empty string
print("bool([]) ->", bool([]))  # Empty list
print("bool(None) ->", bool(None))

# Practical application: Checking if a configuration dictionary is empty
model_config = {}  # Empty dictionary (evaluates to False)
if not model_config:
    print("Warning: Configuration is empty. Using defaults.")

# ==========================================
# 4. Hands-on ML Use-Case: Target Class Labeling
# ==========================================
# In classification, labels may initially be represented as strings or floats,
# but algorithms require them as specific numerical target representations.
print("\n--- Practical ML Use-Case ---")

raw_predictions = [0.99, 0.05, 0.88, 0.12]
binary_threshold = 0.5

# Convert probabilities to boolean flags (True = class 1, False = class 0)
binary_flags = [prob >= binary_threshold for prob in raw_predictions]
print("Predictions above threshold (Booleans):", binary_flags)

# Convert boolean flags to standard integer labels (1 or 0) for training loops
integer_labels = [int(flag) for flag in binary_flags]
print("Casted Target Integer Labels (0 or 1):", integer_labels)

"""
Key Takeaways:
- Implicit typecasting is done automatically (e.g. promoting int to float).
- Explicit typecasting is manual (int(), float(), str(), bool(), list(), set()).
- All objects in Python have a truth value (Truthy vs Falsy). 0, None, and empty structures are Falsy.

Interview Relevance:
- What is the difference between strongly typed and weakly typed languages? Python is strongly typed, so it won't implicitly cast incompatible types like "10" + 5.
- What are Falsy values in Python? (None, False, 0, 0.0, empty collections, empty strings).
- How do you convert a float string (e.g., "3.14") to an integer? (First cast to float: int(float("3.14"))).

AI/ML Relevance:
- PyTorch and TensorFlow require specific dtypes (e.g., float32 for model weights, int64 for target labels).
- Standard preprocessing often involves casting raw dataset string categories to integers using libraries like LabelEncoder or pandas astype().
"""
