"""
Topic:
Data Preprocessing - Feature Scaling (StandardScaler, MinMaxScaler, RobustScaler)

Importance:
Many ML algorithms (e.g. SVMs, K-Means, Neural Networks, KNNs) use Euclidean distance
or gradient descent optimization. If features have vastly different ranges (like age vs salary),
the larger values dominate, degrading model performance. Scaling levels the playing field.

This file covers:
- Setting up a continuous dataset containing scales and outliers
- Implementing StandardScaler (Z-Score Standardization: mean=0, std=1)
- Implementing MinMaxScaler (Normalizing to 0-1 range)
- Implementing RobustScaler (Using median and IQR to resist outlier distortion)
- Comparing scaling transformations output arrays
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# ==========================================
# 1. Setup Dataset with Outliers
# ==========================================
# Column 1: Age (range ~20-50, relatively clean)
# Column 2: Annual Salary (range ~40k-200k, containing an extreme outlier 1,000,000)
raw_data = {
    "age": [25, 30, 35, 40, 45, 50],
    "salary": [50000, 60000, 75000, 90000, 110000, 1000000]  # note the extreme outlier 1,000,000
}

df = pd.DataFrame(raw_data)
print("=======================================")
print("Original Dataset before scaling:")
print("=======================================")
print(df)

# ==========================================
# 2. StandardScaler (Z-Score)
# ==========================================
# Formula: z = (x - mean) / std_dev
# Forces mean=0, variance=1. Sensitive to outliers since mean and std dev are skewed by outliers.
std_scaler = StandardScaler()
df_scaled_std = pd.DataFrame(std_scaler.fit_transform(df), columns=["age_std", "salary_std"])

# ==========================================
# 3. MinMaxScaler (Normalization)
# ==========================================
# Formula: x_scaled = (x - min) / (max - min)
# Forces values into [0, 1] range. Outliers squeeze normal data points into a narrow range.
minmax_scaler = MinMaxScaler()
df_scaled_minmax = pd.DataFrame(minmax_scaler.fit_transform(df), columns=["age_minmax", "salary_minmax"])

# ==========================================
# 4. RobustScaler
# ==========================================
# Formula: x_scaled = (x - median) / IQR
# Centers data using the median and scales using IQR (75th percentile - 25th percentile).
# Outliers do not distort the boundaries of normal values.
robust_scaler = RobustScaler()
df_scaled_robust = pd.DataFrame(robust_scaler.fit_transform(df), columns=["age_robust", "salary_robust"])

# ==========================================
# 5. Output Comparisons
# ==========================================
print("\n=======================================")
print("Feature Scaling Transformation Results:")
print("=======================================")
# Concatenate original values and scaled parameters side by side for salary
comparison_df = pd.concat([
    df[["salary"]],
    df_scaled_std[["salary_std"]],
    df_scaled_minmax[["salary_minmax"]],
    df_scaled_robust[["salary_robust"]]
], axis=1)
print(comparison_df)
print("\n--- Summary Statistics of Scaled Outputs: ---")
print("Standard Scaler Salary Mean:  ", round(df_scaled_std["salary_std"].mean(), 4))
print("Standard Scaler Salary Std:   ", round(df_scaled_std["salary_std"].std(), 4))
print("MinMax Scaler Salary Max:     ", df_scaled_minmax["salary_minmax"].max())
print("MinMax Scaler Salary Min:     ", df_scaled_minmax["salary_minmax"].min())
print("Robust Scaler Salary Median:  ", df_scaled_robust["salary_robust"].median())
print("=======================================")

"""
Key Takeaways:
- StandardScaler centers distributions around 0 with unit variance; highly sensitive to outliers.
- MinMaxScaler squeezes values into the [0, 1] bounds; outliers will compress normal values.
- RobustScaler uses medians and interquartile ranges, making it ideal for datasets with heavy outlier counts.

Interview Relevance:
- What is the difference between Standardization and Normalization? (Standardization centers data to have mean=0 and variance=1 with no upper/lower boundaries; Normalization scales values into a fixed [0,1] range).
- Which scaling technique is best when the dataset has extreme outliers? (RobustScaler, because it uses median and IQR to scale, preventing outliers from shrinking the scaled values of normal data).
- Why do we fit the scaler on the training set and only transform the test set? (To prevent data leakage. Fitting the scaler on the test set would leak target information like test means and ranges into the training parameters).

AI/ML Relevance:
- Distance Algorithms: KNN classifiers and K-Means clustering will fail to compute proper clusters if feature scales are not unified.
- Neural Networks: Gradient descent optimization converges significantly faster when all feature gradients scale within comparable numerical boundaries.
"""
