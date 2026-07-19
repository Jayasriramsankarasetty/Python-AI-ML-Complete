"""
Topic:
Pytest Testing Framework Basics

Importance:
Pytest is the industry standard for writing tests in Python. It is simpler and more Pythonic
than the built-in 'unittest' library, allowing standard assert checks instead of custom assert methods.
In ML, pytest is used to test data formats, features transformation steps, and model prediction metrics.

This file covers:
- Pytest function naming conventions (prefix 'test_')
- Standard assert assertions
- Parameterized tests using @pytest.mark.parametrize (testing multiple inputs)
- Fallback mock execution if pytest library is not installed
- Practical ML application: Testing min-max data scaling calculations
"""

# ==========================================
# 1. Functions to be Tested
# ==========================================

def scale_value(x, minimum, maximum):
    """Min-Max scales value to [0.0, 1.0] range"""
    if minimum == maximum:
        return 0.0
    return (x - minimum) / (maximum - minimum)

# ==========================================
# 2. Writing Pytest Functions
# ==========================================
# Rule: Test functions must start with the prefix 'test_'

def test_scaling_midpoint():
    # Pytest uses standard Python 'assert' statements directly
    assert scale_value(5, 0, 10) == 0.5

def test_scaling_boundaries():
    assert scale_value(0, 0, 10) == 0.0
    assert scale_value(10, 0, 10) == 1.0

# ==========================================
# 3. Parameterized Testing
# ==========================================
# Allows testing multiple combinations of inputs and expected outputs without repeating code.
# In raw pytest, we decorate using: @pytest.mark.parametrize("arg1, arg2, expected", [(val1, val2, exp1), ...])

# Since pytest might not be installed, we define a list of parameter cases manually,
# and check if we can import pytest to define the parameterized decorator.
parameter_cases = [
    (15, 10, 20, 0.5),   # (val, min, max, expected)
    (5, 5, 5, 0.0),      # Division safety check (returns 0.0)
    (2, 0, 8, 0.25)
]

try:
    import pytest
    
    # Define parameterized test using pytest decorator
    @pytest.mark.parametrize("x, minimum, maximum, expected", parameter_cases)
    def test_scaling_parameterized(x, minimum, maximum, expected):
        assert scale_value(x, minimum, maximum) == expected
        
except ImportError:
    # Fallback function if pytest is not active/installed
    print("Warning: 'pytest' module not detected. Falling back to custom runner.")
    
    def test_scaling_parameterized(x, minimum, maximum, expected):
        assert scale_value(x, minimum, maximum) == expected

# ==========================================
# 4. Executable Main Runner
# ==========================================
if __name__ == "__main__":
    try:
        import pytest
        print("Starting Pytest runner execution on this file...")
        # Run pytest on the current file
        pytest.main([__file__, "-v"])
    except ImportError:
        print("\n--- Executing Tests Manually (No Pytest library detected) ---")
        # Run tests manually by executing the assert statements
        try:
            test_scaling_midpoint()
            print("  test_scaling_midpoint: PASSED")
            
            test_scaling_boundaries()
            print("  test_scaling_boundaries: PASSED")
            
            # Run parameterized checks manually
            for x, minimum, maximum, expected in parameter_cases:
                test_scaling_parameterized(x, minimum, maximum, expected)
            print("  test_scaling_parameterized (All cases): PASSED")
            
            print("\nVerification: All tests PASSED successfully!")
        except AssertionError as e:
            print(f"  Assertion failed: {e}")
        except Exception as e:
            print(f"  Test execution failed with error: {e}")

"""
Key Takeaways:
- Pytest does not require you to wrap tests in a Class subclassing TestCase; write functions prefixed with `test_`.
- Use standard `assert` keyword.
- `@pytest.mark.parametrize` enables writing a single test code block that checks multiple input vectors.

Interview Relevance:
- What is the difference between unittest and pytest? (Unittest requires class scaffolding and specific assertion methods; pytest allows writing simple standalone test functions and uses standard Python `assert` statements).
- How do you parameterize a test in pytest? (Use the `@pytest.mark.parametrize` decorator, passing a string of parameter names and a list of tuples containing test cases).
- What command runs tests using pytest? (`pytest` or `python -m pytest`).

AI/ML Relevance:
- Pytest parameterization is heavily used in scikit-learn and PyTorch to test model predictions across different initialization seeds or input matrix dimensions efficiently.
"""
