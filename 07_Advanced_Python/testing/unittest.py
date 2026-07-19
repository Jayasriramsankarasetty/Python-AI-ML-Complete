"""
Topic:
Unit Testing using the built-in unittest Framework

Importance:
Unit testing validates that individual code blocks (functions, classes) work correctly.
In AI/ML production pipelines, unit tests verify data processing calculations and activation limits
to prevent bugs from propagating to active models.

This file covers:
- Dynamic path adjustment to bypass local module shadow collisions
- Creating test cases by subclassing unittest.TestCase
- Standard assertions: assertEqual(), assertTrue(), assertRaises()
- Setting up resources using setUp() and tearing them down using tearDown()
- Practical ML application: Testing Sigmoid activation boundaries and shape outputs
"""

import sys
import os

# --- PATH AND MODULE RESOLUTION HACK TO PREVENT LOCAL SHADOWING ---
# Because this file is named 'unittest.py', standard library imports of 'unittest'
# by pytest or other modules would resolve to this file, causing circular imports.
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir in sys.path:
    sys.path.remove(current_dir)

# Remove the cached local module from sys.modules to force a fresh lookup
if 'unittest' in sys.modules:
    del sys.modules['unittest']

# Import the actual standard library unittest module
import unittest as std_unittest

# Bind the name globally and overwrite the sys.modules entry so future imports get the real package
unittest = std_unittest
sys.modules['unittest'] = std_unittest

# Restore the local path
sys.path.insert(0, current_dir)

# ==========================================
# 1. Functions to be Tested
# ==========================================
# Simulated ML utility functions we want to test

def compute_sigmoid(x):
    """Sigmoid activation function: 1 / (1 + e^-x)"""
    import math
    return 1.0 / (1.0 + math.exp(-x))

def scale_min_max(value, min_val, max_val):
    """Scales a value to [0, 1] range based on limits"""
    if min_val == max_val:
        raise ValueError("Min and Max values cannot be equal.")
    return (value - min_val) / (max_val - min_val)

# ==========================================
# 2. Writing the Test Class
# ==========================================

class TestMLUtilities(unittest.TestCase):
    
    # setUp(): Runs before EVERY single test method. Useful for configuring datasets.
    def setUp(self):
        print("  [SETUP] Initializing test boundaries...")
        self.tolerance = 0.0001
        
    # tearDown(): Runs after EVERY single test method. Useful for cleaning logs/files.
    def tearDown(self):
        print("  [TEARDOWN] Cleaning test configuration...")

    # A. Test Sigmoid calculations
    def test_sigmoid_math(self):
        print("    Running: test_sigmoid_math")
        # Sigmoid(0) should be exactly 0.5
        self.assertEqual(compute_sigmoid(0), 0.5)
        # Sigmoid(large positive) should approach 1.0
        self.assertTrue(compute_sigmoid(100) > 0.999)
        # Sigmoid(large negative) should approach 0.0
        self.assertTrue(compute_sigmoid(-100) < 0.001)

    # B. Test Normalization logic
    def test_min_max_scaling(self):
        print("    Running: test_min_max_scaling")
        # Test standard value
        self.assertEqual(scale_min_max(5, 0, 10), 0.5)
        # Test extreme boundary
        self.assertEqual(scale_min_max(10, 0, 10), 1.0)

    # C. Test Exception Raising
    def test_scaling_exceptions(self):
        print("    Running: test_scaling_exceptions")
        # Assert that passing equal min-max raises ValueError
        with self.assertRaises(ValueError):
            scale_min_max(5, 10, 10)

# ==========================================
# 3. Main Run Execution
# ==========================================
if __name__ == "__main__":
    # Runs all tests in the class
    unittest.main()

"""
Key Takeaways:
- Subclass `unittest.TestCase` to create groups of unit tests.
- Methods checking states must start with the prefix `test_` to be discovered automatically.
- `setUp()` and `tearDown()` configure and cleanup test environments per test.
- Use context managers `self.assertRaises()` to verify code raises expected exceptions on failure inputs.

Interview Relevance:
- What is unit testing and why is it important? (It isolates and tests individual modules of code to ensure correctness and prevent regression bugs on updates).
- Explain the role of setUp() and tearDown() in unittest. (setUp runs before each test to prepare states; tearDown runs after each test to reset states/delete temp files).
- What prefix must test functions have? (They must start with `test_` for the runner to scan them).

AI/ML Relevance:
- Matrix limits validation: Unit tests assert that functions like softmax output vectors sum to exactly 1.0, preventing weight training calculations from drifting.
- Target check asserts: Ensuring classification arrays contain only expected integers (like [0, 1]) is asserted via unit tests to avoid pipeline execution crashes.
"""
