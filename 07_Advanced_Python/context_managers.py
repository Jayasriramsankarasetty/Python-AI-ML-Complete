"""
Topic:
Custom Context Managers in Python

Importance:
Context managers ensure clean handling of resources (like file streams, database connections, and locks).
In AI/ML, context managers measure training execution blocks and configure runtime devices
(e.g., selecting GPU vs CPU devices for tensor allocations).

This file covers:
- The context manager protocol: __enter__() and __exit__()
- Creating a class-based context manager
- Handling exceptions inside __exit__()
- Creating context managers using contextlib.contextmanager
- Practical ML application: Timer context manager and device runtime environment simulator
"""

import time
from contextlib import contextmanager

# ==========================================
# 1. Class-Based Context Manager
# ==========================================
# To implement a custom context manager:
# - __enter__(): runs when entering the 'with' block. Returns a value to bind to the 'as' variable.
# - __exit__(exc_type, exc_val, exc_tb): runs when exiting the block.
#   Returns True if exceptions raised inside the block should be suppressed, False otherwise.

class TimerContext:
    """Measures the elapsed execution time inside a code block."""
    def __enter__(self):
        self.start = time.time()
        # Return self so it can be referenced in the 'as' clause
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"[TIMER CONTEXT] Execution block took {self.elapsed:.6f} seconds.")
        
        # If an exception was raised inside the block, print it
        if exc_type:
            print(f"  Note: Block exited with error: {exc_val}")
        # Return False to let any exceptions propagate up (standard practice)
        return False

print("--- Class-Based Context Manager ---")
with TimerContext() as timer:
    print("Performing heavy computation tasks...")
    time.sleep(0.3)
print("Finished outside block.")

# ==========================================
# 2. Generator-Based Context Manager (@contextmanager)
# ==========================================
# Writing class protocols can be verbose.
# Using 'contextlib' allows creating context managers using generator syntax:
# - Everything before the yield statement is __enter__().
# - The yield yields the 'as' reference.
# - Everything after the yield (or inside finally) is __exit__().

@contextmanager
def cuda_device_selector(device_id):
    """
    Simulates selecting and loading weights to a specific GPU device inside the context block,
    and cleaning up allocations when exiting.
    """
    print(f"\n[DEVICE MANAGER] ---> Loading model weights to CUDA device: GPU_{device_id}...")
    try:
        # Yield is where the 'with' block body executes
        yield f"cuda:{device_id}"
    finally:
        # Cleanup tasks (runs regardless of errors)
        print(f"[DEVICE MANAGER] <--- Releasing allocated memory on GPU_{device_id}. Device reset.")

print("\n--- Generator-Based Context Manager ---")
with cuda_device_selector(device_id=1) as active_device:
    print(f"Active runtime reference: {active_device}")
    print("Training model layers on GPU...")
print("Exited GPU selection block.")

# ==========================================
# 3. Handling Exceptions inside __exit__()
# ==========================================
# We can suppress errors inside the block.

class SuppressZeroDivision:
    def __enter__(self):
        print("\nEntered ZeroDivision suppression block.")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ZeroDivisionError:
            print(f"  Suppressed ZeroDivisionError safely: {exc_val}")
            return True  # Returns True to suppress the exception
        return False  # Let other exceptions propagate

with SuppressZeroDivision():
    print("Calculating metrics...")
    val = 1 / 0  # Triggers ZeroDivisionError but is suppressed!
print("Code execution continues without crashing.")

"""
Key Takeaways:
- Context managers allocate resources on entering and guarantee clean teardown on exiting the `with` block.
- Class-based context managers implement `__enter__` and `__exit__`.
- Generator-based context managers use the `@contextmanager` decorator and a `yield` statement.
- Returning `True` from `__exit__` suppresses exceptions raised in the block.

Interview Relevance:
- Explain the context manager protocol. What methods must be implemented? (Class must define `__enter__()` and `__exit__()`).
- How does Python's `with` statement handle exceptions? (It passes the exception type, value, and traceback to `__exit__()`. If `__exit__()` returns True, the exception is suppressed).
- What is the advantage of the `@contextmanager` decorator? (It allows writing context managers using simple generators instead of full classes).

AI/ML Relevance:
- CUDA context switching: PyTorch uses custom context managers (e.g. `with torch.no_grad():`) to disable gradient updates during model validation loops, conserving memory.
- Execution Benchmarking: Wrapping training blocks inside custom timing context managers helps benchmark layer optimization times.
"""
