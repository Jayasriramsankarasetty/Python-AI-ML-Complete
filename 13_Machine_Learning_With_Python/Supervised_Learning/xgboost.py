"""
Topic:
Supervised Learning - XGBoost (Extreme Gradient Boosting)

Importance:
XGBoost is a highly optimized gradient boosting ensemble model.
It is an industry-standard algorithm for tabular datasets, frequently winning Kaggle
competitions due to its speed, regularization capabilities, and high accuracy.

This file covers:
- Algorithm Explanation & When to use
- Seeding a classification dataset
- Preprocessing (train-test splits)
- Fitting the XGBoost model (with scikit-learn GradientBoosting fallback)
- Evaluating performance using Accuracy, Precision, Recall, and F1 Score
"""

# ==========================================
# 1. Algorithm Explanation & When to use
# ==========================================
# XGBoost belongs to the Gradient Boosting family of ensemble algorithms.
# Unlike Bagging (which trains trees independently in parallel), Boosting trains trees sequentially:
#   1. Train a weak decision tree on the dataset.
#   2. Compute residual prediction errors (loss).
#   3. Train the next tree to predict those residual errors, minimizing the objective loss.
#   4. Aggregate predictions: y = tree_1 + learning_rate * tree_2 + learning_rate * tree_3 ...
# XGBoost (Extreme Gradient Boosting) adds:
#   - Built-in L1 and L2 regularization to penalize tree complexity and avoid overfitting.
#   - Sparsity-aware split finding (efficient handling of missing values).
#   - Parallelized tree structures and cache-aware indexing for extreme speed.
#
# When to use:
# - Large tabular datasets where predictive accuracy is the primary goal.
# - You need robust handling of missing values, skewness, and non-linear relationships.
# - You want a state-of-the-art classifier/regressor with extensive hyperparameter tuning controls.

# ==========================================
# 2. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Try importing xgboost; fallback to scikit-learn GradientBoosting if not installed
use_xgb_lib = True
try:
    import sys
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path = [p for p in sys.path if os.path.abspath(p) != current_dir]
    import xgboost as xgb
    # Force check for attribute to trigger exception if circular import is still cached
    _ = xgb.XGBClassifier
    print("Using native 'xgboost' library.")
except (ImportError, AttributeError):
    from sklearn.ensemble import GradientBoostingClassifier
    use_xgb_lib = False
    print("XGBoost library not found or conflict occurred. Falling back to scikit-learn GradientBoostingClassifier.")

# ==========================================
# 3. Load/Create Dataset
# ==========================================
# Scenario: Customer Churn prediction
# Features: Tenure (months), Monthly Charges ($), Support Tickets Count.
np.random.seed(42)
n_samples = 200

tenure = np.random.uniform(1, 72, size=n_samples)
charges = np.random.uniform(20, 120, size=n_samples)
tickets = np.random.choice([0, 1, 2, 3, 4, 5], size=n_samples, p=[0.4, 0.3, 0.15, 0.08, 0.05, 0.02])

# Non-linear churn rule (1 = churn, 0 = active)
churn = []
for t, c, tk in zip(tenure, charges, tickets):
    prob = 0.10
    # Higher churn probability if tenure is short AND charges are high, or if tickets count is large
    if t < 12 and c > 80.0:
        prob = 0.75
    if tk >= 3:
        prob += 0.30
    prob = min(0.95, prob)
    churn.append(np.random.choice([0, 1], p=[1 - prob, prob]))

df = pd.DataFrame({
    "tenure": tenure,
    "charges": charges,
    "tickets": tickets,
    "churn": churn
})

X = df[["tenure", "charges", "tickets"]]
y = df["churn"]

# ==========================================
# 4. Preprocessing
# ==========================================
# Split data into 80% train and 20% test folds
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 5. Train Model
# ==========================================
if use_xgb_lib:
    # Use scikit-learn compatible XGBoost wrapper API
    model = xgb.XGBClassifier(
        n_estimators=50,
        max_depth=4,
        learning_rate=0.1,
        random_state=42,
        eval_metric="logloss"
    )
else:
    # Fallback Gradient Boosting
    model = GradientBoostingClassifier(
        n_estimators=50,
        max_depth=4,
        learning_rate=0.1,
        random_state=42
    )

model.fit(X_train, y_train)

# ==========================================
# 6. Predict
# ==========================================
y_pred = model.predict(X_test)

# ==========================================
# 7. Evaluate
# ==========================================
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("=======================================")
print("Boosting Ensemble Model Evaluation:")
print("=======================================")
print(f"Algorithm Class: {model.__class__.__name__}")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")
print("=======================================")

# ==========================================
# 8. Simple Interpretation & Conclusion
# ==========================================
print("\n--- Interpretation ---")
print("1. Boosting models train sequentially, forcing each new tree to focus on previous errors.")
print(f"2. Accuracy of {accuracy*100:.1f}% shows that this sequential focus successfully converged.")
print("3. Feature Importances:")
for col, score in zip(X.columns, model.feature_importances_):
    print(f"   - {col}: {score:.4f}")
print("=======================================")

"""
Key Takeaways:
- Boosting trains trees sequentially (additive training), building each tree to correct errors of the prior tree.
- XGBoost implements shrinkage (learning rate) and regularization penalties to prevent model overfits.
- Tabular data models are best served by gradient boosted trees, yielding higher metrics than standard single trees.

Interview Relevance:
- Explain the key difference between Bagging and Boosting. (Bagging trains trees in parallel on bootstrap samples, reducing variance; Boosting trains trees sequentially, where each tree minimizes prior residuals, reducing bias).
- How does XGBoost handle missing values? (It learns a default splitting direction for missing values at each node. During training, if a value is missing, it evaluates both paths and assigns it to the direction that yields higher gain).
- What does the learning rate (eta) do in XGBoost? (It shrinks the weights of new trees added to the ensemble, slowing down training and requiring more trees, which helps prevent overfitting).

AI/ML Relevance:
- Production Standard: Tabular predictive tasks in fintech, recommendations, and logistics utilize XGBoost due to its high efficiency and accuracy.
- Baseline models: Forms the target competitor for any advanced neural networks model trained on structured business tables.
"""
