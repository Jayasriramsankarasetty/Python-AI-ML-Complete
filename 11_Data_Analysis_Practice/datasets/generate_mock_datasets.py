"""
Topic:
Dataset Generation for EDA Practice Projects

Importance:
Having local datasets allows clean, executable, and reproducible projects
without depending on external HTTP requests.

This file covers:
- Generating sales_data.csv (Project 1)
- Generating employee_data.csv (Project 2)
"""

import os
import pandas as pd
import numpy as np

def generate_datasets():
    # Make sure target folder exists
    os.makedirs("11_Data_Analysis_Practice/datasets", exist_ok=True)
    
    # ------------------------------------------
    # 1. Sales Performance Dataset (sales_data.csv)
    # ------------------------------------------
    print("Generating sales_data.csv...")
    np.random.seed(42)
    n_sales = 200
    
    # Dates between 2026-01-01 and 2026-04-30
    date_range = pd.date_range(start="2026-01-01", end="2026-04-30", freq="D")
    dates = np.random.choice(date_range, size=n_sales)
    
    categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Sports"]
    category_choices = np.random.choice(categories, size=n_sales, p=[0.25, 0.20, 0.25, 0.15, 0.15])
    
    units = np.random.randint(1, 10, size=n_sales)
    
    prices_map = {
        "Electronics": 150.0,
        "Clothing": 40.0,
        "Home & Kitchen": 80.0,
        "Books": 15.0,
        "Sports": 60.0
    }
    
    unit_prices = [prices_map[cat] + np.random.randint(-5, 10) for cat in category_choices]
    locations = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
    location_choices = np.random.choice(locations, size=n_sales)
    
    sales_df = pd.DataFrame({
        "Transaction_ID": range(1001, 1001 + n_sales),
        "Date": dates,
        "Product_Category": category_choices,
        "Units_Sold": units,
        "Unit_Price": unit_prices,
        "Store_Location": location_choices
    })
    
    sales_path = "11_Data_Analysis_Practice/datasets/sales_data.csv"
    sales_df.to_csv(sales_path, index=False)
    print(f"Saved: {sales_path} (shape: {sales_df.shape})")

    # ------------------------------------------
    # 2. Employee Retention Dataset (employee_data.csv)
    # ------------------------------------------
    print("Generating employee_data.csv...")
    n_emp = 150
    
    ages = np.random.randint(22, 60, size=n_emp)
    depts = ["HR", "Engineering", "Sales", "Marketing", "Finance"]
    dept_choices = np.random.choice(depts, size=n_emp, p=[0.10, 0.40, 0.25, 0.15, 0.10])
    
    company_years = []
    for age in ages:
        # Company years must be less than age - 18
        max_years = max(1, age - 21)
        company_years.append(np.random.randint(1, min(15, max_years) + 1))
        
    salary_map = {
        "HR": 55000,
        "Engineering": 95000,
        "Sales": 65000,
        "Marketing": 60000,
        "Finance": 75000
    }
    
    monthly_salaries = []
    for d, yrs in zip(dept_choices, company_years):
        base = salary_map[d]
        increment = yrs * 2000
        noise = np.random.randint(-4000, 5000)
        # convert annual salary estimation to monthly
        monthly_salaries.append(round((base + increment + noise) / 12, 2))
        
    satisfaction = np.random.randint(1, 11, size=n_emp)
    
    # Churn status: higher probability if satisfaction is low or salary is low
    churn_labels = []
    for sat, sal in zip(satisfaction, monthly_salaries):
        # normalize salary score
        sal_score = min(1.0, sal / 10000.0)
        churn_prob = 0.8 - (sat * 0.05) - (sal_score * 0.3)
        churn_prob = max(0.05, min(0.95, churn_prob))
        churn_labels.append(np.random.choice([1, 0], p=[churn_prob, 1 - churn_prob]))
        
    emp_df = pd.DataFrame({
        "Emp_ID": range(2001, 2001 + n_emp),
        "Age": ages,
        "Department": dept_choices,
        "Years_At_Company": company_years,
        "Satisfaction_Score": satisfaction,
        "Monthly_Salary": monthly_salaries,
        "Churn_Status": churn_labels
    })
    
    emp_path = "11_Data_Analysis_Practice/datasets/employee_data.csv"
    emp_df.to_csv(emp_path, index=False)
    print(f"Saved: {emp_path} (shape: {emp_df.shape})")

if __name__ == "__main__":
    generate_datasets()
