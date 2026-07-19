"""
Topic:
Advanced Seaborn: Matrix Heatmaps, Regression Plots, and Pairwise Grids

Importance:
Analyzing feature correlations and tracking pairwise combinations highlights multi-collinearity
and dependencies. Using heatmaps and pairplots helps machine learning engineers select and
prune inputs before model training.

This file covers:
- Regression plots (regplot) with line fitting
- Correlation Matrix Heatmap (annotated, custom colors)
- Pairwise grid distributions (pairplot)
- Aesthetic theme overrides
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd
import numpy as np

# Apply global darkgrid theme
sns.set_theme(style="darkgrid")

# Load Iris and Tips datasets
iris = sns.load_dataset("iris")
tips = sns.load_dataset("tips")

# ==========================================
# 1. Regression Plot (regplot)
# ==========================================
print("--- Creating Regression Plot ---")
# Fits a linear regression model and overlays a 95% confidence interval band
fig, ax = plt.subplots(figsize=(8, 5))
sns.regplot(data=tips, x="total_bill", y="tip", ax=ax, scatter_kws={"alpha": 0.6}, line_kws={"color": "red"})
ax.set_title("Total Bill vs Tip: Linear Regression Line Fit")

plt.savefig("09_Python_Libraries_For_AI_ML/Seaborn/regression_fit.png")
plt.close()
print("Saved: 'regression_fit.png'")

# ==========================================
# 2. Correlation Matrix Heatmap
# ==========================================
print("\n--- Creating Correlation Heatmap ---")
# Select only numerical features to compute Pearson Correlation Matrix
numerical_iris = iris.select_dtypes(include=[np.number])
corr_matrix = numerical_iris.corr()
print("Correlation Matrix:\n", corr_matrix)

fig, ax = plt.subplots(figsize=(8, 6))
# Create heatmap with cell annotations and custom diverging color palette
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1, ax=ax, square=True)
ax.set_title("Iris Features: Pearson Correlation Matrix Heatmap")

plt.savefig("09_Python_Libraries_For_AI_ML/Seaborn/correlation_heatmap.png")
plt.close()
print("Saved: 'correlation_heatmap.png'")

# ==========================================
# 3. Pairwise Relationships Grid (pairplot)
# ==========================================
print("\n--- Creating Pairwise Grid ---")
# pairplot is a Grid plot that generates scatterplots for all numeric feature pairs
# and distributions/KDE along the diagonal.
# We color points (hue) by the 'species' category to see class clustering.
grid = sns.pairplot(data=iris, hue="species", palette="Set2", diag_kind="kde")
# Custom title for the PairGrid
grid.figure.suptitle("Iris Dataset: Pairwise Feature Combinations", y=1.02, fontsize=14, fontweight="bold")

grid.savefig("09_Python_Libraries_For_AI_ML/Seaborn/pairplot_grid.png")
plt.close()
print("Saved: 'pairplot_grid.png'")

"""
Key Takeaways:
- `sns.regplot()` automatically fits a linear regression line and highlights uncertainty bands.
- Correlation matrices require numerical columns. Pearson correlation coefficients range from -1 (inverse correlation) to 1 (direct correlation).
- `sns.heatmap()` requires a 2D matrix, visualizing coefficients using divergent colormaps like `'coolwarm'`.
- `sns.pairplot()` creates a grid of pairwise comparison charts, which is highly useful to check class separating boundaries.

Interview Relevance:
- What is multi-collinearity and how do you detect it visually? (Multi-collinearity occurs when independent features are highly correlated with each other. It is detected using a Pearson Correlation Heatmap, identifying cell values close to 1 or -1).
- What does sns.pairplot() display? (It charts scatter plots comparing all numeric column pairs against each other, and frequency/KDE distributions along the main diagonal).
- Why do we pass only numerical data to correlation heatmaps? (Correlation calculations are based on numeric distance offsets and means; strings/categories cannot be calculated).

AI/ML Relevance:
- Feature Selection: Heatmaps reveal redundant columns (correlation > 0.9), allowing you to drop collinear variables to prevent model overfitting.
- Decision Boundaries: Pairplots visually isolate which feature pairings (e.g. Petal Length vs Petal Width) separate classes cleanly, indicating how well classifiers will perform.
- Trend Discovery: Linear regressions reveal if relationships fit straight-line linear models or require polynomial expansions.
"""
