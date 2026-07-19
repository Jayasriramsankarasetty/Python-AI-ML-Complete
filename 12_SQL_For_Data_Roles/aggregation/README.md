# SQL Aggregation & Grouping: GROUP BY & HAVING

This folder covers summarizing tables into group metrics (like counts, averages, and sums) and filtering those groups.

---

## Key SQL Keywords

1. **Aggregation Functions**:
   * **`COUNT()`**: Counts rows.
   * **`SUM()`**: Calculates the total sum of a numerical column.
   * **`AVG()`**: Calculates the average of a numerical column.
   * **`MIN()`**: Finds the minimum value.
   * **`MAX()`**: Finds the maximum value.
2. **`GROUP BY`**:
   * Collapses multiple rows into groups based on common values in specified columns.
3. **`HAVING`**:
   * Filters group aggregates.
   * *Critical Difference*: `WHERE` filters raw rows *before* grouping; `HAVING` filters aggregated values *after* grouping.

---

## Submodule Contents

* [aggregate.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/aggregation/aggregate.py):
  * Executable SQLite script seeding employees to run sum/avg calculations, group by departments, and apply HAVING thresholds.
