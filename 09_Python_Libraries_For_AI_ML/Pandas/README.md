# Pandas Data Manipulation Guide

Pandas is the primary library for data wrangling, cleaning, transformation, and analysis in Python. It introduces two primary data structures:
1. **Series**:
   * A 1D labeled homogeneous array.
2. **DataFrame**:
   * A 2D labeled tabular structure with rows and columns (heterogeneous allowed).

---

## Index Selection: loc vs iloc

Selecting rows and columns in a DataFrame uses indexing accessors:

| Selection Method | Selector Type | Reference Style | Inclusive/Exclusive Bounds |
| :--- | :--- | :--- | :--- |
| **`df.loc[...]`** | **Label-based** | Uses index names and column header titles (e.g. `df.loc[0, 'Age']`). | **Inclusive** of both start and end indexes (e.g. `'Row1':'Row3'` includes Row3). |
| **`df.iloc[...]`** | **Integer-position based** | Uses integer index numbers (e.g. `df.iloc[0, 1]`). | Standard Python slicing **Exclusive** of the end bound (e.g. `0:3` gets indexes 0, 1, 2). |

---

## Files in this Folder

1. [pandas_basics.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/09_Python_Libraries_For_AI_ML/Pandas/pandas_basics.py):
   * DataFrame creation, data exploration and summaries, `loc`/`iloc` selections, boolean filtering, and handling missing data (`dropna`/`fillna`).
2. [pandas_advanced.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/09_Python_Libraries_For_AI_ML/Pandas/pandas_advanced.py):
   * Mapping and applying functions, groupby aggregations, value counting, merging, joining, and concatenation of DataFrames.
