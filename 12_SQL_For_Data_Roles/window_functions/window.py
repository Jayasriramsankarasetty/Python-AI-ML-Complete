"""
Topic:
SQL Window Functions - PARTITION BY, RANK, DENSE_RANK, LAG, and LEAD

Importance:
Window functions permit comparing rows to other rows in the same partition
(e.g., finding salary rank within a department, or calculating transaction time differences)
without collapsing the original rows. This is essential for sequence feature engineering.

This file covers:
- Seeding employee records with departments
- Ranking employees by salary within each department (DENSE_RANK)
- Assigning unique integers within departments (ROW_NUMBER)
- Fetching preceding salary values to check salary differences (LAG)
"""

import sqlite3
import pandas as pd

def run_window_demo():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE employees (
        emp_id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary REAL
    );
    """)
    
    # Seed mock records
    employees_data = [
        (1, "Alice", "Engineering", 95000.0),
        (2, "Bob", "Sales", 60000.0),
        (3, "Charlie", "Engineering", 110000.0),
        (4, "David", "HR", 55000.0),
        (5, "Eva", "Sales", 65000.0),
        (6, "Frank", "Engineering", 95000.0),  # tie salary with Alice
        (7, "Grace", "HR", 70000.0)
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?);", employees_data)
    conn.commit()
    
    # ==========================================
    # SQL Query 1: ROW_NUMBER vs DENSE_RANK
    # ==========================================
    print("=======================================")
    print("Query 1: Row sequence and Dense Salary Rank within departments")
    print("=======================================")
    query_1 = """
    SELECT 
        department,
        name,
        salary,
        ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS Dept_Row_Num,
        DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS Dept_Salary_Rank
    FROM employees;
    """
    df1 = pd.read_sql_query(query_1, conn)
    print(df1)
    
    # ==========================================
    # SQL Query 2: LAG (Preceding values checks)
    # ==========================================
    print("\n=======================================")
    print("Query 2: Comparing employee salary with the next lowest salary in their department")
    print("=======================================")
    query_2 = """
    SELECT 
        department,
        name,
        salary,
        LAG(salary, 1) OVER(PARTITION BY department ORDER BY salary DESC) AS Higher_Salary_Neighbor,
        salary - LAG(salary, 1) OVER(PARTITION BY department ORDER BY salary DESC) AS Salary_Difference
    FROM employees;
    """
    df2 = pd.read_sql_query(query_2, conn)
    print(df2)
    print("=======================================")
    
    conn.close()

if __name__ == "__main__":
    run_window_demo()

"""
Key Takeaways:
- Window functions retain row-level granularity while computing group stats.
- DENSE_RANK does not skip ranks in case of ties; RANK does skip ranks.
- LAG accesses previous rows; LEAD accesses subsequent rows inside the sorted window partition.

Interview Relevance:
- What is the difference between RANK and DENSE_RANK? (RANK skips rank numbers in case of duplicate ties, e.g., 1, 2, 2, 4; DENSE_RANK does not skip, e.g., 1, 2, 2, 3).
- Can you use window functions in the WHERE clause? (No, because window functions are calculated in the select phase, which is after the WHERE clause filters rows).
- What does PARTITION BY do? (It divides the result set into partitions to apply the window function to each partition independently).

AI/ML Relevance:
- Feature Engineering: Calculating row offsets using LAG (e.g. time delta between current log and previous log) creates crucial session sequence features.
- Sequence Analysis: Sorting transaction sequences per client ID helps compile cron logs for Churn prediction models.
"""
