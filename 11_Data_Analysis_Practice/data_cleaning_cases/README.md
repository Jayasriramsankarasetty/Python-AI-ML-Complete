# Data Cleaning Best Practices

Data cleaning is the process of detecting and correcting corrupt, inaccurate, or incomplete records from a dataset. Messy data degrades model performance and introduces biases.

---

## Messy Data Problems & Solutions

1. **Duplicate Entries**:
   * *Problem*: Identical records inflate dataset size and artificially skew metrics.
   * *Solution*: Identify using `df.duplicated()` and remove using `df.drop_duplicates()`.
2. **Missing/Null Values**:
   * *Problem*: Many models fail to process mathematical calculations containing NaN values.
   * *Solution*: Impute defaults (mean, median, mode) or drop rows/columns containing missing values.
3. **Inconsistent Categorical Strings**:
   * *Problem*: Casing errors (e.g. `'New York'`, `'new york'`, `'NY'`) are treated as distinct classes.
   * *Solution*: Standardize casing using `.str.lower()` or `.str.title()`, and map abbreviations.
4. **Inconsistent Date/Time Formats**:
   * *Problem*: Dates stored as mismatched strings (e.g. `'25-12-2026'`, `'2026/12/25'`) cannot be sorted or partitioned.
   * *Solution*: Parse using `pd.to_datetime(..., errors='coerce')` to standardize to ISO formats.

---

## Submodule Contents

* [data_cleaning.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/11_Data_Analysis_Practice/data_cleaning_cases/data_cleaning.py):
  * Practical case study processing a messy list of dictionary elements, parsing them into a clean Pandas DataFrame, resolving duplicates, handling nulls, normalizing string casing, and standardizing dates.
