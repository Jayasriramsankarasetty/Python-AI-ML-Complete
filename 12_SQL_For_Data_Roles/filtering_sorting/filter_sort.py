"""
Topic:
SQL Filtering & Sorting - WHERE, LIKE, IN, BETWEEN, ORDER BY, and LIMIT

Importance:
Data extraction pipelines rarely extract entire raw tables.
Filtering down records to relevant temporal bounds, locations, or numeric ranges
improves retrieval efficiency before data transformation.

This file covers:
- Seeding mock employee datasets
- Logical filters (WHERE, AND, BETWEEN)
- Wildcards matching (LIKE)
- Set checks (IN)
- Output sorting (ORDER BY ASC/DESC)
- Fetch limits (LIMIT)
"""

import sqlite3
import pandas as pd

def run_filtering_demo():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE employees (
        emp_id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary REAL,
        city TEXT
    );
    """)
    
    # Seed mock records
    employees_data = [
        (1, "Alice", "Engineering", 95000.0, "New York"),
        (2, "Bob", "Sales", 60000.0, "Los Angeles"),
        (3, "Charlie", "Engineering", 110000.0, "Chicago"),
        (4, "David", "HR", 55000.0, "New York"),
        (5, "Eva", "Sales", 65000.0, "Los Angeles"),
        (6, "Frank", "Engineering", 80000.0, "San Francisco"),
        (7, "Grace", "HR", 70000.0, "Chicago")
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?);", employees_data)
    conn.commit()
    
    # ==========================================
    # SQL Query 1: AND, BETWEEN Ranges
    # ==========================================
    print("=======================================")
    print("Query 1: Engineers earning between 80,000 and 100,000")
    print("=======================================")
    query_1 = """
    SELECT name, department, salary 
    FROM employees 
    WHERE department = 'Engineering' 
      AND salary BETWEEN 80000 AND 100000;
    """
    df1 = pd.read_sql_query(query_1, conn)
    print(df1)
    
    # ==========================================
    # SQL Query 2: IN set filters, LIKE text matchers
    # ==========================================
    print("\n=======================================")
    print("Query 2: Employees located in New York or Chicago whose names start with 'A' or 'C'")
    print("=======================================")
    query_2 = """
    SELECT name, city 
    FROM employees 
    WHERE city IN ('New York', 'Chicago')
      AND (name LIKE 'A%' OR name LIKE 'C%');
    """
    df2 = pd.read_sql_query(query_2, conn)
    print(df2)
    
    # ==========================================
    # SQL Query 3: ORDER BY & LIMIT (Top Salaries)
    # ==========================================
    print("\n=======================================")
    print("Query 3: Top 3 highest-earning employees")
    print("=======================================")
    query_3 = """
    SELECT name, salary 
    FROM employees 
    ORDER BY salary DESC 
    LIMIT 3;
    """
    df3 = pd.read_sql_query(query_3, conn)
    print(df3)
    print("=======================================")
    
    conn.close()

if __name__ == "__main__":
    run_filtering_demo()

"""
Key Takeaways:
- WHERE filters rows before grouping or projecting.
- LIKE '%' matches wildcards of any text length; '_' matches exactly one character.
- ORDER BY sorts column elements; DESC sets descending order, ASC sets ascending (default).
- LIMIT constraints truncate return counts, improving processing speed.

Interview Relevance:
- What is the difference between WHERE and HAVING? (WHERE filters records *before* any groupings are computed; HAVING filters grouped summary metrics *after* GROUP BY executes).
- How do you select rows where a column is NULL? (Use `WHERE column_name IS NULL`. Do not use `WHERE column_name = NULL` because NULL compared to anything, even itself, returns NULL/False).
- Explain the difference between LIKE and IN operators. (LIKE is used for pattern matching text with wildcards; IN is used to check if a value matches any element in a specific list).

AI/ML Relevance:
- Dataset Splitting: Querying subsets of data (e.g. `WHERE train_flag = 1`) allows loading specific train/test folds directly.
- Temporal Partitioning: Applying dates filters (`WHERE date BETWEEN '2026-01-01' AND '2026-06-30'`) ensures proper out-of-time validation splits.
"""
