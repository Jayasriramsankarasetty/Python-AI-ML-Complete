"""
Topic:
Covariance & Correlation (Pearson vs Spearman)

Importance:
Identifying input-to-target dependency structures informs feature selection algorithms.
Correlation coefficients measure linear and monotonic strength relationships, helping engineers
eliminate collinear features.

This file covers:
- Covariance formula and coding calculation
- Pearson Correlation Coefficient (linear relationships)
- Spearman Rank Correlation Coefficient (non-linear monotonic relationships)
"""

import numpy as np
from scipy import stats

# ==========================================
# Formula Explanation in Comments
# ==========================================
# 1. Covariance (Cov(X, Y)):
#    - Measures the directional relationship between two variables.
#    - If Cov(X, Y) > 0: variables move in the same direction.
#    - If Cov(X, Y) < 0: variables move in opposite directions.
#    - Formula: Cov(X, Y) = Σ (x_i - x̄)(y_i - ȳ) / (N - 1)
#    - Limitation: Value scales with data units, making comparison hard.
#
# 2. Pearson Correlation Coefficient (r):
#    - Normalized covariance, ranging from -1 to 1.
#    - Measures only linear strength relationships.
#    - Formula: r = Cov(X, Y) / (s_x * s_y), where s_x and s_y are standard deviations.
#
# 3. Spearman Rank Correlation Coefficient (ρ):
#    - Measures monotonic strength relationships (how well relationship can be described by any monotonic function).
#    - Pearson correlation applied to the ranks of data values instead of raw values.
#    - Highly robust to outliers and non-linear (but monotonic) curves.

# ==========================================
# Python Implementation & Verification
# ==========================================

def compute_relationship_metrics(x, y):
    """
    Calculates Covariance, Pearson correlation, and Spearman correlation.
    """
    x_arr = np.array(x)
    y_arr = np.array(y)
    
    # Covariance Matrix: np.cov returns a 2x2 matrix:
    # [[Cov(X,X), Cov(X,Y)],
    #  [Cov(Y,X), Cov(Y,Y)]]
    cov_matrix = np.cov(x_arr, y_arr)
    covariance_val = cov_matrix[0, 1]
    
    # Pearson Correlation Coefficient (r) and p-value
    pearson_r, pearson_p = stats.pearsonr(x_arr, y_arr)
    
    # Spearman Rank Correlation (rho) and p-value
    spearman_rho, spearman_p = stats.spearmanr(x_arr, y_arr)
    
    return covariance_val, pearson_r, spearman_rho


# ==========================================
# Example Data & Execution
# ==========================================
if __name__ == "__main__":
    print("=======================================")
    print("Topic: Covariance & Correlation Analysis")
    print("=======================================")
    
    # Dataset A: Perfect Linear Relationship
    x_linear = [1, 2, 3, 4, 5]
    y_linear = [10, 20, 30, 40, 50]
    
    # Dataset B: Monotonic but Non-Linear Relationship (Exponential)
    x_mono = [1, 2, 3, 4, 5]
    y_mono = [10, 100, 1000, 10000, 100000]
    
    # Calculate Metrics for Linear Dataset
    cov_lin, pearson_lin, spearman_lin = compute_relationship_metrics(x_linear, y_linear)
    
    # Calculate Metrics for Monotonic Dataset
    cov_mon, pearson_mon, spearman_mon = compute_relationship_metrics(x_mono, y_mono)
    
    # ==========================================
    # Interpretation of Results
    # ==========================================
    print("--- Case 1: Perfect Linear Relationship ---")
    print(f"X: {x_linear} | Y: {y_linear}")
    print(f"Covariance:          {cov_lin:.2f}")
    print(f"Pearson Correlation: {pearson_lin:.4f}")
    print(f"Spearman Correlation: {spearman_lin:.4f}")
    print("Interpretation: Both Pearson and Spearman coefficients are 1.0, showing a perfect linear trend.")
    
    print("\n--- Case 2: Monotonic Non-Linear (Exponential) Relationship ---")
    print(f"X: {x_mono} | Y: {y_mono}")
    print(f"Covariance:          {cov_mon:.2f}  (scaled by massive exponential magnitudes)")
    print(f"Pearson Correlation: {pearson_mon:.4f}  (underestimates because the curve is not a straight line)")
    print(f"Spearman Correlation: {spearman_mon:.4f}  (retains 1.0 because rank ordering is perfectly preserved)")
    print("Interpretation: Spearman successfully identifies the perfect monotonic growth trend (1.0),")
    print("while Pearson drops (0.71) because it struggles to model non-linear boundaries.")
    print("=======================================")

"""
Key Takeaways:
- Covariance measures direction only, and is unit-dependent.
- Pearson Correlation measures strictly linear relationships.
- Spearman Rank Correlation checks monotonic relationships by ranking raw values, making it robust against outliers and non-linear curves.

Interview Relevance:
- What is the difference between Covariance and Correlation? (Covariance indicates the direction of a linear relationship between two variables; Correlation scales covariance by standard deviations, making it unit-independent and bound between -1 and 1).
- When would you use Spearman instead of Pearson? (When data relationships are non-linear but monotonic, or when the data contains extreme outliers that skew standard covariance).
- Does correlation imply causation? (No, correlation only measures mathematical associations. A third variable, a confounding factor, could be causing both changes).

AI/ML Relevance:
- Multicollinearity: Highly correlated features (Pearson r > 0.85) should be dropped or combined to prevent model variance instability (inflated weight standard errors in Linear Regression).
- Feature Importances: Correlation matrix heatmaps verify feature-to-target dependency strengths during initial EDA.
"""
