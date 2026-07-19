"""
Topic:
Lambda Functions, Map, and Filter in Python

Importance:
Functional programming features enable short, readable, inline operations.
Data preprocessing, text cleaning, feature transformation, and row-by-row mapping
frequently employ lambdas, map, and filter.

This file covers:
- Lambda (Anonymous) Functions
- Transforming lists using map()
- Filtering elements using filter()
- Practical ML application: Normalizing data features and isolating high-performing models
"""

# ==========================================
# 1. Lambda Functions
# ==========================================
# Syntax: lambda arguments: expression
# Simple inline functions that don't need a name (anonymous).

print("--- Lambda Functions ---")
# Normal function
def add_five(x):
    return x + 5

# Equivalent lambda function
lambda_add_five = lambda x: x + 5

val = 10
print(f"Normal function output ({val}): {add_five(val)}")
print(f"Lambda function output ({val}): {lambda_add_five(val)}")

# Lambda with multiple arguments
multiply = lambda a, b: a * b
print(f"Multiplication using lambda (6 * 7): {multiply(6, 7)}")

# ==========================================
# 2. The map() Function
# ==========================================
# Syntax: map(function, iterable)
# Applies a function to all elements in an iterable. Returns a map object (iterator).

print("\n--- map() Function ---")
raw_measurements = [10.0, 20.0, 30.0, 40.0]

# Preprocess: Scale values by division (normalizing to range [0, 1] relative to max 40.0)
scale_fn = lambda x: x / 40.0

scaled_measurements_map = map(scale_fn, raw_measurements)
# Convert the map iterator to a list to view contents
scaled_measurements = list(scaled_measurements_map)

print(f"Raw Measurements: {raw_measurements}")
print(f"Scaled Measurements (0-1 range): {scaled_measurements}")

# ==========================================
# 3. The filter() Function
# ==========================================
# Syntax: filter(function, iterable)
# Filters elements based on a function that returns a Boolean (True/False).

print("\n--- filter() Function ---")
accuracy_scores = [0.82, 0.54, 0.93, 0.48, 0.88, 0.99]

# Keep only models that satisfy accuracy threshold of >= 0.85
threshold_filter = lambda score: score >= 0.85

filtered_scores_obj = filter(threshold_filter, accuracy_scores)
top_performers = list(filtered_scores_obj)

print(f"All Model Scores: {accuracy_scores}")
print(f"Top Performers (accuracy >= 85%): {top_performers}")

# ==========================================
# 4. Combining Map & Filter in an ML pipeline
# ==========================================
# Let's say we have raw training temperatures, we want to:
# 1. Filter out erroneous negative temperatures (noise filtering)
# 2. Convert valid temperatures to Kelvin (feature transformation)

raw_temps = [25.0, -999.0, 30.5, -999.0, 22.1]  # -999 is placeholder for bad reading

# 1. Filter anomalies
valid_temps = filter(lambda t: t != -999.0, raw_temps)

# 2. Map to Kelvin (Celsius + 273.15)
kelvin_temps = map(lambda t: t + 273.15, valid_temps)

print("\n--- Combined Pipeline ---")
print(f"Raw inputs: {raw_temps}")
print(f"Processed Kelvin outputs: {list(kelvin_temps)}")

"""
Key Takeaways:
- Lambdas are limited to a single expression and implicitly return its evaluation.
- map() and filter() are lazy. They return iterators and do not evaluate until requested (e.g. converting to list).
- Code is much cleaner using lambdas in map/filter rather than writing full def statements for minor operations.

Interview Relevance:
- Explain what lambda functions are. What are their limitations? (Only 1 expression, no multi-line code blocks, no return keyword needed).
- How do map() and filter() save memory? (Explain lazy evaluation: elements are generated on-the-fly instead of storing the whole list in memory).
- Write a lambda to sort a list of tuples based on the second value. (E.g. `sorted(data, key=lambda x: x[1])`).

AI/ML Relevance:
- Pandas Apply: When manipulating DataFrame columns (e.g. preprocessing text), lambdas are passed to `.apply()` to do row-wise manipulations.
- Data pipelines: PySpark and TensorFlow Datasets use mapping structures heavily to clean and resize input batches before feeding models.
"""
