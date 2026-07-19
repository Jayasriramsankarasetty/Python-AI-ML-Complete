"""
Topic:
Data Cleaning Case Study

Importance:
Real-world data is noisy, dirty, and contains inconsistent entries.
A machine learning engineer must know how to programmatically resolve duplicate values,
standardize categorical spellings, clean date formats, and impute missing fields.

This file covers:
- Standardizing column headings string casings
- Removing duplicate rows
- Standardizing mixed date formats using pd.to_datetime
- Standardizing category spellings and white spaces
- Imputing missing numerical and categorical fields
"""

import pandas as pd
import numpy as np

# ==========================================
# 1. Setup Messy Raw Dataset
# ==========================================
# Mock messy dataset containing duplicates, casing errors, missing values, and date format mismatches.
raw_messy_records = [
    {"user_id": 101, "name": "Alice", "JOIN_DATE": "2026-01-15", "city": "New York ", "salary": 75000},
    {"user_id": 102, "name": "bob", "JOIN_DATE": "25/02/2026", "city": "los angeles", "salary": 82000},
    {"user_id": 103, "name": "Charlie", "JOIN_DATE": "2026/03/10", "city": "Chicago", "salary": np.nan},  # null salary
    {"user_id": 101, "name": "Alice", "JOIN_DATE": "2026-01-15", "city": "New York ", "salary": 75000},  # duplicate row
    {"user_id": 104, "name": "David", "JOIN_DATE": "invalid_date", "city": np.nan, "salary": 60000},    # null city & invalid date
    {"user_id": 105, "name": "Eva", "JOIN_DATE": "2026-04-05", "city": "new york", "salary": 90000}    # inconsistent city casing
]

df = pd.DataFrame(raw_messy_records)
print("=======================================")
print("Original Messy DataFrame:")
print("=======================================")
print(df)

# ==========================================
# 2. Step-by-Step Data Cleaning
# ==========================================

# Step A: Standardize Column Names
# Rename column headers to lower case for uniformity
df.columns = df.columns.str.lower()
print("\n--- Column names standardized to lowercase: ---")
print(df.columns.tolist())

# Step B: Remove Duplicates
print(f"\nDuplicates count: {df.duplicated().sum()}")
df = df.drop_duplicates()
print("DataFrame after removing duplicates:\n", df)

# Step C: Standardize Categorical Strings (City Column)
# 1. Strip leading/trailing whitespaces: "New York " -> "New York"
df["city"] = df["city"].str.strip()
# 2. Standardize casing to Title Case: "los angeles" -> "Los Angeles", "new york" -> "New York"
df["city"] = df["city"].str.title()
print("\nAfter cleaning city casing and spaces:\n", df)

# Step D: Standardize Date Formats
# pd.to_datetime automatically parses mixed formats. errors='coerce' turns invalid formats ("invalid_date") to NaT (Not a Time)
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")
print("\nAfter parsing date formats:\n", df)

# Step E: Handle Missing/Null Values
# 1. Fill missing city with "Unknown"
df["city"] = df["city"].fillna("Unknown")
# 2. Impute missing salary with the median salary
median_sal = df["salary"].median()
df["salary"] = df["salary"].fillna(median_sal)
# 3. Handle NaT date by forwarding fill or setting a default (we will drop the row if date is critical, or fill with median date)
# Let's fill the missing date with the earliest date in the column
min_date = df["join_date"].min()
df["join_date"] = df["join_date"].fillna(min_date)

print("\n=======================================")
print("Final Cleaned DataFrame:")
print("=======================================")
print(df)
print("=======================================")

"""
Key Takeaways:
- Standardizing column headers to lowercase simplifies indexing references.
- `pd.to_datetime(..., errors='coerce')` converts invalid dates to NaT (null date markers) instead of crashing.
- String accessors like `.str.strip()` and `.str.title()` standardizes category keys.

Interview Relevance:
- What does errors='coerce' do in pd.to_datetime()? (It parses valid dates, and converts any unparseable invalid text strings directly to NaT).
- How do you drop duplicate rows based on only specific column subset fields? (Pass the subset parameter: `df.drop_duplicates(subset=['col1', 'col2'])`).
- What is the difference between string lower(), upper(), and title()? (`lower()` makes all characters lowercase; `upper()` makes them uppercase; `title()` capitalizes only the first letter of each word).

AI/ML Relevance:
- String matching: Mismatched cases ('New York' vs 'new york') create redundant feature dummy columns during One-Hot encoding. Cleaning text saves memory bounds.
- Normalization: Mismatched dates crash time series forecasting models. Normalizing dates coordinates chronological sorting indices.
"""
