# SQL Relational Joins: INNER, LEFT, CROSS, & SELF

This folder covers techniques for combining columns from multiple tables using shared primary/foreign key connections.

---

## Types of Joins

1. **`INNER JOIN`**:
   * Returns records that have matching values in both tables.
2. **`LEFT JOIN`** (or `LEFT OUTER JOIN`):
   * Returns all records from the left table, and the matched records from the right table. Fill unmatched right values with `NULL`.
3. **`RIGHT JOIN`** (or `RIGHT OUTER JOIN`):
   * Returns all records from the right table, and the matched records from the left table. (Simulated in SQLite using a LEFT JOIN with table arguments swapped).
4. **`FULL OUTER JOIN`**:
   * Returns all records when there is a match in either left or right table. (Simulated in SQLite using a UNION of LEFT and RIGHT joins).
5. **`CROSS JOIN`**:
   * Returns the Cartesian product of the two tables (combines every row of the first table with every row of the second table).
6. **`SELF JOIN`**:
   * Joining a table to itself. Useful to query hierarchical structures (e.g. employee-to-manager relationships).

---

## Submodule Contents

* [joins.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/joins/joins.py):
  * Executable SQLite script seeding mock `employees` and `departments` tables to perform INNER, LEFT, CROSS, and SELF joins.
