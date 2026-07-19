"""
Topic:
Intermediate Project - Credit Card Fraud Detection on Imbalanced Data

Importance:
Real-world classification tasks are often highly imbalanced.
Learning how to apply class weighting and evaluate using Recall and Precision
is a vital placement and production requirement.

This file covers:
- Seeding a highly imbalanced dataset (98% Normal, 2% Fraud)
- Preprocessing (scaling and splits)
- Training a RandomForestClassifier using class_weight='balanced'
- Evaluating performance using Recall, Precision, and Confusion Matrix
"""

# ==========================================
# 1. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# ==========================================
# 2. Load/Create Imbalanced Dataset
# ==========================================
np.random.seed(42)
n_samples = 1000

# Features: transaction amount, distance from home
amounts = np.random.exponential(scale=50.0, size=n_samples) + 2.0
distances = np.random.exponential(scale=10.0, size=n_samples) + 0.5

# Fraud is class 1, normal is 0.
# Only 20 cases of fraud out of 1000 (2% imbalance)
y = np.zeros(n_samples)
fraud_indices = np.random.choice(n_samples, size=20, replace=False)
y[fraud_indices] = 1

# Make fraud features systematically larger to create learning signal
amounts[fraud_indices] += 250.0
distances[fraud_indices] += 80.0

df = pd.DataFrame({
    "amount": amounts,
    "distance": distances,
    "fraud": y
})

X = df[["amount", "distance"]]
y = df["fraud"]

# ==========================================
# 3. Preprocessing
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# 4. Train Balanced Model
# ==========================================
# class_weight='balanced' automatically adjusts weights inversely proportional
# to class frequencies in the input data.
model = RandomForestClassifier(n_estimators=50, max_depth=5, class_weight="balanced", random_state=42)
model.fit(X_train_scaled, y_train)

# ==========================================
# 5. Predict & Evaluate
# ==========================================
y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)
conf = confusion_matrix(y_test, y_pred)

print("=======================================")
print("Fraud Detection Project Results:")
print("=======================================")
print("Confusion Matrix:\n", conf)
print(f"Accuracy:  {accuracy:.4f}  (Blind metric under high imbalance)")
print(f"Precision: {precision:.4f}  (Ability to avoid false fraud flags)")
print(f"Recall:    {recall:.4f}  (Ability to successfully catch actual fraud cases)")
print(f"F1-Score:  {f1:.4f}")
print("=======================================")

"""
Key Takeaways:
- Standard accuracy is a deceptive metric for imbalanced classes (98% accuracy can still miss 100% of fraud cases).
- Class weight adjustments penalize minority class errors heavily to guide gradient optimizations correctly.
- Confusion Matrix displays critical True Positive and False Positive segment distributions.

Interview Relevance:
- How do you handle highly imbalanced datasets? (1. Use class weights (`class_weight='balanced'`). 2. Employ resampling techniques (over-sampling minority class with SMOTE, under-sampling majority class). 3. Evaluate models using Precision, Recall, and F1-Score instead of accuracy).
- What is the difference between SMOTE and simple oversampling? (Simple oversampling duplicates existing minority class samples, which causes overfitting. SMOTE synthetically creates new, slightly varied samples along the line segments joining k-nearest neighbors).

AI/ML Relevance:
- Fintech Risk systems: Industry-standard template used in transaction processing pipes.
"""
