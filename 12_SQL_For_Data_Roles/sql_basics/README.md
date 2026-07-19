# SQL Basics: Select & Alias Projections

This folder covers the entry points of SQL database querying, focusing on column projections, deduplications, and output aliases.

---

## Key SQL Keywords

1. **`SELECT`**:
   * Specifies which database columns to query.
   * Syntax: `SELECT column1, column2 FROM table_name;`
   * Use `SELECT *` to retrieve all columns.
2. **`DISTINCT`**:
   * Removes duplicate rows from the query output.
   * Syntax: `SELECT DISTINCT column1 FROM table_name;`
3. **`AS` (Alias)**:
   * Replaces column or table output headings with temporary descriptive names.
   * Syntax: `SELECT column_name AS custom_alias FROM table_name;`

---

## Submodule Contents

* [basics.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/sql_basics/basics.py):
  * Sets up a SQLite in-memory database containing a mock `employees` table.
  * Runs projections selecting specific columns, distinct departments, and renaming columns using SQL aliases.
