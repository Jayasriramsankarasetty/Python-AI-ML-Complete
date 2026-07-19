"""
Topic:
Operators in Python

Importance:
Operators perform logical, arithmetic, comparison, and identity checks.
They are essential for evaluating model metrics, data filtering, math formulas (e.g., loss calculations), and control flow.

This file covers:
- Arithmetic Operators (+, -, *, /, //, %, **)
- Comparison/Relational Operators (==, !=, >, <, >=, <=)
- Logical Operators (and, or, not)
- Assignment Operators (=, +=, -=, *=, /=)
- Identity Operators (is, is not)
- Membership Operators (in, not in)
- Bitwise Operators (brief introduction)
"""

# ==========================================
# 1. Arithmetic Operators
# ==========================================
# Used for mathematical operations. Let's calculate a simple MSE-like loss component.
y_actual = 10.0
y_predicted = 8.5

diff = y_actual - y_predicted           # Subtraction
squared_diff = diff ** 2                 # Exponentiation (power of 2)
print("--- Arithmetic Operators ---")
print("Difference:", diff)
print("Squared Difference:", squared_diff)

# Floating point vs Floor division
a = 15
b = 4
div = a / b                             # Normal Division (float result)
floor_div = a // b                       # Floor Division (ignores decimal fraction)
remainder = a % b                        # Modulus (returns remainder)
print(f"Division: {a} / {b} = {div}")
print(f"Floor Division: {a} // {b} = {floor_div}")
print(f"Modulus (Remainder): {a} % {b} = {remainder}")

# ==========================================
# 2. Comparison/Relational Operators
# ==========================================
# Returns Boolean (True or False)
threshold_accuracy = 0.90
model_a_accuracy = 0.92
model_b_accuracy = 0.88

print("\n--- Comparison Operators ---")
print("Is Model A better than threshold?", model_a_accuracy > threshold_accuracy)
print("Is Model B better than threshold?", model_b_accuracy > threshold_accuracy)
print("Do both models have equal accuracy?", model_a_accuracy == model_b_accuracy)
print("Is Model A's accuracy not equal to Model B's?", model_a_accuracy != model_b_accuracy)

# ==========================================
# 3. Logical Operators
# ==========================================
# Combines conditional statements
is_accuracy_high = model_a_accuracy >= 0.90
is_latency_low = True

# and: True if both conditions are True
# or: True if at least one condition is True
# not: Reverses the state
deploy_model = is_accuracy_high and is_latency_low
print("\n--- Logical Operators ---")
print("Deploy Model (accuracy >= 90% AND latency low):", deploy_model)
print("Should we flag model for review (accuracy < 90% OR latency high)?", not is_accuracy_high or not is_latency_low)

# ==========================================
# 4. Assignment Operators
# ==========================================
# Used to assign values to variables, often combining arithmetic
print("\n--- Assignment Operators ---")
epoch_count = 0
epoch_count += 1   # Equivalent to: epoch_count = epoch_count + 1
print("Epoch count after += 1:", epoch_count)

learning_rate = 0.1
learning_rate *= 0.5  # Decay learning rate by half
print("Decayed learning rate after *= 0.5:", learning_rate)

# ==========================================
# 5. Identity & Membership Operators
# ==========================================
# Identity (is / is not): Checks if variables refer to the exact same object in memory
# Membership (in / not in): Checks if a value is present in a sequence (string, list, etc.)

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print("\n--- Identity & Membership Operators ---")
print("Are list_a and list_b identical in memory?", list_a is list_b)  # False, they are different objects with same content
print("Are list_a and list_c identical in memory?", list_a is list_c)  # True, they point to same memory address

# Membership check
selected_features = ["age", "income", "education"]
target_feature = "income"
unwanted_feature = "id"

print(f"Is '{target_feature}' in selected features?", target_feature in selected_features)
print(f"Is '{unwanted_feature}' not in selected features?", unwanted_feature not in selected_features)

# ==========================================
# 6. Bitwise Operators (Bonus Interview Prep)
# ==========================================
# Works on binary representation of integers
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift)
n1 = 5  # Binary: 0101
n2 = 3  # Binary: 0011

print("\n--- Bitwise Operators ---")
print("Bitwise AND (5 & 3):", n1 & n2)  # Binary 0001 -> Decimal 1
print("Bitwise OR (5 | 3):", n1 | n2)   # Binary 0111 -> Decimal 7

"""
Key Takeaways:
- Comparison operators return Booleans (True/False).
- '//' returns the floored quotient, whereas '%' returns the remainder.
- 'is' checks for memory identity (address), whereas '==' checks for value equality.
- 'in' is highly optimized for checking presence in structures like sets and dicts, and is used extensively in data filtering.

Interview Relevance:
- What is the difference between '==' and 'is'? ('==' checks values, 'is' checks reference identity/memory address).
- Explain the behavior of short-circuit evaluation in logical 'and' / 'or'.
- How do logical operators 'and', 'or', 'not' behave with non-Boolean operands (truthy and falsy values)?

AI/ML Relevance:
- Membership checking is constantly used to verify if training files exist or if feature columns exist in data frames.
- Exponentiation (**) is used for math formulas like standard deviation, Euclidean distance, and error metrics.
- Identity check 'is None' is standard in Python for optional arguments (e.g., if random_state is None).
"""
