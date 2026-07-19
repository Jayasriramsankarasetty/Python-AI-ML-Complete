"""
Topic:
Supervised Learning - Decision Tree Classifier

Importance:
Decision Trees partition datasets recursively using condition thresholds.
They are highly intuitive, require minimal preprocessing (no scaling needed),
and form the building blocks for ensemble models like Random Forest and XGBoost.

This file covers:
- Algorithm Explanation & When to use
- Seeding a classification dataset
- Preprocessing (train-test splits)
- Fitting the DecisionTreeClassifier model
- Controlling tree depth to prevent overfitting
- Evaluating performance using Accuracy, Precision, Recall, and F1 Score
"""

# ==========================================
# 1. Algorithm Explanation & When to use
# ==========================================
# A Decision Tree is a flowchart-like tree structure where:
#   - Internal nodes represent feature test checks.
#   - Branches represent check results (True/False).
#   - Leaf nodes represent class outcome decisions.
# Splits are chosen recursively to maximize the "Information Gain" by minimizing:
#   - Gini Impurity: Gini = 1 - Σ (p_i)²
#   - Entropy: Entropy = - Σ p_i * log2(p_i)
# Decision Trees easily overfit if allowed to grow deep, memorizing training noises.
# Regularization parameters include `max_depth`, `min_samples_split`, and `min_samples_leaf`.
#
# When to use:
# - Relationships are non-linear and feature scaling/normalization is not desired.
# - You need high model interpretability (explaining predictions via decision rules).
# - You have mixed numerical and categorical features.

# ==========================================
# 2. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ==========================================
# 3. Load/Create Dataset
# ==========================================
# Scenario: Loan default prediction.
# Features: Credit Score (300-850) and Debt-to-Income (DTI) ratio (0.0 - 1.0).
np.random.seed(42)
n_samples = 150

credit_scores = np.random.randint(300, 850, size=n_samples)
dti_ratios = np.random.uniform(0.1, 0.9, size=n_samples)

# Non-linear split rules (Default class = 1, otherwise 0)
defaults = []
for cs, dti in zip(credit_scores, dti_ratios):
    if cs < 600 or (cs < 700 and dti > 0.4) or dti > 0.7:
        defaults.append(1)
    else:
        defaults.append(0)

df = pd.DataFrame({
    "credit_score": credit_scores,
    "dti_ratio": dti_ratios,
    "default": defaults
})

X = df[["credit_score", "dti_ratio"]]
y = df["default"]

# ==========================================
# 4. Preprocessing
# ==========================================
# Split data into 80% train and 20% test folds
# Note: Decision trees do NOT require scaling/standardization since splits
# evaluate features individually without computing distances.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 5. Train Model
# ==========================================
# We constrain `max_depth` to 4 to prevent the tree from overfitting.
model = DecisionTreeClassifier(criterion="gini", max_depth=4, random_state=42)
model.fit(X_train, y_train)

# ==========================================
# 6. Predict
# ==========================================
y_pred = model.predict(X_test)

# ==========================================
# 7. Evaluate
# ==========================================
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("=======================================")
print("Decision Tree Model Evaluation:")
print("=======================================")
print(f"Max Depth constraint: {model.max_depth}")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")
print("=======================================")

# ==========================================
# 8. Simple Interpretation & Conclusion
# ==========================================
print("\n--- Interpretation ---")
print(f"1. Accuracy of {accuracy*100:.1f}% indicates our decision rules perform well on unseen profiles.")
print(f"2. Gini Impurity splits feature axes orthogonally (e.g. credit_score <= 598.5).")
print("3. Feature Importances:")
for col, score in zip(X.columns, model.feature_importances_):
    print(f"   - {col}: {score:.4f}")
print("   Here, the model identifies Credit Score as carrying the largest information split weight.")
print("=======================================")

"""
Key Takeaways:
- Decision Trees split features orthogonally to maximize information gain/decrease impurity.
- Pruning parameters (like `max_depth` and `min_samples_split`) are critical to prevent overfitting.
- Decision trees are invariant to feature scaling (scaling does not change split ordering).

Interview Relevance:
- Explain Gini Impurity vs Entropy. (Gini measures the probability of misclassifying a chosen element if it were randomly labeled according to the distribution; Entropy measures information uncertainty. Gini is computationally faster since it doesn't calculate log operations).
- What is Overfitting in Decision Trees and how do you prevent it? (When a tree grows too deep, memorizing training noise. Prevent it via pre-pruning: setting `max_depth`, `min_samples_leaf`, or post-pruning: cost-complexity pruning).
- Why do Decision Trees split orthogonally? (Each split evaluates a single feature column, creating splits parallel to feature axes).

AI/ML Relevance:
- Base Ensemble Class: Random Forests and XGBoost combine hundreds of shallow decision trees to stabilize variance and bias.
- Non-linear Boundaries: Ideal for modeling step-function thresholds in datasets without heavy preprocessing.
"""
