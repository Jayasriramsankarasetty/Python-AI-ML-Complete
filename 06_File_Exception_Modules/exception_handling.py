"""
Topic:
Exception Handling in Python

Importance:
Exceptions are runtime errors that disrupt normal execution. Handling exceptions prevents crashes
in production environments. In model deployment (APIs), errors must be intercepted to return clean responses.

This file covers:
- Difference between syntax errors and exceptions
- The try-except block
- Handling specific exceptions (FileNotFoundError, ValueError, ZeroDivisionError)
- Catching multiple exceptions
- The 'else' and 'finally' blocks
- Practical ML application: Handling a missing dataset pathway and validating metric calculations
"""

# ==========================================
# 1. Understanding Try-Except Basics
# ==========================================
# try: wraps code that might raise an exception.
# except: defines recovery blocks for specific exceptions.

print("--- Try-Except (FileNotFoundError) ---")
missing_file = "non_existent_data.csv"

try:
    print(f"Attempting to open: {missing_file}")
    with open(missing_file, "r") as file:
        data = file.read()
except FileNotFoundError as e:
    # Catches and handles FileNotFoundError
    print(f"Exception caught successfully! System warning: {e}")
    print("Reverting to default fallback configuration: loading placeholder dataset...")

# ==========================================
# 2. Handling Multiple Exceptions
# ==========================================
# Different errors require different recovery actions.

print("\n--- Handling Specific Exceptions ---")

def process_accuracy_score(total_correct, total_predictions):
    try:
        # Step 1: Compute ratio
        ratio = float(total_correct) / float(total_predictions)
        # Step 2: Format percentage
        percentage_str = f"Accuracy: {ratio * 100:.2f}%"
        return percentage_str
        
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: Total predictions is 0. Returning 0.0% accuracy.")
        return "Accuracy: 0.0%"
    except ValueError:
        print("Caught ValueError: Input values could not be casted to float.")
        return "Accuracy: Error"
    except TypeError as e:
        print(f"Caught TypeError: Invalid datatype passed. Error details: {e}")
        return "Accuracy: Error"

# Test cases
print(process_accuracy_score(15, 20))      # Valid
print(process_accuracy_score(0, 0))        # Triggers ZeroDivisionError
print(process_accuracy_score("abc", 20))  # Triggers ValueError
print(process_accuracy_score([1], 20))     # Triggers TypeError

# ==========================================
# 3. Try-Except-Else-Finally Block
# ==========================================
# - else: executes ONLY if no exception was raised in the try block.
# - finally: ALWAYS executes, regardless of whether an exception was raised or caught. Useful for resource cleanup.

print("\n--- Try-Except-Else-Finally ---")
divisor = 5  # Try changing to 0 to trace paths

try:
    print("Executing division calculation...")
    result = 100 / divisor
except ZeroDivisionError:
    print("  Exception block: Divisor cannot be zero.")
else:
    print(f"  Else block: Division completed successfully. Result: {result}")
finally:
    print("  Finally block: Releasing resources and continuing execution.")

"""
Key Takeaways:
- Exceptions are caught via `try-except`. Do not use a bare `except:` as it catches all exceptions (including KeyboardInterrupt) making debugging difficult.
- The `else` block runs only if the `try` block succeeds without raising errors.
- The `finally` block always runs, making it the ideal location to close databases or release file lock handles.

Interview Relevance:
- What is the difference between Syntax Error and Exception? (Syntax errors are caught by parser before execution; exceptions are runtime errors that occur during execution).
- What is the purpose of the 'finally' block? (To execute cleanup code that must run regardless of success or failure).
- Can we have a 'try' block without an 'except' block? (Yes, but it must be followed by a 'finally' block, e.g., `try-finally`).

AI/ML Relevance:
- Safe Loading: In production APIs, inference requests are wrapped in try-except blocks to catch corrupt inputs (e.g. invalid base64 images) and return a structured HTTP 400 Bad Request error.
- Zero-Division: During training validations, if validation sets are empty or class subsets are missing, metrics equations must intercept division-by-zero to avoid breaking optimization pipelines.
"""
