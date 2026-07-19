"""
Topic:
Model Evaluation - Cross-Validation Strategies (K-Fold & Stratified K-Fold)

Importance:
A simple train-test split can introduce sample bias (high variance in performance estimates).
Cross-Validation partitions the dataset into multiple folds, validating performance iteratively
across all subsets to compute a stable, generalizable average score.

This file covers:
- Concepts of K-Fold and Stratified K-Fold (for target balance maintenance)
- Seeding a classification dataset
- Preprocessing (Standardization)
- Executing K-Fold Cross-Validation loops using cross_val_score
- Executing Stratified K-Fold manually to track split counts
- Evaluating variance across folds
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression

# ==========================================
# 1. Concept Explanation & When to use
# ==========================================
# Cross-Validation splits a dataset into 'K' groups (folds).
#   1. Partition dataset into K equal folds.
#   2. In each iteration, use Fold K as the validation set, and the remaining K-1 folds as training set.
#   3. Fit the model and compute metrics.
#   4. Repeat K times, alternating the validation fold.
#   5. Compute average and standard deviation of metrics across all iterations.
# Stratified K-Fold ensures that each fold contains roughly the same percentage of target class labels
# as the entire dataset. Highly critical for imbalanced classes.
#
# When to use:
# - Evaluating small or medium-sized datasets where a single train-test split risks high sample bias.
# - Tuning hyperparameters (comparing models generalizability).
# - Validating imbalanced target distributions.

# ==========================================
# 2. Setup Dataset
# ==========================================
# Scenario: Imbalanced target labels (e.g. Fraud detection: 90% non-fraud, 10% fraud)
np.random.seed(42)
n_samples = 150

f1 = np.random.normal(0, 1, n_samples)
f2 = np.random.normal(0, 1, n_samples)

# Force imbalanced class y (15 fraud, 135 normal)
y = np.zeros(n_samples)
y[:15] = 1

X = np.column_stack((f1, f2))

# ==========================================
# 3. Preprocessing
# ==========================================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================================
# 4. Standard K-Fold Cross Validation
# ==========================================
print("=======================================")
print("1. Standard K-Fold Cross-Validation (K=5)")
print("=======================================")
kf = KFold(n_splits=5, shuffle=True, random_state=42)
model = LogisticRegression()

# cross_val_score automatically runs splits, trains, evaluates, and returns array scores
scores = cross_val_score(model, X_scaled, y, cv=kf, scoring="accuracy")

print("Accuracy score per fold:", scores)
print(f"Mean Accuracy:           {scores.mean():.4f}")
print(f"Scores Std Deviation:    {scores.std():.4f}")
print("=======================================")

# ==========================================
# 5. Stratified K-Fold Cross Validation
# ==========================================
print("\n=======================================")
print("2. Stratified K-Fold Class Balance Check")
print("=======================================")
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

fold_index = 1
for train_idx, val_idx in skf.split(X_scaled, y):
    y_train_split = y[train_idx]
    y_val_split = y[val_idx]
    # Check the balance of the positive label '1' in each validation split
    num_ones_val = np.sum(y_val_split == 1)
    print(f"Fold {fold_index} - Val Set size: {len(y_val_split)} | Pos Class Count: {num_ones_val}")
    fold_index += 1
print("=======================================")

# ==========================================
# 6. Simple Interpretation & Conclusion
# ==========================================
print("\n--- Interpretation ---")
print("1. Standard K-Fold splits data blindly. In cases of high target imbalance,")
print("   some validation folds might accidentally contain zero positive fraud cases, skewing accuracy metrics.")
print("2. Stratified K-Fold resolves this by guaranteeing that each validation fold contains")
print("   exactly 3 positive cases (15 positive cases total / 5 folds), providing stable error estimates.")
print("=======================================")

"""
Key Takeaways:
- Cross-Validation evaluates model stability across multiple data splits to reduce sample variance bias.
- Standard K-Fold is suited for balanced datasets; Stratified K-Fold is mandatory for imbalanced class distributions.
- Standard deviation across folds indicates how sensitive the model is to training data variations.

Interview Relevance:
- What is K-Fold Cross-Validation? (It is a validation strategy where the dataset is split into K equal folds, iteratively training on K-1 folds and validating on the remaining fold to compute a stable average score).
- When is Stratified K-Fold preferred over standard K-Fold? (When the target variable is highly imbalanced. Stratified K-Fold preserves class label percentages in each fold, preventing empty class folds).
- Why is cross-validation computationally expensive? (Because it requires fitting the model K times instead of once. For large deep learning models, cross-validation is often avoided or replaced by single validation sets).

AI/ML Relevance:
- Hyperparameter search: Cross-validation runs inside grid searches (GridSearchCV) to locate stable parameter coordinates.
- Generalization Audit: Comparing standard deviations across folds ensures models won't exhibit high variance in production.
"""
