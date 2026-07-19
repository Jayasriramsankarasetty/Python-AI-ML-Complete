"""
Topic:
Model Evaluation Metrics - Classification vs Regression Validation

Importance:
Models cannot be deployed without proving their generalization capabilities.
Selecting correct metrics (e.g. F1-score for imbalanced text, RMSE vs MAE for outliers)
determines target tuning priorities in ML pipelines.

This file covers:
- Classification evaluation metrics calculations (Precision, Recall, F1, ROC-AUC)
- Regression evaluation metrics calculations (MAE, MSE, RMSE, R-squared)
- Mathematical equations in comments
- Python evaluations using scikit-learn
"""

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix,
    mean_absolute_error, mean_squared_error, r2_score
)

# ==========================================
# Formulas Explanation in Comments
# ==========================================
# 1. Classification Metrics:
#    - Accuracy = (TP + TN) / (TP + TN + FP + FN) -> Overall fraction of correct predictions.
#    - Precision = TP / (TP + FP) -> Fraction of predicted positives that are actual positives. (Minimizes false alarms).
#    - Recall (Sensitivity) = TP / (TP + FN) -> Fraction of actual positives correctly identified. (Minimizes miss rates).
#    - F1-Score = 2 * (Precision * Recall) / (Precision + Recall) -> Harmonic mean of Precision and Recall.
#    - ROC-AUC: Area under the Receiver Operating Characteristic curve. Measures model's ability to rank classes.
#
# 2. Regression Metrics:
#    - Mean Absolute Error (MAE) = (1/N) * Σ |y_actual - y_pred| -> Average absolute error deviation. Less sensitive to outliers.
#    - Mean Squared Error (MSE) = (1/N) * Σ (y_actual - y_pred)² -> Penalizes large errors heavily (due to squaring).
#    - Root Mean Squared Error (RMSE) = √MSE -> Expresses errors in original target units.
#    - R-squared (R²) = 1 - (RSS / TSS) -> Percentage of target variance explained by model features.

# ==========================================
# 1. Classification Evaluation Demo
# ==========================================
def run_classification_metrics_demo():
    print("=======================================")
    print("1. Classification Metrics Demonstration")
    print("=======================================")
    
    # Example data: actual binary classification labels vs model predictions/probabilities
    y_actual = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 0])
    y_predicted = np.array([0, 0, 1, 1, 0, 0, 1, 1, 1, 0]) # 1 false negative, 1 false positive
    y_prob_scores = np.array([0.1, 0.2, 0.8, 0.9, 0.4, 0.1, 0.95, 0.7, 0.85, 0.3])
    
    # Calculate Metrics
    acc = accuracy_score(y_actual, y_predicted)
    prec = precision_score(y_actual, y_predicted)
    rec = recall_score(y_actual, y_predicted)
    f1 = f1_score(y_actual, y_predicted)
    auc = roc_auc_score(y_actual, y_prob_scores)
    conf = confusion_matrix(y_actual, y_predicted)
    
    # Print results
    print("Confusion Matrix:\n", conf)
    print(f"Accuracy:  {acc:.4f}  (Overall correctness percentage)")
    print(f"Precision: {prec:.4f}  (Minimizes False Positives)")
    print(f"Recall:    {rec:.4f}  (Minimizes False Negatives)")
    print(f"F1-Score:  {f1:.4f}  (Balanced harmonic average)")
    print(f"ROC-AUC:   {auc:.4f}  (Classes sorting strength)")
    print("=======================================")

# ==========================================
# 2. Regression Evaluation Demo
# ==========================================
def run_regression_metrics_demo():
    print("\n=======================================")
    print("2. Regression Metrics Demonstration")
    print("=======================================")
    
    # Example data: actual house prices vs predicted values (with one large outlier error at index 4)
    y_actual = np.array([300000, 400000, 350000, 280000, 550000])
    y_predicted = np.array([295000, 405000, 342000, 288000, 450000]) # 100k error on last sample
    
    # Calculate Metrics
    mae = mean_absolute_error(y_actual, y_predicted)
    mse = mean_squared_error(y_actual, y_predicted)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_actual, y_predicted)
    
    # Print results
    print(f"Mean Absolute Error (MAE):     ${mae:.2f}")
    print(f"Mean Squared Error (MSE):      {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): ${rmse:.2f}")
    print(f"R-squared Score (R²):          {r2:.4f}")
    print("\n--- Interpretation ---")
    print(f"1. MAE is ${mae:.2f}, representing average absolute dollar deviations.")
    print(f"2. RMSE is ${rmse:.2f}. Notice that RMSE is significantly larger than MAE.")
    print("   This is because the squaring operation in MSE penalizes the single outlier error of $100,000 heavily.")
    print("=======================================")

if __name__ == "__main__":
    run_classification_metrics_demo()
    run_regression_metrics_demo()

"""
Key Takeaways:
- Classification accuracy can be highly misleading on imbalanced datasets.
- Precision shrinks False Positives; Recall shrinks False Negatives.
- RMSE penalizes extreme outlier errors heavily compared to MAE due to the squaring penalty.

Interview Relevance:
- If a dataset is highly imbalanced (e.g. 99% non-fraud, 1% fraud), is accuracy a good metric? (No. A naive model that classifies everything as non-fraud will achieve 99% accuracy but fail to detect any fraud. Focus on Recall, Precision, or F1-Score instead).
- Explain the trade-off between Precision and Recall. (As you lower classification thresholds, you predict more positives, increasing Recall but introducing more false positives, which decreases Precision).
- What does R-squared represent? (R² measures the proportion of target variance explained by model features. An R² of 0.80 means 80% of target variance is captured by independent variables).

AI/ML Relevance:
- Objective Alignment: In medical diagnostics, minimizing false negatives (Recall) is prioritized. In spam filters, minimizing false positives (Precision) is prioritized.
- Loss Function: Optimization backpropagation algorithms directly use loss variants of these metrics (like Binary Cross Entropy or MSE) to train weights.
"""
