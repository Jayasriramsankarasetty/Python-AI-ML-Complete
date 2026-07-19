"""
Topic:
SQL Subqueries - Scalar Subqueries and Derived Tables (Nested Queries)

Importance:
Many logical queries cannot be answered in a single flat SQL pass.
For instance, selecting records above a dynamic mean salary requires calculating the mean
first using an inner query, then filtering columns in the outer pass.

This file covers:
- Seeding mock employees table
- Scalar subquery in WHERE (comparing against average salary)
- Derived tables inside FROM (calculating temporary aggregates)
- Correlated subqueries (comparing values within subgroups)
"""

import sqlite3
import pandas as pd

def run_subqueries_demo():
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
    # SQL Query 1: Scalar Subquery in WHERE
    # ==========================================
    # Goal: Get all employees earning above the company average salary.
    # Company average salary = (95k+60k+110k+55k+65k+80k+70k)/7 = 535/7 = ~76.4k
    print("=======================================")
    print("Query 1: Employees earning above average salary")
    print("=======================================")
    query_1 = """
    SELECT name, department, salary 
    FROM employees 
    WHERE salary > (SELECT AVG(salary) FROM employees);
    """
    df1 = pd.read_sql_query(query_1, conn)
    print(df1)
    
    # ==========================================
    # SQL Query 2: Derived Table in FROM
    # ==========================================
    # Goal: Query from a subquery calculation that maps annual incomes.
    print("\n=======================================")
    print("Query 2: Querying from a derived annual income calculation table")
    print("=======================================")
    query_2 = """
    SELECT 
        derived.name, 
        derived.annual_income 
    FROM (
        SELECT name, salary * 12 AS annual_income 
        FROM employees
    ) AS derived 
    WHERE derived.annual_income > 1000000;
    """
    df2 = pd.read_sql_query(query_2, conn)
    print(df2)
    
    # ==========================================
    # SQL Query 3: Correlated Subquery
    # ==========================================
    # Goal: Get employees earning more than the average salary of their own department.
    print("\n=======================================")
    print("Query 3: Employees earning more than their own department's average")
    print("=======================================")
    query_3 = """
    SELECT outer_emp.name, outer_emp.department, outer_emp.salary 
    FROM employees outer_emp
    WHERE outer_emp.salary > (
        SELECT AVG(inner_emp.salary) 
        FROM employees inner_emp 
        WHERE inner_emp.department = outer_emp.department
    );
    """
    df3 = pd.read_sql_query(query_3, conn)
    print(df3)
    print("=======================================")
    
    conn.close()

if __name__ == "__main__":
    run_subqueries_demo()

"""
Key Takeaways:
- Scalar subqueries return exactly one row and one column.
- Derived tables inside the FROM clause must be assigned a table alias (e.g. `AS derived`).
- Correlated subqueries reference outer query values, running once per outer row, which can be computationally expensive on large tables.

Interview Relevance:
- What is a correlated subquery and how does it compare to a standard subquery? (A standard subquery executes once and its output is used by the outer query; a correlated subquery references columns in the outer query and must execute once for every row processed by the outer query).
- Can a subquery return multiple columns? (Yes, if used with operators like `EXISTS` or when matching tuple pairs like `WHERE (col1, col2) IN (SELECT col1, col2 FROM ...)`).
- Which is faster, a JOIN or a subquery? (In general, JOINs are optimized better by relational database engine planners than correlated subqueries, though modern planners often rewrite subqueries as joins automatically).

AI/ML Relevance:
- Cohort Identification: Selecting subgroups that behave differently from average behavior (e.g., selecting customers who spent twice the cohort average) uses scalar WHERE filters.
- Complex Features: Calculating nested aggregation tables (e.g., historical user averages) and joining them back to the active user records uses derived FROM constructs.
"""
