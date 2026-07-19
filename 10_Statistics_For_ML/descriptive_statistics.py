"""
Topic:
Descriptive Statistics: Measures of Central Tendency & Dispersion

Importance:
Before training any model, engineers must inspect dataset shapes, scales,
center anchors, and deviations to configure feature scaling and normalization.

This file covers:
- Measures of Central Tendency: Mean, Median, Mode
- Measures of Dispersion: Range, Variance, Standard Deviation, Quartiles, Interquartile Range (IQR)
- Shape measures: Skewness and Kurtosis
"""

import numpy as np
from scipy import stats

# ==========================================
# Formula Explanation in Comments
# ==========================================
# 1. Mean (μ or x̄):
#    - Average of the numbers.
#    - Formula: Sum of values / Count of values -> (Σ x_i) / N
#
# 2. Median:
#    - Middle value when data is sorted.
#    - Robust against extreme outliers.
#
# 3. Mode:
#    - Most frequently occurring value in the dataset.
#
# 4. Range:
#    - Difference between maximum and minimum values: Max - Min.
#
# 5. Variance (σ² for population, s² for sample):
#    - Average squared deviation from the mean.
#    - Sample Formula: s² = Σ (x_i - x̄)² / (N - 1) (Bessel's correction divides by N-1 for unbiased sample variance).
#
# 6. Standard Deviation (σ or s):
#    - Square root of variance. Expresses dispersion in original units.
#    - Formula: s = √Variance
#
# 7. Quartiles (Q1, Q2, Q3) & Interquartile Range (IQR):
#    - Q1: 25th percentile. Q2: 50th percentile (Median). Q3: 75th percentile.
#    - IQR: Difference between 75th and 25th percentiles: Q3 - Q1.
#    - Checked to identify outliers.
#
# 8. Skewness:
#    - Measures asymmetry of distribution. 0 is symmetric, negative is left-skewed, positive is right-skewed.
#
# 9. Kurtosis:
#    - Measures "tailedness" of distribution. Normal distribution has Kurtosis = 3 (or excess kurtosis = 0).

# ==========================================
# Python Implementation
# ==========================================

def compute_descriptive_statistics(data):
    """
    Computes central tendency, dispersion, and shape statistics for a 1D array.
    """
    data_arr = np.array(data)
    
    # Central Tendency
    mean_val = np.mean(data_arr)
    median_val = np.median(data_arr)
    # stats.mode returns ModeResult(mode=array, count=array)
    mode_result = stats.mode(data_arr, keepdims=True)
    mode_val = mode_result.mode[0]
    
    # Dispersion
    min_val = np.min(data_arr)
    max_val = np.max(data_arr)
    data_range = max_val - min_val
    
    # ddof=1 computes sample variance (N-1) instead of population (N)
    variance_val = np.var(data_arr, ddof=1)
    std_dev_val = np.std(data_arr, ddof=1)
    
    # Percentiles
    q1 = np.percentile(data_arr, 25)
    q3 = np.percentile(data_arr, 75)
    iqr_val = q3 - q1
    
    # Shape
    skewness_val = stats.skew(data_arr)
    kurtosis_val = stats.kurtosis(data_arr)  # scipy returns excess kurtosis (kurtosis - 3)
    
    return {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val,
        "range": data_range,
        "variance": variance_val,
        "std_dev": std_dev_val,
        "q1": q1,
        "q3": q3,
        "iqr": iqr_val,
        "skewness": skewness_val,
        "excess_kurtosis": kurtosis_val
    }


# ==========================================
# Example Data & Execution
# ==========================================
if __name__ == "__main__":
    # Mock data representing salaries of 12 software engineers in thousands
    salaries = [50, 52, 55, 58, 60, 62, 63, 65, 70, 72, 80, 150]  # note the extreme outlier 150
    
    stats_dict = compute_descriptive_statistics(salaries)
    
    print("=======================================")
    print("Topic: Descriptive Statistics Summary")
    print("=======================================")
    print("Example salaries dataset:", salaries)
    
    # ==========================================
    # Interpretation of Results
    # ==========================================
    print("\n--- Measures of Central Tendency ---")
    print(f"Mean Salary:   {stats_dict['mean']:.2f}k")
    print(f"Median Salary: {stats_dict['median']:.2f}k")
    print(f"Mode Salary:   {stats_dict['mode']:.2f}k")
    
    print("\n--- Measures of Dispersion ---")
    print(f"Salary Range:       {stats_dict['range']:.2f}k")
    print(f"Sample Variance:    {stats_dict['variance']:.2f}k²")
    print(f"Sample Std Dev:     {stats_dict['std_dev']:.2f}k")
    print(f"25th Percentile (Q1): {stats_dict['q1']:.2f}k")
    print(f"75th Percentile (Q3): {stats_dict['q3']:.2f}k")
    print(f"Interquartile Range: {stats_dict['iqr']:.2f}k")
    
    print("\n--- Shape Metrics ---")
    print(f"Skewness:        {stats_dict['skewness']:.4f}")
    print(f"Excess Kurtosis: {stats_dict['excess_kurtosis']:.4f}")
    
    print("\n--- Interpretation ---")
    print(f"1. Outlier Effect: Note that the Mean ({stats_dict['mean']:.2f}k) is pulled upwards significantly")
    print(f"   due to the outlier '150k'. The Median ({stats_dict['median']:.2f}k) remains closer to the bulk of salaries,")
    print("   showing it is robust to outliers.")
    print(f"2. Dispersion: The standard deviation of {stats_dict['std_dev']:.2f}k highlights that salaries")
    print("   typically spread within that range around the mean.")
    print(f"3. Skewness: The positive skewness of {stats_dict['skewness']:.2f} indicates that the data distribution has")
    print("   a long tail extending to the right (positive skew).")
    print(f"4. Kurtosis: Positive excess kurtosis of {stats_dict['excess_kurtosis']:.2f} shows a leptokurtic distribution")
    print("   (heavy-tailed, due to the high outlier).")
    print("=======================================")

"""
Key Takeaways:
- Mean is highly sensitive to extreme outliers; Median is robust.
- Standard Deviation measures spread in original dataset units, while variance is in squared units.
- Positive skewness implies data is stretched to the right; negative skewness implies stretch to the left.

Interview Relevance:
- Explain why the sample variance formula divides by N-1 instead of N. (Bessel's correction adjusts for bias when estimating population parameters from a sample).
- When would you prefer median over mean? (When the data contains significant outliers or is highly skewed, like house prices or household incomes).
- Explain IQR (Interquartile Range) and how it detects outliers. (IQR represents the middle 50% of the data. Values beyond 1.5 * IQR from Q1 or Q3 are mathematically flagged as outliers).

AI/ML Relevance:
- Data Scaling: Standard scaler uses Mean and Std Dev to normalize features -> z = (x - μ) / σ.
- Feature Transformations: Highly skewed features (skewness > 1 or < -1) can degrade linear model performance. Log transformations help reduce positive skew.
"""
