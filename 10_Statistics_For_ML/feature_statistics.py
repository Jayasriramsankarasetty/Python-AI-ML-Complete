"""
Topic:
Feature Statistics: Outliers Detection, Normality Checks, and Log Transformations

Importance:
Real-world datasets contain anomalies, noise, and highly skewed patterns.
Using statistical limits to prune anomalies (IQR/Z-score) and validating normal distribution
assumptions is standard practice in predictive analytics pipelines.

This file covers:
- Outliers detection using Z-Score threshold
- Outliers detection using Interquartile Range (IQR) boundary limits
- Normality testing using Shapiro-Wilk test
- Skewness remediation using Log transformation
"""

import numpy as np
from scipy import stats

# ==========================================
# Formula Explanation in Comments
# ==========================================
# 1. Z-Score Outlier Filter:
#    - Standardizes the data points: Z = (x - μ) / σ.
#    - Outlier rule: Any data point with an absolute Z-score value greater than a threshold
#      (typically 3) is considered an outlier.
#    - Note: Best suited for symmetric Gaussian datasets.
#
# 2. IQR Outlier Filter (Tukey's Fences):
#    - IQR = Q3 - Q1.
#    - Outlier boundaries:
#      - Lower Bound = Q1 - 1.5 * IQR
#      - Upper Bound = Q3 + 1.5 * IQR
#    - Outlier rule: Any data point falling below the Lower Bound or above the Upper Bound is an outlier.
#    - Note: Robust to skewed distributions.
#
# 3. Shapiro-Wilk Normality Test:
#    - Null Hypothesis (H0): The data is normally distributed.
#    - Alternative Hypothesis (Ha): The data is NOT normally distributed.
#    - Decision: If P-value <= 0.05, reject H0 (data is not normal).
#
# 4. Log Transformation:
#    - Applies y = log(x) (or log(x + 1) if data contains zeros) to compress positive skewness.

# ==========================================
# Python Implementation & Verification
# ==========================================

# 1. Outlier Detection Functions
def detect_outliers_z_score(data, threshold=3.0):
    mean = np.mean(data)
    std = np.std(data)
    outliers = []
    outlier_indices = []
    
    for idx, x in enumerate(data):
        z = (x - mean) / std
        if abs(z) > threshold:
            outliers.append(x)
            outlier_indices.append(idx)
    return outliers, outlier_indices

def detect_outliers_iqr(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = []
    outlier_indices = []
    for idx, x in enumerate(data):
        if x < lower_bound or x > upper_bound:
            outliers.append(x)
            outlier_indices.append(idx)
    return outliers, outlier_indices, lower_bound, upper_bound

# 2. Normality Checking Function
def check_normality(data, alpha=0.05):
    # shapiro returns (shapiro_stat, p_value)
    stat, p_val = stats.shapiro(data)
    is_normal = p_val > alpha
    return stat, p_val, is_normal


# ==========================================
# Example Data & Execution
# ==========================================
if __name__ == "__main__":
    print("=======================================")
    print("Topic: Feature Statistics & Transformations")
    print("=======================================")
    
    # Example dataset: Log-normal skewed data containing a high outlier anomaly
    # Bulk of data lies between 10 and 100, plus one extreme outlier 500
    feature_vals = [12, 15, 18, 22, 25, 30, 45, 60, 75, 90, 110, 500]
    
    # 1. Detect Outliers
    z_outliers, z_indices = detect_outliers_z_score(feature_vals, threshold=2.0)  # low threshold for demo
    iqr_outliers, iqr_indices, low_b, up_b = detect_outliers_iqr(feature_vals)
    
    # 2. Normality Check Before Transformation
    shapiro_s, shapiro_p, normal_bool = check_normality(feature_vals)
    
    # 3. Log Transformation
    log_transformed = np.log1p(feature_vals)  # log1p computes log(x + 1) to safely handle zero inputs
    skew_before = stats.skew(feature_vals)
    skew_after = stats.skew(log_transformed)
    
    # Normality Check After Transformation
    _, shapiro_p_after, normal_bool_after = check_normality(log_transformed)
    
    # ==========================================
    # Interpretation of Results
    # ==========================================
    print("--- 1. Outlier Detection Results ---")
    print(f"Original Feature List: {feature_vals}")
    print(f"Z-Score (threshold=2.0) detected outliers: {z_outliers} (indices: {z_indices})")
    print(f"IQR detected bounds: [{low_b:.2f}, {up_b:.2f}]")
    print(f"IQR detected outliers:                 {iqr_outliers} (indices: {iqr_indices})")
    print("Interpretation: Both filters successfully flagged '500' as an outlier. IQR is robust to the outlier itself")
    print("when computing boundaries, whereas Z-score boundaries are expanded by the outlier because it inflates std dev.")
    
    print("\n--- 2. Normality & Transformation Results ---")
    print(f"Skewness BEFORE Log Transform: {skew_before:.4f}")
    print(f"Shapiro-Wilk test p-value before: {shapiro_p:.8f} (Normally distributed? {normal_bool})")
    
    print(f"\nSkewness AFTER Log Transform:  {skew_after:.4f}")
    print(f"Shapiro-Wilk test p-value after:  {shapiro_p_after:.8f} (Normally distributed? {normal_bool_after})")
    
    print("\n--- Interpretation ---")
    print("1. Before transformation, the dataset failed the normality check (p-value close to 0) due to positive skewness.")
    print("2. Applying a Log transformation successfully reduced the skewness coefficient closer to zero (from positive skew)")
    print("   and increased the normality p-value, formatting features in a much cleaner shape for ML models.")
    print("=======================================")

"""
Key Takeaways:
- IQR outlier boundaries are calculated using the 25th and 75th percentiles, making bounds calculation robust to outliers.
- Shapiro-Wilk test uses a null hypothesis of normal distribution; small p-values (< 0.05) reject this normality.
- Skewed datasets can be normalized using mathematical transformations like Log or Box-Cox.

Interview Relevance:
- Explain how you detect outliers in a dataset. (Explain Z-score limits for normal data and IQR fence rules for skewed data).
- How do you verify if a dataset column is normally distributed? (Visually using Q-Q plots/histograms, or statistically using the Shapiro-Wilk normality test).
- What is Log-Transformation and when do you use it? (It is a feature transformation technique that applies natural logarithms to compress right-skewed variables, centering features and stabilizing variances).

AI/ML Relevance:
- Data Prep: Standard classifiers and regression pipelines require outlier pruning (dropping IQR outlier rows) to avoid overfitting weight estimates.
- Assumptions Audit: Linear models assume variables or residuals are normal; checking normality prevents poor testing performance.
"""
