"""
Topic:
SQL Joins - INNER, LEFT, CROSS, and SELF Joins

Importance:
Databases are normalized into multiple tables to reduce redundancy.
Connecting relational tables (e.g. mapping customer attributes to transactions)
is a fundamental data aggregation step before feature engineering.

This file covers:
- Seeding employee and department relational tables
- INNER JOIN (intersection records)
- LEFT JOIN (all left tables records plus right matches)
- CROSS JOIN (Cartesian product combinations)
- SELF JOIN (parent-child hierarchy querying)
"""

import sqlite3
import pandas as pd

def run_joins_demo():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # Create two relational tables
    cursor.execute("""
    CREATE TABLE departments (
        dept_id INTEGER PRIMARY KEY,
        dept_name TEXT
    );
    """)
    
    cursor.execute("""
    CREATE TABLE employees (
        emp_id INTEGER PRIMARY KEY,
        name TEXT,
        dept_id INTEGER,
        manager_id INTEGER
    );
    """)
    
    # Seed data
    cursor.executemany("INSERT INTO departments VALUES (?, ?);", [
        (10, "HR"),
        (20, "Engineering"),
        (30, "Sales")
    ])
    
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?);", [
        (1, "Alice", 20, None),     # Alice is the CEO/Manager
        (2, "Bob", 20, 1),          # Bob reports to Alice (1)
        (3, "Charlie", 10, 1),      # Charlie reports to Alice (1)
        (4, "David", 99, 2)         # David belongs to department 99 (no matching department info)
    ])
    conn.commit()
    
    # ==========================================
    # SQL Query 1: INNER JOIN
    # ==========================================
    print("=======================================")
    print("Query 1: INNER JOIN (Only matching departments)")
    print("=======================================")
    query_1 = """
    SELECT e.name, d.dept_name 
    FROM employees e
    INNER JOIN departments d ON e.dept_id = d.dept_id;
    """
    df1 = pd.read_sql_query(query_1, conn)
    print(df1)
    
    # ==========================================
    # SQL Query 2: LEFT JOIN
    # ==========================================
    print("\n=======================================")
    print("Query 2: LEFT JOIN (Retain all employees, even without matching department)")
    print("=======================================")
    query_2 = """
    SELECT e.name, d.dept_name 
    FROM employees e
    LEFT JOIN departments d ON e.dept_id = d.dept_id;
    """
    df2 = pd.read_sql_query(query_2, conn)
    print(df2)
    
    # ==========================================
    # SQL Query 3: SELF JOIN
    # ==========================================
    print("\n=======================================")
    print("Query 3: SELF JOIN (Employee to Manager name mapping)")
    print("=======================================")
    query_3 = """
    SELECT 
        emp.name AS Employee, 
        mgr.name AS Manager
    FROM employees emp
    LEFT JOIN employees mgr ON emp.manager_id = mgr.emp_id;
    """
    df3 = pd.read_sql_query(query_3, conn)
    print(df3)
    print("=======================================")
    
    conn.close()

if __name__ == "__main__":
    run_joins_demo()

"""
Key Takeaways:
- INNER JOIN requires matching keys in both tables; LEFT JOIN retains all records from the left table even if no match exists.
- SELF JOIN requires applying distinct aliases to the same table (e.g. `employees emp` vs `employees mgr`).
- Joins combine data horizontally by appending columns.

Interview Relevance:
- What is the difference between LEFT JOIN and INNER JOIN? (INNER JOIN only returns rows where there is a match in both tables; LEFT JOIN returns all rows from the left table and matching rows from the right, filling missing right values with NULL).
- How do you emulate a FULL OUTER JOIN in SQLite? (Use a UNION of a LEFT JOIN and a RIGHT-simulated LEFT JOIN).
- What is a cross join and when is it useful? (A CROSS JOIN returns the Cartesian product of two tables. It is useful when you need to generate all possible combinations of features, like product-store-day grids).

AI/ML Relevance:
- Relational Merging: Merging user metrics, history transaction logs, and location metrics together into a unified feature set uses left joins.
- Cartesian Seeding: Generating all potential user-item pair records for Recommendation Systems uses CROSS JOIN statements.
"""
