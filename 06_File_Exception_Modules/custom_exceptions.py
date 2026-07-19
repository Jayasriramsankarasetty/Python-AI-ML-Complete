"""
Topic:
Custom Exceptions in Python

Importance:
Standard exceptions (like ValueError or TypeError) are generic. Creating domain-specific
custom exceptions makes error logging more descriptive and debugging easier in complex ML frameworks.

This file covers:
- Subclassing the built-in Exception class
- Defining custom attributes in custom exceptions
- Manually raising exceptions using 'raise'
- Practical ML application: Creating and raising an InvalidHyperparameterError
"""

# ==========================================
# 1. Defining a Custom Exception Class
# ==========================================
# Custom exceptions inherit from the base Exception class.

class InvalidHyperparameterError(Exception):
    """Exception raised when an ML model hyperparameter violates boundary limits."""
    def __init__(self, param_name, passed_value, message="Value is invalid"):
        self.param = param_name
        self.val = passed_value
        self.msg = message
        # Call the base Exception class constructor with a formatted message
        super().__init__(f"{self.msg} -> parameter '{self.param}' was given value: {self.val}")

# ==========================================
# 2. Raising and Catching the Exception
# ==========================================
# We use the 'raise' keyword to throw exceptions when custom validation assertions fail.

print("--- Raising Custom Exceptions ---")

def configure_training_pipeline(learning_rate, batch_size):
    """Configures parameters, raising Custom Exceptions on invalid boundary values"""
    print(f"Configuring pipeline with learning_rate={learning_rate}, batch_size={batch_size}...")
    
    # Validation 1: Learning Rate boundary check
    if learning_rate <= 0.0 or learning_rate > 1.0:
        raise InvalidHyperparameterError(
            param_name="learning_rate",
            passed_value=learning_rate,
            message="Learning rate must be strictly in range (0.0, 1.0]"
        )
        
    # Validation 2: Batch Size boundary check (must be a positive power of 2)
    if batch_size <= 0:
        raise InvalidHyperparameterError(
            param_name="batch_size",
            passed_value=batch_size,
            message="Batch size must be a positive integer"
        )
        
    print("Pipeline configuration loaded successfully.")

# Test Case A: Valid configs
try:
    configure_training_pipeline(0.01, 32)
except InvalidHyperparameterError as e:
    print(f"Error caught: {e}")

# Test Case B: Triggering LR validation error
print("\nTesting Invalid Learning Rate:")
try:
    configure_training_pipeline(1.5, 32)
except InvalidHyperparameterError as e:
    print(f"Error caught inside handler block:")
    print(f"  Message: {e}")
    print(f"  Faulty parameter name: {e.param}")
    print(f"  Incorrect value: {e.val}")

# Test Case C: Triggering Batch Size validation error
print("\nTesting Invalid Batch Size:")
try:
    configure_training_pipeline(0.01, -64)
except InvalidHyperparameterError as e:
    print(f"Error caught inside handler block:")
    print(f"  Message: {e}")

"""
Key Takeaways:
- Custom exceptions are created by subclassing the base `Exception` class.
- The `raise` keyword is used to trigger an exception immediately.
- Custom attributes (like parameter name and value) can be defined inside the exception's `__init__` constructor to pass structured error context to the catch block handler.

Interview Relevance:
- How do you create a custom exception in Python? (Define a class that inherits from the built-in `Exception` base class).
- What does the 'raise' keyword do? (It manually triggers a specified exception object, halting normal execution path).
- Why should custom exceptions inherit from Exception instead of BaseException? (BaseException is the root of all exceptions, including system-exiting signals like SystemExit and KeyboardInterrupt. Inheriting from Exception ensures standard catch-blocks can safely catch the error without disabling interrupt controls).

AI/ML Relevance:
- Input constraints: Libraries like PyTorch raise custom errors (like `DimensionError` or `CUDAError`) to provide contextual instructions for matrix mismatch or GPU resource exhausting configurations.
- Custom validators: Enterprise ML deployment platforms raise structured exceptions when prediction request payloads do not match required schemas (e.g. image channel count checks).
"""
