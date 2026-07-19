"""
Topic:
Seaborn Basics: Relational and Categorical Statistical Plots

Importance:
Seaborn simplifies statistical data plotting by integrating with Pandas DataFrames.
It automatically calculates aggregates (means, confidence intervals) and distributions,
which speeds up Exploratory Data Analysis (EDA).

This file covers:
- Set up Agg non-interactive backend
- Relational plots (scatterplot, lineplot)
- Categorical plots (countplot, boxplot, violinplot)
- Applying style themes and saving outputs
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd

# Set Seaborn theme aesthetics globally
sns.set_theme(style="whitegrid", palette="muted")

# ==========================================
# 0. Load Built-In Dataset
# ==========================================
# Seaborn has built-in datasets. We will load the classic 'tips' dataset.
tips = sns.load_dataset("tips")
# Columns: total_bill, tip, sex, smoker, day, time, size
print("Sample DataFrame rows:\n", tips.head(3))

# ==========================================
# 1. Relational Scatter & Line Plots
# ==========================================
print("\n--- Creating Relational Plots ---")

# Scatter Plot: total_bill vs tip, colored by smoker category, sized by table size
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="smoker", size="size", ax=ax, alpha=0.8)
ax.set_title("Total Bill vs Tip (Categorized by Smoker/Size)")
plt.savefig("09_Python_Libraries_For_AI_ML/Seaborn/relational_scatter.png")
plt.close()
print("Saved: 'relational_scatter.png'")

# Line Plot: average bill over days (automatic mean and 95% confidence interval bands calculation)
fig, ax = plt.subplots(figsize=(8, 5))
sns.lineplot(data=tips, x="day", y="total_bill", hue="sex", marker="o", ax=ax)
ax.set_title("Average Total Bill Trend Across Days (with CI bands)")
plt.savefig("09_Python_Libraries_For_AI_ML/Seaborn/relational_line.png")
plt.close()
print("Saved: 'relational_line.png'")

# ==========================================
# 2. Categorical Distribution Plots (Box & Violin)
# ==========================================
print("\n--- Creating Categorical Plots ---")

# Box Plot: total_bill distributions across days (shows median, IQR, and outliers)
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="total_bill", hue="time", ax=ax)
ax.set_title("Bill Distributions Across Days (Box Plot: Outliers Check)")
plt.savefig("09_Python_Libraries_For_AI_ML/Seaborn/categorical_boxplot.png")
plt.close()
print("Saved: 'categorical_boxplot.png'")

# Violin Plot: total_bill distribution grouped by sex (shows full KDE density curve)
fig, ax = plt.subplots(figsize=(8, 5))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True, inner="quart", ax=ax)
ax.set_title("Bill Density Spread Across Days (Split Violin Plot)")
plt.savefig("09_Python_Libraries_For_AI_ML/Seaborn/categorical_violinplot.png")
plt.close()
print("Saved: 'categorical_violinplot.png'")

# Count Plot: count frequencies of categories (e.g. counts of tables served per day)
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=tips, x="day", hue="smoker", ax=ax)
ax.set_title("Total Tables Served Per Day (Count Plot)")
plt.savefig("09_Python_Libraries_For_AI_ML/Seaborn/categorical_countplot.png")
plt.close()
print("Saved: 'categorical_countplot.png'")

"""
Key Takeaways:
- Seaborn integrates with Pandas, allowing you to pass DataFrames to `data` and refer to column header titles as strings for `x` and `y`.
- `sns.lineplot()` automatically calculates statistical aggregate means and overlays a shaded 95% confidence interval band.
- Box plots check IQR outliers; Violin plots combine box plots with symmetric Kernel Density Estimate (KDE) probability spreads.
- Setting `split=True` in violin plots merges binary categories (e.g. Male/Female) into single split violins, saving space.

Interview Relevance:
- Difference between a Box Plot and a Violin Plot? (A Box Plot displays quartiles, median, IQR, and isolates outliers; a Violin Plot adds a smoothed Kernel Density Estimate to show full shape probability density curves of the data).
- How does Seaborn handle DataFrame inputs compared to Matplotlib? (Matplotlib accepts raw lists/arrays; Seaborn accepts pandas DataFrames and maps column string names to variables directly).
- What does the shaded area in Seaborn line plots mean? (By default, it represents the 95% bootstrap confidence interval around the calculated mean).

AI/ML Relevance:
- Outliers Management: Using `sns.boxplot()` helps visualize data distribution tails to prune outlier samples before feeding input features to linear regression models.
- Target Balance: Count plots (`sns.countplot()`) check if training classes suffer from skewness or label imbalance.
- Demographic Segmentation: Slicing variables across dimensions (like `hue='time'`, `hue='sex'`) aids in cohort feature engineering.
"""
