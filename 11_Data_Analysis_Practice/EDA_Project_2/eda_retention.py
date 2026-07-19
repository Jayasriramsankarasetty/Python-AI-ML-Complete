"""
Topic:
EDA Project 2 - Employee Attrition & Retention Profiling

Importance:
Analyzing customer or employee churn profiles is a high-frequency business application.
Understanding correlation matrix networks and distributions splits shapes the feature engineering
choices for classifier models.

This file covers:
- Loading CSV datasets
- Statistical comparison (Mean metrics grouped by Churn)
- Correlation Heatmaps
- Boxplots and Histograms for demographic profiles
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
sns.set_theme(style="darkgrid", palette="muted")

def run_retention_eda():
    dataset_path = "11_Data_Analysis_Practice/datasets/employee_data.csv"
    
    # 0. Check if dataset exists
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset {dataset_path} not found. Please run generate_mock_datasets.py first.")
        return
        
    # 1. Load Data
    df = pd.read_csv(dataset_path)
    print("=======================================")
    print("Employee Dataset Loaded successfully.")
    print("=======================================")
    print(f"Data Shape: {df.shape}")
    print("\nFirst 3 rows:\n", df.head(3))
    
    # 2. Descriptive Profiling grouped by Churn_Status
    # (1 = Left, 0 = Stayed)
    print("\n--- Mean metrics grouped by Churn Status ---")
    # Exclude non-numeric or ID fields for clean average summary
    numeric_cols = ["Age", "Years_At_Company", "Satisfaction_Score", "Monthly_Salary", "Churn_Status"]
    churn_group = df[numeric_cols].groupby("Churn_Status").mean()
    print(churn_group)
    
    # 3. Correlation Analysis Heatmap
    print("\n--- Correlation Heatmap Matrix ---")
    corr_matrix = df[numeric_cols].corr()
    print(corr_matrix)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1, ax=ax, square=True)
    ax.set_title("Employee Attributes: Correlation Heatmap Matrix", fontsize=12, fontweight="bold")
    plt.tight_layout()
    plt.savefig("11_Data_Analysis_Practice/EDA_Project_2/correlation_matrix.png")
    plt.close()
    print("Saved: 'correlation_matrix.png'")
    
    # 4. Boxplot: Salary distribution across Churn groups
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x="Churn_Status", y="Monthly_Salary", hue="Department", ax=ax)
    ax.set_title("Salary distribution across Churn Status (by Department)")
    ax.set_xlabel("Churn Status (0 = Retained, 1 = Churned)")
    ax.set_ylabel("Monthly Salary ($)")
    plt.tight_layout()
    plt.savefig("11_Data_Analysis_Practice/EDA_Project_2/salary_boxplot.png")
    plt.close()
    print("Saved: 'salary_boxplot.png'")
    
    # 5. Satisfaction score histogram comparison
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x="Satisfaction_Score", hue="Churn_Status", kde=True, multiple="stack", bins=10, ax=ax)
    ax.set_title("Employee Satisfaction distribution by Churn Status")
    ax.set_xlabel("Satisfaction Score (1-10)")
    ax.set_ylabel("Count")
    plt.tight_layout()
    plt.savefig("11_Data_Analysis_Practice/EDA_Project_2/satisfaction_histogram.png")
    plt.close()
    print("Saved: 'satisfaction_histogram.png'")
    
    print("\n=======================================")
    print("EDA Retention analysis completed successfully.")
    print("=======================================")

if __name__ == "__main__":
    run_retention_eda()
