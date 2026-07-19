"""
Topic:
EDA Project 1 - Sales Performance Analysis

Importance:
Understanding revenue trends, top-selling categories, and regional store performance
is a standard business intelligence and predictive analytics requirement.
This file practices data aggregations, feature engineering, and plot visualizations.

This file covers:
- Loading CSV dataset using Pandas
- Feature engineering (calculating Total Revenue)
- Product and Store performance groupings
- Time-series monthly revenue trends
- Saving charts to disk (non-interactive backend)
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns
import os

# Set visual styling
sns.set_theme(style="whitegrid", palette="deep")

def run_sales_eda():
    dataset_path = "11_Data_Analysis_Practice/datasets/sales_data.csv"
    
    # 0. Check if dataset exists
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_path} not found. Please run generate_mock_datasets.py first.")
        return
        
    # 1. Load Data
    df = pd.read_csv(dataset_path)
    print("=======================================")
    print("Sales Dataset Loaded successfully.")
    print("=======================================")
    print(f"Data Shape: {df.shape}")
    print("\nFirst 3 rows:\n", df.head(3))
    
    # Check for missing values
    print("\nMissing values:\n", df.isnull().sum())
    
    # 2. Feature Engineering: Total Revenue
    # Revenue = Units_Sold * Unit_Price
    df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]
    print("\nAfter adding 'Revenue' column:\n", df.head(3))
    
    # 3. Product Category Analysis
    print("\n--- Product Category Performance ---")
    cat_summary = df.groupby("Product_Category").agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Units=("Units_Sold", "sum"),
        Avg_Unit_Price=("Unit_Price", "mean")
    ).sort_values(by="Total_Revenue", ascending=False)
    print(cat_summary)
    
    # Save Plot: Revenue by Product Category
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=cat_summary.reset_index(), x="Product_Category", y="Total_Revenue", ax=ax, edgecolor="black")
    ax.set_title("Total Revenue by Product Category", fontsize=14, fontweight="bold")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig("11_Data_Analysis_Practice/EDA_Project_1/revenue_by_category.png")
    plt.close()
    print("Saved: 'revenue_by_category.png'")
    
    # 4. Regional Store Analysis
    print("\n--- Store Location Performance ---")
    store_summary = df.groupby("Store_Location")["Revenue"].sum().sort_values(ascending=False)
    print(store_summary)
    
    # 5. Time-Series Trend Analysis
    print("\n--- Monthly Revenue Trend ---")
    # Parse Date column and extract Year-Month
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year_Month"] = df["Date"].dt.to_period("M")
    
    monthly_summary = df.groupby("Year_Month")["Revenue"].sum().sort_index()
    print(monthly_summary)
    
    # Save Plot: Monthly Trend
    fig, ax = plt.subplots(figsize=(8, 5))
    # Convert PeriodIndex to strings for plotting compatibility
    sns.lineplot(x=monthly_summary.index.astype(str), y=monthly_summary.values, marker="o", color="blue", linewidth=2, ax=ax)
    ax.set_title("Monthly Revenue Trend (2026)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("11_Data_Analysis_Practice/EDA_Project_1/monthly_revenue_trend.png")
    plt.close()
    print("Saved: 'monthly_revenue_trend.png'")
    
    print("\n=======================================")
    print("EDA Sales analysis completed successfully.")
    print("=======================================")

if __name__ == "__main__":
    run_sales_eda()
