"""
Topic:
Data Preprocessing - Handling Missing Values (Imputation)

Importance:
Real-world datasets contain missing entries. Most scikit-learn ML models
cannot handle missing values (NaN) during training, which throws errors.
Knowing how to apply univariate (SimpleImputer) and multivariate (KNNImputer) strategies
is key for stable data pipelines.

This file covers:
- Setting up a mock dataset containing missing values (NaN)
- Univariate imputation using SimpleImputer (Mean, Median, and Mode)
- Multivariate imputation using KNNImputer (K-Nearest Neighbors)
- Fitting and transforming imputation pipelines correctly
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer

# ==========================================
# 1. Create a Mock Dataset with Missing Data
# ==========================================
# Scenario: House details (Square Footage, Number of Bedrooms, Price)
# Some values are set to np.nan representing missing records.
raw_data = {
    "sq_footage": [1500, 2000, np.nan, 2500, 1800, 3000],
    "bedrooms": [3, np.nan, 4, 3, np.nan, 5],
    "price": [300000, 400000, 350000, np.nan, 280000, 550000]
}

df = pd.DataFrame(raw_data)
print("=======================================")
print("Original Dataset containing NaNs:")
print("=======================================")
print(df)

# ==========================================
# 2. Univariate Imputation: SimpleImputer
# ==========================================
print("\n--- 1. Univariate Imputation (SimpleImputer) ---")

# Strategy 'mean' for continuous values like square footage
mean_imputer = SimpleImputer(strategy="mean")
df_simple = df.copy()
df_simple["sq_footage"] = mean_imputer.fit_transform(df_simple[["sq_footage"]])

# Strategy 'median' for continuous variables (robust to outliers)
median_imputer = SimpleImputer(strategy="median")
df_simple["price"] = median_imputer.fit_transform(df_simple[["price"]])

# Strategy 'most_frequent' (mode) for discrete values like bedrooms count
mode_imputer = SimpleImputer(strategy="most_frequent")
df_simple["bedrooms"] = mode_imputer.fit_transform(df_simple[["bedrooms"]])

print("Imputed DataFrame using SimpleImputer:")
print(df_simple)

# ==========================================
# 3. Multivariate Imputation: KNNImputer
# ==========================================
print("\n--- 2. Multivariate Imputation (KNNImputer) ---")
# KNNImputer uses Euclidean distance weights from nearest neighbor coordinates
# to impute missing fields, taking all features into account.
knn_imputer = KNNImputer(n_neighbors=2)
knn_imputed_array = knn_imputer.fit_transform(df)

# Convert return array back to a Pandas DataFrame
df_knn = pd.DataFrame(knn_imputed_array, columns=df.columns)
print("Imputed DataFrame using KNNImputer (k=2):")
print(df_knn)
print("=======================================")

"""
Key Takeaways:
- SimpleImputer imputes missing values using univariate metrics (mean, median, mode, constant).
- Median strategy is robust to outliers; Mode is standard for discrete/categorical parameters.
- KNNImputer models relationships across other columns to impute data points, which is often more accurate.

Interview Relevance:
- How does SimpleImputer differ from KNNImputer? (SimpleImputer uses statistical metrics of a single column to fill values; KNNImputer uses the distance relationships across all features to fill values based on the nearest neighbors).
- When would you drop rows with missing values instead of imputing them? (When the missing data is in the target variable, or when a row contains missing values across almost all feature columns, making imputation speculative).
- Why is it critical to fit the imputer ONLY on the training split, and transform the test split? (To prevent data leakage. If we fit on the entire dataset, metrics like mean or median of the test split will leak into the training dataset).

AI/ML Relevance:
- Robustness: Cleaning missing entries prevents program crashes during model training.
- Pipeline Safety: Fitting imputers on train data and applying them to test/prod data preserves validation integrity.
"""
