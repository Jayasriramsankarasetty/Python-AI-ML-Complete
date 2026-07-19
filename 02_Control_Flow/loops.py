"""
Topic:
Loops (for, while, control statements) in Python

Importance:
Iteration is the core of AI algorithms. Training models, iterating through raw files,
processing image batches, and optimizing parameters all require loops.

This file covers:
- For loops and range() function
- While loops
- Loop control statements: break, continue, and pass
- Python's unique 'for-else' / 'while-else' construct
- Practical ML application: Simulating epoch iterations and parameter convergence
"""

# ==========================================
# 1. For Loops and range()
# ==========================================
# 'for' loop is used to iterate over a sequence (list, tuple, string, or range).
# range(start, stop, step) generates numbers from 'start' to 'stop - 1' incremented by 'step'.

print("--- Range and For Loops ---")
# Simple loop from 0 to 4
for i in range(5):
    print(f"Iteration: {i}")

# Loop from 1 to 9 with step of 2
print("\nOdd numbers in range(1, 10, 2):")
for num in range(1, 10, 2):
    print(num, end=" ")
print()

# ==========================================
# 2. While Loops
# ==========================================
# Runs as long as a condition is True.
print("\n--- While Loops ---")
threshold_loss = 0.05
simulated_loss = 0.08
epoch = 1

# Reduce loss dynamically until it hits threshold
while simulated_loss > threshold_loss:
    print(f"Epoch {epoch} | Current Loss: {simulated_loss:.4f}")
    # Simulate training learning decay
    simulated_loss -= 0.012
    epoch += 1

print(f"Convergence reached at Epoch {epoch-1} with Loss: {simulated_loss:.4f}")

# ==========================================
# 3. Loop Control: Break, Continue, Pass
# ==========================================
# - break: Terminates the loop immediately.
# - continue: Skips the remaining code in the current iteration and goes to the next.
# - pass: A null statement placeholder to satisfy syntactical requirements.

print("\n--- Loop Control (Break & Continue) ---")
# Example: Batch validation check
accuracies = [0.82, 0.85, 0.50, 0.91, 0.70]  # List of accuracies

for idx, acc in enumerate(accuracies):
    # Skip processing low values (continue)
    if acc < 0.60:
        print(f"Index {idx}: Flagged anomaly ({acc}) - Skipping processing.")
        continue
        
    print(f"Index {idx}: Valid accuracy score: {acc}")
    
    # Terminate early if threshold goal achieved (break)
    if acc >= 0.90:
        print("Index reached target validation accuracy of >= 90%. Halting further evaluation.")
        break

# Example: pass placeholder
for x in range(3):
    if x == 1:
        pass  # Placeholder: do nothing for 1, maybe implement later
    else:
        print(f"Value of x is: {x}")

# ==========================================
# 4. For-Else / While-Else Construct
# ==========================================
# The 'else' block executes ONLY if the loop completed successfully without hitting a 'break'.
# This is highly relevant for search logic in interviews.

print("\n--- Loop-Else Construct ---")
features_in_data = ["age", "income", "zipcode", "tenure"]
search_target = "gpa"

for feature in features_in_data:
    if feature == search_target:
        print(f"Found target feature '{search_target}' in the dataset columns!")
        break
else:
    # Executes only if the loop ran to completion without finding 'gpa'
    print(f"Target feature '{search_target}' was NOT found in the dataset columns.")

# ==========================================
# 5. Hands-on ML Use-Case: Gradient Descent Simulation
# ==========================================
# Let's combine loops to simulate updating a model parameter (weight)
# with learning rate and gradient checks.
print("\n--- Practical ML Use-Case: Weight Update Loop ---")

weight = 10.0          # Initial weight parameter
learning_rate = 0.1
target_weight = 2.0    # Target optimized parameter value
tolerance = 0.05
max_epochs = 100

for epoch in range(1, max_epochs + 1):
    # Compute derivative (gradient) of loss: (weight - target_weight) * 2
    gradient = (weight - target_weight) * 2
    
    # Update weight using formula: weight = weight - (learning_rate * gradient)
    weight -= learning_rate * gradient
    
    # Check convergence condition
    if abs(weight - target_weight) < tolerance:
        print(f"Optimized Weight converged to: {weight:.4f} at epoch {epoch}.")
        break
else:
    print("Optimization reached max epochs without satisfying convergence tolerance.")

"""
Key Takeaways:
- For loops are best when the number of iterations is known or bounded.
- While loops run until a condition changes to False (ensure a progression step to prevent infinite loops).
- 'break' exits the loop; 'continue' skips the current step; 'pass' does nothing.
- 'else' after a loop executes if and only if 'break' was not encountered.

Interview Relevance:
- Explain what loop-else does in Python. When does it run? (Runs when loop exits without a break).
- What is the difference between break and continue?
- How does range(1, 5) differ from range(1, 5, 2)? (Explain boundaries and steps).

AI/ML Relevance:
- Epochs: Neural networks train by looping through the full dataset multiple times (epochs).
- Gradient Descent: Optimization loops (like SGD, Adam) update weights inside a while/for loop.
- Batch processing: Dataloaders loop over slices of high-dimensional arrays to feed them to GPUs.
"""
