"""
Topic:
Basic Decorators in Python

Importance:
Decorators modify the behavior of functions dynamically without editing their source code.
They are heavily used for logging training steps, timing executions, verifying authentication
in APIs, and configuring routes in web servers like FastAPI.

This file covers:
- Higher-Order Functions (functions as first-class citizens)
- Basic decorator wrapper mechanics
- Using the @ decorator syntax
- Measuring execution time of an ML training step with a timer decorator
"""

import time

# ==========================================
# 1. Functions as First-Class Citizens
# ==========================================
# In Python, functions can be:
# - Passed as arguments to other functions
# - Returned from other functions
# - Assigned to variables

def say_hello():
    return "Hello!"

def execute_function(func):
    """Higher-order function taking another function as argument"""
    print("Executing helper wrapper...")
    result = func()
    return f"Result: {result}"

print("--- Higher-Order Functions ---")
print(execute_function(say_hello))

# ==========================================
# 2. Creating a Simple Decorator
# ==========================================
# A decorator is a function that takes a function as argument, wraps it,
# adds some custom behavior, and returns the modified wrapper function.

def debug_logger(func):
    def wrapper():
        print("[LOG - BEFORE]: Executing function block...")
        func()
        print("[LOG - AFTER]: Function execution completed.")
    return wrapper

# Standard way to apply decorator without syntax shortcut
def process_data_old():
    print("Processing datasets...")

decorated_process = debug_logger(process_data_old)
print("\n--- Traditional Decorator Call ---")
decorated_process()

# ==========================================
# 3. Using the @ Syntax Shortcut
# ==========================================
# Rather than reassigning variables, we use the @decorator syntax above the function declaration.

@debug_logger
def process_data_new():
    print("Processing datasets cleanly...")

print("\n--- Pythonic @ Decorator Call ---")
process_data_new()

# ==========================================
# 4. Hands-on ML Use-Case: Performance Timer
# ==========================================
# ML models can take seconds, hours, or days to run.
# Creating a timer decorator helps benchmark training function runtimes.

def performance_timer(func):
    """
    Decorator that calculates and prints execution time of a function.
    Notice the use of *args and **kwargs in the wrapper to accept any function signature!
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"[BENCHMARK] '{func.__name__}' execution took {elapsed_time:.6f} seconds.")
        return result
    return wrapper

@performance_timer
def train_dummy_model(num_epochs, model_name="NeuralNet"):
    print(f"\nTraining model '{model_name}' for {num_epochs} epochs...")
    # Simulate computation delay
    time.sleep(0.5)
    print("Model trained successfully.")
    return "Model Weights Dict Object"

print("\n--- Practical ML Use-Case: Benchmarking Decorator ---")
output = train_dummy_model(500, model_name="DeepCNN")
print("Returned weight structure:", output)

"""
Key Takeaways:
- Decorators extend the behavior of an existing function dynamically.
- The `@decorator` syntax is a wrapper shortcut for `func = decorator(func)`.
- Use `*args` and `**kwargs` in the inner wrapper function to ensure the decorator works with any inputs.

Interview Relevance:
- Explain how decorators work under the hood. (Mention first-class functions, closures, and returning functions).
- Why do we use *args and **kwargs inside the wrapper function of a decorator? (To allow the decorator to wrap functions with arbitrary input parameters).
- What is `functools.wraps` and why is it recommended for decorators? (It preserves the original function's name and docstring metadata. This will be covered in Advanced Python).

AI/ML Relevance:
- Benchmark profiling: Engineers use decorators to wrap inference functions to track latency (ms per request).
- API Routes: In model deployment, frameworks like FastAPI use decorators (like `@app.post("/predict")`) to map HTTP requests to prediction functions.
- Registry patterns: Libraries like PyTorch or Hugging Face use decorators to register custom models, loss metrics, and optimizers.
"""
