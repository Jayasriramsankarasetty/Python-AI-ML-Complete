# SQL Filtering & Sorting: WHERE, ORDER BY, & LIMIT

This folder covers techniques for filtering rows, matching text patterns, sorting values, and limiting return result counts.

---

## Key SQL Keywords

1. **`WHERE`**:
   * Conditional filter statement targeting specific row criteria.
   * Operators: `=`, `!=`, `>`, `<`, `>=`, `<=`, `AND`, `OR`, `NOT`.
2. **`IN`**:
   * Matches values against a predefined set/list.
   * Example: `WHERE department IN ('Engineering', 'Sales')`
3. **`BETWEEN`**:
   * Matches values within an inclusive range.
   * Example: `WHERE salary BETWEEN 50000 AND 100000`
4. **`LIKE`**:
   * Standard wild card text matches.
   * `%` matches zero or more characters; `_` matches a single character.
   * Example: `WHERE name LIKE 'A%'` (names starting with 'A').
5. **`ORDER BY`**:
   * Sorts query outputs in Ascending (`ASC`, default) or Descending (`DESC`) order.
6. **`LIMIT`**:
   * Caps the number of records returned. Essential for pagination or top-N queries.

---

## Submodule Contents

* [filter_sort.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/filtering_sorting/filter_sort.py):
  * Executable SQLite script seeding mock records to demonstrate logical conditions, wildcards, sorting, and LIMIT configurations.
