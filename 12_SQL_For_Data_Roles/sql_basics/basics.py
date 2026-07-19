"""
Topic:
SQL Basics - SELECT, DISTINCT, and Aliasing Projections

Importance:
Understanding column projection structures represents the absolute entry point of database queries.
Standardizing column namespaces using aliasing is a key prep step before converting databases
into Pandas DataFrames for machine learning.

This file covers:
- Setting up an in-memory SQLite database
- Seeding mock employee records
- Running projections selecting specific columns
- Extracting unique values using DISTINCT
- Renaming headings using AS aliasing
"""

import sqlite3
import pandas as pd

def run_basics_demo():
    # 1. Establish database connection (in-memory SQLite database)
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # 2. Create mock table
    cursor.execute("""
    CREATE TABLE employees (
        emp_id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary REAL
    );
    """)
    
    # 3. Seed mock data records
    employees_data = [
        (1, "Alice", "Engineering", 95000.0),
        (2, "Bob", "Sales", 60000.0),
        (3, "Charlie", "Engineering", 110000.0),
        (4, "David", "HR", 55000.0),
        (5, "Eva", "Sales", 60000.0)
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?);", employees_data)
    conn.commit()
    
    # ==========================================
    # SQL Query 1: Basic Column Projection (SELECT)
    # ==========================================
    print("=======================================")
    print("Query 1: Retrieving employee names and salaries")
    print("=======================================")
    query_1 = "SELECT name, salary FROM employees;"
    df1 = pd.read_sql_query(query_1, conn)
    print(df1)
    
    # ==========================================
    # SQL Query 2: Extracting Unique Values (DISTINCT)
    # ==========================================
    print("\n=======================================")
    print("Query 2: Finding distinct departments in the firm")
    print("=======================================")
    query_2 = "SELECT DISTINCT department FROM employees;"
    df2 = pd.read_sql_query(query_2, conn)
    print(df2)
    
    # ==========================================
    # SQL Query 3: Aliasing Column Names (AS)
    # ==========================================
    print("\n=======================================")
    print("Query 3: Projecting columns with custom aliases")
    print("=======================================")
    query_3 = """
    SELECT 
        name AS Employee_Name, 
        salary AS Monthly_Earnings 
    FROM employees;
    """
    df3 = pd.read_sql_query(query_3, conn)
    print(df3)
    print("=======================================")
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    run_basics_demo()

"""
Key Takeaways:
- SELECT defines column projections; SELECT * fetches all database columns.
- DISTINCT deduplicates output sets based on column values.
- AS allows renaming column headings for cleaner business reporting presentation.

Interview Relevance:
- Explain what DISTINCT does and how it handles NULL values. (DISTINCT returns only unique values in a column; if there are multiple NULLs, it returns a single NULL).
- Can you use aliases in the WHERE clause? (Generally, no, because the WHERE clause is evaluated before the SELECT projections are calculated).
- What is the difference between SELECT * and specifying column names? (Specifying column names is faster, uses less network traffic, and prevents code failure if the database schema columns order changes).

AI/ML Relevance:
- Feature Names: Standardizing column headings using AS aliases keeps variable names aligned when downloading tables into training scripts.
- Memory Allocation: Selecting only the necessary feature columns (instead of SELECT *) reduces data transfer payloads and local machine RAM usage.
"""
