"""
Topic:
Intermediate Project - Customer Churn Prediction using Random Forest

Importance:
Churn analysis is a high-value business task. This project uses
an ensemble Random Forest model to handle non-linear boundaries.

This file covers:
- Loading customer records (Tenure, Satisfaction, Charges)
- Splitting train-test subsets
- Standardizing features
- Training a RandomForestClassifier
- Outputting classification reports (Accuracy, Precision, Recall, F1)
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
# 2. Load/Create Dataset
# ==========================================
np.random.seed(42)
n_samples = 200

tenure = np.random.uniform(1.0, 72.0, n_samples)
satisfaction = np.random.uniform(1.0, 10.0, n_samples)
charges = np.random.normal(70, 20, n_samples)

# Churn = 1 (Left) or 0 (Retained)
# Higher churn if tenure is short and satisfaction is low
y = []
for t, s, c in zip(tenure, satisfaction, charges):
    prob = 0.05
    if t < 12 and s < 5:
        prob = 0.80
    elif s < 3:
        prob = 0.60
    y.append(np.random.choice([0, 1], p=[1 - prob, prob]))

df = pd.DataFrame({
    "tenure": tenure,
    "satisfaction": satisfaction,
    "charges": charges,
    "churn": y
})

X = df[["tenure", "satisfaction", "charges"]]
y = df["churn"]

# ==========================================
# 3. Preprocessing
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# 4. Train Model
# ==========================================
model = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
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
print("Customer Churn Prediction Project Results:")
print("=======================================")
print("Confusion Matrix:\n", conf)
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")
print("=======================================")

"""
Key Takeaways:
- Random Forest ensembles combine multiple weak decision trees to reduce overall variance.
- Evaluating churn requires balancing Precision (preventing false incentives) and Recall (catching true churners).
- Feature scaling ensures consistent optimization boundaries during preprocessing.

Interview Relevance:
- Which metric is more important for churn prediction: Precision or Recall? (Typically Recall, because missing a customer who is about to churn costs the business far more than offering a discount to a customer who wasn't planning to leave. However, if the cost of the incentive is very high, you must balance both metrics).

AI/ML Relevance:
- Customer Analytics: Industry-standard workflow template to construct churn alert systems.
"""
