"""
Topic:
Advanced Decorators in Python

Importance:
Decorators modify function behaviors dynamically. In professional production systems:
- We must preserve original function metadata (names, docstrings) using functools.wraps.
- We need to pass configuration arguments to decorators (like accuracy thresholds).
- We chain multiple decorators (timing, validation, logging).

This file covers:
- Preserving docstrings using functools.wraps
- Creating decorators that accept arguments
- Chaining multiple decorators
- Practical ML application: Data dimensions validator decorator combined with a training timer
"""

import time
from functools import wraps

# ==========================================
# 1. Preserving Metadata (functools.wraps)
# ==========================================
# Standard decorators overwrite the function's __name__ and __doc__ with the wrapper's details.
# wraps() copies them back to maintain reflection consistency.

def standard_decorator(func):
    @wraps(func)  # Preserves name and docstring of 'func'
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@standard_decorator
def custom_classifier():
    """Custom classification model docstring description."""
    pass

print("--- Preserving Metadata ---")
print("Function name preserved:", custom_classifier.__name__)
print("Docstring preserved:", custom_classifier.__doc__.strip())

# ==========================================
# 2. Decorators that Accept Arguments
# ==========================================
# A decorator with arguments requires THREE layers of nested functions:
# 1. Outer layer: accepts the decorator arguments.
# 2. Middle layer: accepts the function object.
# 3. Inner layer (wrapper): executes validation and function.

def threshold_monitor(min_accuracy=0.85):
    """
    Decorator validating if a returned accuracy metric is above threshold.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            metric_score = func(*args, **kwargs)
            print(f"[MONITOR] Model accuracy evaluated to: {metric_score:.4f}")
            if metric_score < min_accuracy:
                print(f"  Warning: Accuracy is below expected threshold ({min_accuracy})!")
            else:
                print("  Success: Accuracy threshold met.")
            return metric_score
        return wrapper
    return decorator

@threshold_monitor(min_accuracy=0.90)
def train_random_forest():
    # Simulate training returning accuracy
    return 0.88

print("\n--- Decorator with Arguments ---")
train_random_forest()

# ==========================================
# 3. Chaining Decorators & Hands-on ML Use-Case
# ==========================================
# Multiple decorators execute from closest to furthest (bottom-up sequence).
# E.g.
# @decorator_one
# @decorator_two
# def func(): ...
# Runs: decorator_one(decorator_two(func))

# Decorator A: Timer
def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIMER] '{func.__name__}' execution took {time.time() - start:.4f}s.")
        return result
    return wrapper

# Decorator B: Input Dimension Checker (accepts expected length argument)
def validate_dimensions(expected_dim):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Inspect first positional argument representing input data array
            data_input = args[0] if args else kwargs.get("data")
            if not isinstance(data_input, list) or len(data_input) != expected_dim:
                raise ValueError(f"[VALIDATION ERROR] Expected input length of {expected_dim}, got {len(data_input) if isinstance(data_input, list) else type(data_input)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Chaining both decorators on a prediction step
@timer_decorator
@validate_dimensions(expected_dim=3)
def predict_coordinates(data):
    """Predicts a spatial label based on a 3D coordinate list."""
    print("Processing predictions on valid coordinate inputs...")
    time.sleep(0.1)  # Simulate latency
    return "Class_A"

print("\n--- Chaining Decorators ---")
# Valid call (length 3 input)
output_valid = predict_coordinates([1.2, 3.4, 5.6])
print("Prediction output:", output_valid)

# Invalid call (triggers ValueError)
print("\nCalling with invalid dimensions:")
try:
    predict_coordinates([1.2, 3.4])
except ValueError as e:
    print("Caught error:", e)

"""
Key Takeaways:
- Use `functools.wraps` on wrapper functions to prevent overriding the original function's name and docstring attributes.
- Decorators that accept arguments return a decorator function, which in turn returns the wrapper.
- Chained decorators execute from bottom-to-top (inner-to-outer).

Interview Relevance:
- Why do we use `@wraps(func)` from the `functools` module? (To preserve the original function's metadata, like `__name__` and `__doc__`, which would otherwise be overwritten by the wrapper function's metadata).
- How do you pass arguments to a decorator? (By wrapping the decorator in another outer function that accepts the arguments, returning the actual decorator).
- What is the sequence of execution when chaining decorators? (Bottom-up: the decorator nearest to the function is applied first).

AI/ML Relevance:
- Schema validation: Rest APIs serving predictions check query inputs (like checking if input lists represent correct pixel arrays) before executing heavy inference loops.
- Experiment tracking: Loggers hook training loops to log configs and accuracy progress automatically.
"""
