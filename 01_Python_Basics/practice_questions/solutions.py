"""
Topic:
Python Basics Practice Solutions

Importance:
Solidifying basic syntax, operator precedence, typecasting, and inputs is 
essential for building advanced programmatic logic in coding rounds and pipelines.

This file covers:
- Solution 1: Celsius to Fahrenheit Converter
- Solution 2: Swap two variables without using a third variable
- Solution 3: BMI Calculator
- Solution 4: Simple and Compound Interest Calculator
- Solution 5: Odd-Even check using Bitwise AND
"""

# =====================================================================
# Solution 1: Temperature Converter (Celsius to Fahrenheit)
# =====================================================================
print("==================================================")
print("SOLUTION 1: Temperature Converter (Celsius to Fahrenheit)")
print("==================================================")

# Simulating a user input of 37 degrees Celsius (Human Body Temp)
celsius_input = "37"
celsius = float(celsius_input)  # Typecasting string to float

# Applying conversion formula
fahrenheit = (celsius * 9/5) + 32

print(f"Input Celsius: {celsius}°C")
print(f"Output Fahrenheit: {fahrenheit:.2f}°F")
print()


# =====================================================================
# Solution 2: Swap Variables without a Third Variable
# =====================================================================
print("==================================================")
print("SOLUTION 2: Swap Variables without Third Variable")
print("==================================================")

a = 15
b = 42
print(f"Before Swap: a = {a}, b = {b}")

# Method A: Pythonic Tuple Unpacking Swap (Industry Standard)
a, b = b, a
print(f"After Swap (Tuple Unpacking): a = {a}, b = {b}")

# Resetting values
a = 15
b = 42

# Method B: Arithmetic Swap (Addition/Subtraction)
a = a + b  # a now stores sum (57)
b = a - b  # b now stores original a (57 - 42 = 15)
a = a - b  # a now stores original b (57 - 15 = 42)
print(f"After Swap (Arithmetic): a = {a}, b = {b}")
print()


# =====================================================================
# Solution 3: BMI Calculator
# =====================================================================
print("==================================================")
print("SOLUTION 3: BMI Calculator")
print("==================================================")

weight_kg = 72.0
height_m = 1.78

# Calculate BMI using exponentiation ** 2
bmi = weight_kg / (height_m ** 2)

print(f"Weight: {weight_kg} kg | Height: {height_m} m")
print(f"Calculated BMI: {bmi:.1f}")
print()


# =====================================================================
# Solution 4: Simple and Compound Interest Calculator
# =====================================================================
print("==================================================")
print("SOLUTION 4: Simple and Compound Interest Calculator")
print("==================================================")

principal = 10000.0   # $10,000 investment
rate = 5.0            # 5% annual interest rate
time_years = 3        # 3 year period

# 1. Simple Interest
simple_interest = (principal * rate * time_years) / 100

# 2. Compound Interest (Compounded Annually)
# Formula: P * (1 + R/100)^T - P
compound_interest = principal * ((1 + (rate / 100)) ** time_years) - principal

print(f"Principal: ${principal} | Rate: {rate}% | Time: {time_years} years")
print(f"Simple Interest: ${simple_interest:.2f}")
print(f"Compound Interest: ${compound_interest:.2f}")
print()


# =====================================================================
# Solution 5: Odd-Even Check Using Bitwise Operators
# =====================================================================
print("==================================================")
print("SOLUTION 5: Odd-Even Check Using Bitwise AND")
print("==================================================")

# Logic:
# Binary representation of even numbers ends with 0 (e.g., 4 is 0100).
# Binary representation of odd numbers ends with 1 (e.g., 5 is 0101).
# Bitwise ANDing (&) any number with 1 checks the last bit.
# If number & 1 == 0, it's Even. If number & 1 == 1, it's Odd.

num_even = 88
num_odd = 13

even_check = (num_even & 1) == 0
odd_check = (num_odd & 1) == 0

print(f"Is {num_even} Even? {even_check} (using & 1)")
print(f"Is {num_odd} Even? {odd_check} (using & 1)")
print()


"""
Key Takeaways:
- Pythonic tuple swapping `a, b = b, a` is cleaner and faster than mathematical swapping.
- Precedence matters in calculation formulas; always use parentheses `()` to enforce correct math order.
- The bitwise operator `&` is computationally faster than the `%` arithmetic division operator at the processor level.

Interview Relevance:
- Candidates are frequently asked to swap variables without a third variable. Know both methods: tuple unpacking (Python-specific) and arithmetic addition/subtraction.
- Be prepared to discuss bitwise operations as optimizations in loops.

AI/ML Relevance:
- Normalization & Formulas: Implementing formulas like compound interest or BMI helps build coding accuracy for ML metric formulas (like Root Mean Squared Error, Gini Impurity, or Entropy).
- Bitwise masks: Checking binary values is used when processing binary arrays or target classes in deep learning classification outputs.
"""
