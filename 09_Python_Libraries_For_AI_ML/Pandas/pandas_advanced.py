"""
Topic:
Advanced Pandas Operations: Grouping, Transformations, Merging and Joining

Importance:
Analyzing aggregates across categories, applying custom mappings, and merging split relational datasets
into consolidated formats is a standard feature engineering prerequisite.

This file covers:
- Groupby and Aggregation functions (groupby, agg, value_counts)
- Column transformation maps (map, apply, lambdas)
- Adding/dropping columns
- DataFrame Merging (inner/left joins) and Concatenation
"""

import pandas as pd

# ==========================================
# 1. Setup Sample DataFrames
# ==========================================
employee_data = {
    "Emp_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Dept": ["HR", "IT", "IT", "Sales", "HR"],
    "Salary": [70000, 85000, 95000, 60000, 72000]
}
df_emp = pd.DataFrame(employee_data)

dept_info = {
    "Dept": ["HR", "IT", "Sales", "Marketing"],
    "Budget": [500000, 1200000, 800000, 300000]
}
df_dept = pd.DataFrame(dept_info)

print("Employee DataFrame:\n", df_emp)
print("\nDepartment DataFrame:\n", df_dept)

# ==========================================
# 2. Transformations (apply, map, edit columns)
# ==========================================
print("\n--- Transformations ---")

# Using map: Translate Dept to custom codes
dept_mapping = {"HR": "Human Resources", "IT": "Information Technology", "Sales": "Sales Division"}
df_emp["Dept_Full"] = df_emp["Dept"].map(dept_mapping)

# Using apply: Apply a custom logic function to calculate tax (e.g. 10% if salary > 75000, else 5%)
def calculate_tax(salary):
    if salary > 75000:
        return salary * 0.10
    else:
        return salary * 0.05

df_emp["Tax"] = df_emp["Salary"].apply(calculate_tax)

# Using apply with lambda (inline anonymous function)
# Double the tax calculated
df_emp["Double_Tax"] = df_emp["Tax"].apply(lambda x: x * 2)

print("\nDataFrame after mappings & applies:\n", df_emp)

# Dropping unnecessary columns
df_emp = df_emp.drop(columns=["Double_Tax"])
print("\nAfter dropping column 'Double_Tax':\n", df_emp)

# ==========================================
# 3. Grouping & Aggregations
# ==========================================
print("\n--- Grouping & Aggregations ---")

# value_counts: Count occurence of categories
print("Value counts for Dept:\n", df_emp["Dept"].value_counts())

# Groupby: Get average salary per department
avg_salary_dept = df_emp.groupby("Dept")["Salary"].mean()
print("\nAverage salary per Dept:\n", avg_salary_dept)

# Multi-aggregation: sum of salary, mean of tax, count of employees per Dept
agg_dept = df_emp.groupby("Dept").agg(
    Total_Salary=("Salary", "sum"),
    Average_Tax=("Tax", "mean"),
    Employee_Count=("Emp_ID", "count")
)
print("\nAggregated table per Dept:\n", agg_dept)

# ==========================================
# 4. Merging & Concatenation
# ==========================================
print("\n--- Merging & Concatenation ---")

# Merge: relational databases join (join df_emp and df_dept on 'Dept')
# Inner Join: Keeps only matched departments (Marketing is dropped since no employee in Marketing)
df_inner = pd.merge(df_emp, df_dept, on="Dept", how="inner")
print("Inner Merge:\n", df_inner)

# Left Join: Keeps all rows from left (df_emp), inserts NaN for unmatched right fields
df_left = pd.merge(df_emp, df_dept, on="Dept", how="left")
print("\nLeft Merge:\n", df_left)

# Concatenation: Stacking DataFrames vertically (axis=0) or horizontally (axis=1)
# Create a new employee entry DataFrame
new_emp = pd.DataFrame({
    "Emp_ID": [106],
    "Name": ["Frank"],
    "Dept": ["Marketing"],
    "Salary": [65000]
})
print("\nNew Employee entry:\n", new_emp)

# Concatenate vertically
df_concat_vertical = pd.concat([df_emp, new_emp], axis=0, ignore_index=True)
print("\nVertically concatenated employees list:\n", df_concat_vertical)

"""
Key Takeaways:
- `map()` is used for element-wise values translation using a dictionary or function (Series only).
- `apply()` applies custom complex functions or lambdas along DataFrame rows/columns or Series.
- `groupby()` aggregates columns based on categorical parameters.
- `pd.merge()` performs relational database joining (inner, left, right, outer).
- `pd.concat()` combines/stacks datasets vertically (axis=0) or horizontally (axis=1).

Interview Relevance:
- What is the difference between `map` and `apply`? (`map` works element-wise on a Series by mapping keys to dictionary values; `apply` can run custom functions on Series or columns/rows of DataFrames).
- Difference between inner merge and left merge? (Inner merge keeps only rows with matching keys in both DataFrames; Left merge preserves all rows from the left DataFrame, inserting NaNs for missing keys on the right).
- How do you perform SQL-like aggregations in Pandas? (Combine `groupby()` with `.agg()`, specifying column targets and function strings: `df.groupby('category').agg(mean_val=('col', 'mean'))`).

AI/ML Relevance:
- Category Encoding: Translating labels to integers is done using `.map({'Yes': 1, 'No': 0})`.
- Feature Engineering: Aggregating user interaction logs (clicks per user id) uses `.groupby('user_id').agg({'click': 'count'})` to create user profiles.
- Consolidated Datasets: Merging transactional features with user profile databases is performed using `pd.merge(transactions, profiles, on='user_id', how='left')`.
"""
