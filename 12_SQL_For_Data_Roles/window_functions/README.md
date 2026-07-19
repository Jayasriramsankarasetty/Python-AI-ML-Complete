# SQL Window Functions: PARTITION BY & OVER

Window functions perform calculations across a set of table rows that are related to the current row, without collapsing the rows into a single output row (unlike standard GROUP BY aggregates).

---

## Key SQL Concepts

1. **`OVER` Clause**:
   * Marks a window function. Specifies how to partition and order the rows before applying the function.
2. **`PARTITION BY`**:
   * Divides rows into groups (windows) to apply calculations. If omitted, the entire table is treated as one window.
3. **`ORDER BY`**:
   * Sorts rows inside each partition.
4. **Key Functions**:
   * **`ROW_NUMBER()`**: Assigns a unique sequential integer starting from 1.
   * **`RANK()`**: Assigns ranks, skipping values in case of ties.
   * **`DENSE_RANK()`**: Assigns ranks, without skipping numbers in case of ties.
   * **`LAG()`**: Retrieves values from a preceding row.
   * **`LEAD()`**: Retrieves values from a succeeding row.

---

## Submodule Contents

* [window.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/window_functions/window.py):
  * Executable SQLite script seeding employees to run `ROW_NUMBER()`, `DENSE_RANK()`, `LAG()`, and `LEAD()` functions.
