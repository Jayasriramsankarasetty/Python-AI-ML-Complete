"""
Topic:
SQL Aggregations - GROUP BY and HAVING

Importance:
Summarizing transactional records (e.g. counting clicks per user, averaging daily purchases)
is crucial to compile training arrays for regression or classification models.

This file covers:
- Seeding mock employees table
- Aggregation functions: COUNT, SUM, AVG, MAX, MIN
- GROUP BY groupings
- HAVING group filters
"""

import sqlite3
import pandas as pd

def run_aggregation_demo():
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
        (6, "Frank", "Engineering", 80000.0),
        (7, "Grace", "HR", 70000.0)
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?);", employees_data)
    conn.commit()
    
    # ==========================================
    # SQL Query 1: Basic Group Aggregation (GROUP BY)
    # ==========================================
    print("=======================================")
    print("Query 1: Employee count, total salary, and average salary per department")
    print("=======================================")
    query_1 = """
    SELECT 
        department,
        COUNT(emp_id) AS Employee_Count,
        SUM(salary) AS Total_Salary_Spend,
        AVG(salary) AS Average_Salary,
        MAX(salary) AS Highest_Salary,
        MIN(salary) AS Lowest_Salary
    FROM employees
    GROUP BY department;
    """
    df1 = pd.read_sql_query(query_1, conn)
    print(df1)
    
    # ==========================================
    # SQL Query 2: Group Filtering (HAVING)
    # ==========================================
    print("\n=======================================")
    print("Query 2: Departments spending more than 120,000 in total salary")
    print("=======================================")
    query_2 = """
    SELECT 
        department,
        SUM(salary) AS Total_Salary_Spend
    FROM employees
    GROUP BY department
    HAVING SUM(salary) > 120000;
    """
    df2 = pd.read_sql_query(query_2, conn)
    print(df2)
    print("=======================================")
    
    conn.close()

if __name__ == "__main__":
    run_aggregation_demo()

"""
Key Takeaways:
- Aggregations reduce data rows into summaries.
- GROUP BY partitions rows into subset buckets based on column categories.
- HAVING filters the output of GROUP BY, whereas WHERE filters input rows before GROUP BY.

Interview Relevance:
- What is the difference between WHERE and HAVING? (WHERE filters individual rows before grouping; HAVING filters aggregated groups after GROUP BY).
- Can you use aggregate functions in the WHERE clause? (No, because individual rows do not contain group aggregates).
- How does COUNT(*) differ from COUNT(column_name)? (COUNT(*) counts all rows including NULL rows; COUNT(column_name) counts only rows where the specified column is not NULL).

AI/ML Relevance:
- Feature Engineering: Summing total transaction value or counting login events per customer creates key feature columns for predictive modeling.
- Data Summarization: Aggregating statistics checks consistency of labels across subgroups before splitting dataset arrays.
"""
