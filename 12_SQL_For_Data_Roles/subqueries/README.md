# SQL Subqueries: Nested Queries

This folder covers nesting queries inside outer queries (nested SELECTs, filtering using WHERE, and derived tables using FROM).

---

## Types of Subqueries

1. **Scalar Subqueries**:
   * Returns a single value (one row, one column).
   * Example: Select employees whose salary is greater than the company average:
     `SELECT name FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);`
2. **Multi-Row Subqueries**:
   * Returns a list of values (one column, multiple rows). Used with `IN`, `ANY`, or `ALL`.
   * Example: `SELECT name FROM employees WHERE dept_id IN (SELECT dept_id FROM departments WHERE location = 'NY');`
3. **Correlated Subqueries**:
   * Inner query references a column in the outer query. Evaluated once for each row processed by the outer query.
4. **Derived Tables (Subquery in FROM)**:
   * Subquery result behaves as a temporary table. Must have an alias.
   * Example: `SELECT * FROM (SELECT name, salary * 12 AS annual FROM employees) WHERE annual > 100000;`

---

## Submodule Contents

* [subqueries.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/subqueries/subqueries.py):
  * Executable SQLite script seeding employees to run scalar subqueries (above average salary comparison) and derived tables computations.
