"""
Topic:
Function Basics in Python

Importance:
Functions allow modularity, code reuse, and structure. In AI/ML, functions are used
to define layers, compute losses, preprocess data batches, and build cleaner model pipelines.

This file covers:
- Defining and calling functions with def
- Writing function docstrings (PEP 257)
- Scope of variables: Local vs Global scope
- The 'global' keyword and its implications
- Practical ML example: Implementing a Rectified Linear Unit (ReLU) activation function
"""

# Global variable representing our model name
GLOBAL_MODEL_NAME = "ResNet-50"

# ==========================================
# 1. Defining a Function and Docstrings
# ==========================================
# Functions are defined using the 'def' keyword.
# A docstring describes what the function does, its parameters, and returns.

def greet_candidate(name):
    """
    Greets the candidate for the placement preparation.

    Parameters:
        name (str): The name of the candidate.

    Returns:
        None
    """
    print(f"Welcome, {name}! Let's master Python functions.")

print("--- Function Execution ---")
greet_candidate("Jaya Sri Ram")

# Inspecting function docstring programmatically (frequently asked in interviews)
print("\nGreeter Function Docstring:")
print(greet_candidate.__doc__)

# ==========================================
# 2. Local vs Global Scope
# ==========================================
# Variables defined inside a function are local to it.
# Variables defined outside have global scope.

hyperparameter_lr = 0.01  # Global variable

def train_step():
    local_loss = 0.35     # Local variable
    print("Inside train_step():")
    print(f"  Accessing Global Hyperparameter (lr): {hyperparameter_lr}")
    print(f"  Accessing Local Loss: {local_loss}")

train_step()

# Accessing local_loss outside would raise NameError:
# print(local_loss)

# ==========================================
# 3. The 'global' Keyword
# ==========================================
# If we want to modify a global variable inside a function, we must use the 'global' keyword.

training_epochs = 10  # Global

def double_epochs():
    global training_epochs
    training_epochs = training_epochs * 2
    print(f"Modified inside double_epochs(): {training_epochs}")

print("\n--- Modifying Global Variables ---")
print(f"Original Epochs value: {training_epochs}")
double_epochs()
print(f"Value of Epochs outside: {training_epochs}")

# ==========================================
# 4. Hands-on ML Use-Case: ReLU Activation
# ==========================================
# ReLU (Rectified Linear Unit) returns 0 if input is negative, and the input itself if positive.
# Formula: f(x) = max(0, x)

def relu_activation(x):
    """
    Computes the ReLU activation value for a given float input.

    Parameters:
        x (float): The input value to the neural network node.

    Returns:
        float: The activated value.
    """
    if x > 0:
        return float(x)
    else:
        return 0.0

print("\n--- Practical ML Use-Case: ReLU Activation ---")
input_value_positive = 4.5
input_value_negative = -2.8

output_pos = relu_activation(input_value_positive)
output_neg = relu_activation(input_value_negative)

print(f"ReLU({input_value_positive}) -> {output_pos}")
print(f"ReLU({input_value_negative}) -> {output_neg}")

"""
Key Takeaways:
- Use `def` to define functions and a return statement to pass values back.
- Docstrings are enclosed in triple quotes directly under the function definition and explain intent.
- Variables created inside a function are local. To edit a global variable, declare it with `global`.
- Best practice: Avoid overuse of the `global` keyword as it makes code harder to debug.

Interview Relevance:
- What is a docstring in Python and how do you access it programmatically? (Access using `func.__doc__`).
- How does variable scope lookup work? (Explain the LEGB rule: Local -> Enclosing -> Global -> Built-in).
- Can a local variable have the same name as a global variable? (Yes, this is called variable shadowing. The local variable takes precedence within its scope).

AI/ML Relevance:
- Modularity: Model configurations, forward steps, backward passes, metric logs are all wrapped in functions for readability.
- Activation Functions: Simple math operations like ReLU, Sigmoid, or Leaky ReLU are implemented as python functions in custom scratch models.
"""
