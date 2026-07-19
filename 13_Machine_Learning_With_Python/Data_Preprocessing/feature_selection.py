"""
Topic:
Data Preprocessing - Feature Selection (Filter Methods)

Importance:
Adding too many features to a model causes the Curse of Dimensionality,
which increases training time, creates noise, and causes overfitting. Selecting the most
predictive subset of features preserves generalizability.

This file covers:
- Setting up a mock dataset containing low variance and highly correlated features
- VarianceThreshold (dropping features with near-constant values)
- Correlation Thresholding (dropping collinear inputs)
- SelectKBest with f_classif (selecting top K features based on ANOVA f-value scores)
"""

import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif

# ==========================================
# 1. Setup Mock Dataset
# ==========================================
# Target label: y (binary classifier class: 1 or 0)
# Feature 1: Constant feature (all values are 5.0, zero variance)
# Feature 2: High correlation feature (very similar to feature 3)
# Feature 3: Base numerical variable
# Feature 4: Random noise feature (unassociated with y)
np.random.seed(42)
n_samples = 100

y = np.random.choice([0, 1], size=n_samples)

# Generate features
f_constant = np.full(n_samples, 5.0)                       # low variance
f_numeric = np.random.normal(loc=y * 2.0, scale=1.0)        # strong signal (depends on target y)
f_collinear = f_numeric + np.random.normal(0, 0.05, n_samples)  # highly collinear with f_numeric
f_noise = np.random.normal(loc=0.0, scale=1.0, size=n_samples) # random noise

df_features = pd.DataFrame({
    "constant": f_constant,
    "signal": f_numeric,
    "collinear": f_collinear,
    "noise": f_noise
})

print("=======================================")
print("Original Dataset Features (first 5 rows):")
print("=======================================")
print(df_features.head(5))

# ==========================================
# 2. Variance Threshold Selection
# ==========================================
print("\n--- 1. VarianceThreshold Filtering ---")
# Drop features with variance below threshold (default = 0.0, drops constant columns)
selector_var = VarianceThreshold(threshold=0.01)
selected_var_array = selector_var.fit_transform(df_features)

# Convert back to DataFrame
selected_cols_var = df_features.columns[selector_var.get_support()]
df_var_filtered = pd.DataFrame(selected_var_array, columns=selected_cols_var)
print(f"Features kept after variance filter: {selected_cols_var.tolist()}")

# ==========================================
# 3. Correlation Threshold Selection
# ==========================================
print("\n--- 2. Correlation Filtering ---")
# Check correlation matrix of remaining columns
corr_matrix = df_var_filtered.corr().abs()
print("Correlation Matrix:")
print(corr_matrix)

# Select upper triangle of correlation matrix
upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Find columns with correlation greater than 0.90
to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.90)]
df_corr_filtered = df_var_filtered.drop(columns=to_drop)

print(f"Columns dropped due to high correlation (>0.90): {to_drop}")
print(f"Remaining features after correlation filter: {df_corr_filtered.columns.tolist()}")

# ==========================================
# 4. Statistical Selection: SelectKBest (ANOVA)
# ==========================================
print("\n--- 3. SelectKBest (ANOVA) Selection ---")
# Select top 1 feature that has the strongest relationship with the target variable y
# f_classif calculates ANOVA F-value between numerical features and binary target classes
selector_k = SelectKBest(score_func=f_classif, k=1)
selected_k_array = selector_k.fit_transform(df_corr_filtered, y)

# Inspect feature scores
feature_scores = pd.DataFrame({
    "Feature": df_corr_filtered.columns,
    "F_Score": selector_k.scores_
}).sort_values(by="F_Score", ascending=False)
print("ANOVA Feature Scores:")
print(feature_scores)

selected_cols_k = df_corr_filtered.columns[selector_k.get_support()]
print(f"\nTop 1 selected feature: {selected_cols_k.tolist()}")
print("=======================================")

"""
Key Takeaways:
- VarianceThreshold filters features that do not carry any informational spread (constant values).
- Collinear variables are redundant; dropping one of a correlated pair stabilizes model weight estimates.
- SelectKBest filters features by sorting statistical association values (like ANOVA or Chi-Square).

Interview Relevance:
- Explain the difference between Filter, Wrapper, and Embedded feature selection methods. (Filter methods evaluate features individually based on statistics; Wrapper methods search sets of features by training models iteratively; Embedded methods select features during model training, like Lasso L1 regularization).
- What is Multicollinearity and why is it a problem? (When two or more features are highly correlated. It causes instability in regression coefficients and inflates variance bounds).
- How does VarianceThreshold handle target values? (It doesn't. VarianceThreshold is completely unsupervised and only looks at feature variances, regardless of targets).

AI/ML Relevance:
- Dimensionality Pruning: Stripping noisy features (like the noise column) speeds up training and makes models less prone to overfitting.
- Efficiency: Selecting a small subset of features lowers storage footprint and query compute costs in production inference nodes.
"""
