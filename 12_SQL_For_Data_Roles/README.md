# SQL for Data Roles (Module 12)

Structured Query Language (SQL) is the industrial standard for storing, retrieving, and manipulating transactional and analytical databases. For data science and ML engineering roles, SQL is a core requirement to query training features from data warehouses.

---

## Folder Contents

This module covers SQL topics from beginner to interview levels, implemented using interactive, executable Python SQLite scripts:

1. [sql_basics/](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/sql_basics/):
   * Projections using SELECT, DISTINCT, and column aliasing.
2. [filtering_sorting/](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/filtering_sorting/):
   * Conditional selection using WHERE, IN, LIKE patterns, ranges, ORDER BY, and LIMIT.
3. [joins/](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/joins/):
   * Connecting relational tables using INNER JOIN, LEFT JOIN, CROSS JOIN, and SELF JOIN.
4. [aggregation/](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/aggregation/):
   * Summarizing data tables using grouping functions and filtering on metrics using HAVING.
5. [subqueries/](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/subqueries/):
   * Nested query logic in SELECT, WHERE, and FROM clauses.
6. [window_functions/](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/window_functions/):
   * Calculating running values, relative ranks, and time steps using PARTITION BY.
7. [interview_questions/](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/12_SQL_For_Data_Roles/interview_questions/):
   * High-frequency SQL interview questions (LeetCode database templates) and solutions.

---

## Running the Interactive Demos
Since local setups may not have MySQL or PostgreSQL installed, we build our database queries inside Python script files using Python's built-in `sqlite3` engine. Running any script will build an in-memory database, seed mock tables, execute standard SQL queries, and print results.

Example:
```bash
python sql_basics/basics.py
```
