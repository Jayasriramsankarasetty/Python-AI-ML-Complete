"""
Topic:
Conditional Statements (if-elif-else) in Python

Importance:
Conditional branching is essential for control logic, model decision thresholds,
validating parameters, and checking learning progress (like early stopping).

This file covers:
- Python indentation rules
- Basic if-elif-else syntax
- Nested conditionals
- Ternary operator (conditional expression)
- Practical ML application: Binary threshold classification and early stopping check
"""

# ==========================================
# 1. Indentation Rules & Basic Syntax
# ==========================================
# Python relies on indentation (typically 4 spaces) instead of curly braces {} to define scopes.
# A block starts with a colon (:) and must be consistently indented.

score = 85

print("--- Basic Conditional Checks ---")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")

# ==========================================
# 2. Nested Conditionals
# ==========================================
# Placements and project logic often check multiple nested conditions.

is_placement_eligible = True
gpa = 7.8

print("\n--- Nested Conditionals ---")
if is_placement_eligible:
    print("Placement eligibility: Verified")
    if gpa >= 8.0:
        print("Candidate status: Recommended (High GPA)")
    else:
        print("Candidate status: Regular (Average GPA)")
else:
    print("Placement eligibility: Not Eligible")

# ==========================================
# 3. Ternary Operator (Conditional Expressions)
# ==========================================
# Syntactic shortcut: value_if_true if condition else value_if_false
# Very common in data science code for simple assignments.

threshold = 0.5
prediction_probability = 0.72

# Decide target class based on probability
predicted_class = 1 if prediction_probability >= threshold else 0
print("\n--- Ternary Operator ---")
print(f"Prediction Probability: {prediction_probability} -> Predicted Class: {predicted_class}")

# ==========================================
# 4. Hands-on ML Use-Case: Early Stopping Check
# ==========================================
# In deep learning, early stopping halts training when the validation loss stops improving.
print("\n--- Practical ML Use-Case: Early Stopping ---")

best_val_loss = 0.2450
current_val_loss = 0.2485
patience_counter = 2
patience_limit = 3

print(f"Best Loss: {best_val_loss:.4f} | Current Loss: {current_val_loss:.4f}")

# Check if validation loss improved
if current_val_loss < best_val_loss:
    print("Validation loss improved! Saving model checkpoint...")
    best_val_loss = current_val_loss
    patience_counter = 0  # Reset patience
else:
    patience_counter += 1
    print(f"Validation loss did not improve. Incrementing patience to: {patience_counter}/{patience_limit}")
    
    if patience_counter >= patience_limit:
        print("Patience limit reached! Triggering EARLY STOPPING to prevent overfitting.")
    else:
        print("Continuing training...")

"""
Key Takeaways:
- Python uses whitespace indentation to structure blocks of code.
- elif is short for "else if" and allows checking multiple mutually exclusive options sequentially.
- The ternary operator is written as: `x if condition else y`.
- Nested conditionals allow hierarchical logical flows, but code readability degrades if nesting is too deep.

Interview Relevance:
- Does Python have a 'switch-case' statement? (Historically no, but Python 3.10 introduced structural pattern matching using 'match' and 'case').
- How does Python determine when a block of code ends? (By inspecting the decrease/shift back in indentation level).
- What is the Ternary Operator in Python? (Explain: `value_if_true if condition else value_if_false`).

AI/ML Relevance:
- Activation functions: ReLU (Rectified Linear Unit) is mathematically defined as: `f(x) = x if x > 0 else 0`.
- Decision Trees: Decision trees are essentially deep nested structures of if-else statements splitting on features.
- Early stopping algorithms monitor metrics across training iterations and conditionally halt execution using if-else logic.
"""
