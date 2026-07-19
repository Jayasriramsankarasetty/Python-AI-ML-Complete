"""
Topic:
Pandas DataFrame Basics

Importance:
Feature matrices and datasets exist as tabular columns in real-world ML tasks.
Inspecting structural shapes, subsets selection (loc/iloc), condition queries, and
cleaning null inputs forms 80% of data pre-processing workloads.

This file covers:
- DataFrame creation from a dictionary
- Basic data inspection methods (head, info, describe, shape)
- Index selection (loc vs iloc)
- Boolean filtering / querying
- Handling missing data (isnull, dropna, fillna)
"""

import pandas as pd
import numpy as np

# ==========================================
# 1. DataFrame Creation & Inspection
# ==========================================
print("--- DataFrame Creation & Inspection ---")
raw_data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, np.nan, 22, 28],  # np.nan represents missing value
    "City": ["New York", "Los Angeles", "Chicago", np.nan, "New York"],
    "Salary": [70000, 85000, 95000, 60000, np.nan]
}

# Create DataFrame
df = pd.DataFrame(raw_data)
print("Created DataFrame:\n", df)

# Shape
print("\nShape of DataFrame:", df.shape)  # expected (5, 4)

# Head: view first N rows
print("\nFirst 3 rows:\n", df.head(3))

# Info: datatypes, non-null counts, memory footprint
print("\nDataFrame Summary Info:")
df.info()

# Describe: numerical summary statistics
print("\nNumerical statistics summary:\n", df.describe())

# ==========================================
# 2. Index Selection (loc vs iloc)
# ==========================================
print("\n--- Index Selection (loc vs iloc) ---")
# Set custom row index names
df_indexed = df.copy()
df_indexed.index = ["Row_A", "Row_B", "Row_C", "Row_D", "Row_E"]
print("DataFrame with custom index:\n", df_indexed)

# loc: Label-based selection
# Select value at row 'Row_B', column 'City'
print("\nloc (Row_B, City):", df_indexed.loc["Row_B", "City"])  # Los Angeles
# Slice: Row_A to Row_C (inclusive), columns Name and Age
print("loc slice:\n", df_indexed.loc["Row_A":"Row_C", ["Name", "Age"]])

# iloc: Integer-position based selection
# Select value at row index 1, column index 2
print("\niloc (row 1, col 2):", df_indexed.iloc[1, 2])  # Los Angeles
# Slice: first 3 rows (0, 1, 2), first 2 columns (0, 1)
print("iloc slice:\n", df_indexed.iloc[:3, :2])

# ==========================================
# 3. Boolean Filtering
# ==========================================
print("\n--- Boolean Filtering ---")
# Filter rows where Age > 24
age_filter = df["Age"] > 24
print("Rows where Age > 24:\n", df[age_filter])

# Combining multiple conditions using bitwise operators (&, |)
# Filter rows where Age > 24 AND City is "New York"
ny_filter = (df["Age"] > 24) & (df["City"] == "New York")
print("Rows where Age > 24 AND City is New York:\n", df[ny_filter])

# ==========================================
# 4. Handling Missing Data
# ==========================================
print("\n--- Handling Missing Data ---")
# Detect nulls
print("Null locations:\n", df.isnull())
print("\nSum of nulls per column:\n", df.isnull().sum())

# Option A: Drop rows with any missing value
df_dropped = df.dropna()
print("\nDropped rows with nulls:\n", df_dropped)

# Option B: Fill missing values with defaults
df_filled = df.copy()
# Fill missing age with mean age
mean_age = df_filled["Age"].mean()
df_filled["Age"] = df_filled["Age"].fillna(mean_age)
# Fill missing City with "Unknown"
df_filled["City"] = df_filled["City"].fillna("Unknown")
# Fill missing Salary with median salary
median_salary = df_filled["Salary"].median()
df_filled["Salary"] = df_filled["Salary"].fillna(median_salary)

print("\nFilled values:\n", df_filled)

"""
Key Takeaways:
- DataFrame is a 2D labeled spreadsheet structure with heterogeneous columns.
- `loc` accesses elements using index names (inclusive bounds); `iloc` accesses elements using integer offset positions (exclusive bounds).
- Boolean combinations require bitwise operators `&` and `|` wrapped in parentheses for precedence alignment.
- Missing values (`np.nan`) can be detected using `isnull()`, dropped using `dropna()`, or imputed using `fillna()`.

Interview Relevance:
- Difference between `loc` and `iloc`? (`loc` is label-based and inclusive of bounds; `iloc` is integer-position based and exclusive of the end index).
- How do you query a DataFrame with multiple criteria? (Use boolean masks with bitwise `&` or `|` operators, ensuring each condition is wrapped in parentheses: `df[(df['col1'] > A) & (df['col2'] == B)]`).
- How to check for missing values in a DataFrame? (Use `df.isnull().sum()` to get counts of missing fields in each column).

AI/ML Relevance:
- Data Cleaning: Imputing missing values (`df.fillna(df.mean())`) is required before passing feature matrix inputs to scikit-learn models (which do not support NaN entries).
- Feature Extraction: Splitting features and labels from loaded CSV files utilizes label slicing (`X = df.loc[:, ['Age', 'Salary']]`).
"""
