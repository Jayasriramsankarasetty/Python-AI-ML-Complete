"""
Topic:
Supervised Learning - Random Forest Classifier

Importance:
Random Forest is a highly powerful bagging ensemble model.
By combining hundreds of decision trees with feature-wise bootstrapping, it stabilizes variance,
reduces overfitting, and outputs robust predictions on complex structured datasets.

This file covers:
- Algorithm Explanation & When to use
- Seeding a classification dataset
- Preprocessing (train-test splits)
- Fitting the RandomForestClassifier model
- Extracting feature importance scores
- Evaluating performance using Accuracy, Precision, Recall, and F1 Score
"""

# ==========================================
# 1. Algorithm Explanation & When to use
# ==========================================
# Random Forest is an ensemble learning method that uses Bootstrap Aggregation (Bagging).
# Process:
#   1. Bootstrapping: It draws multiple random samples with replacement from the dataset.
#   2. Feature Bagging: At each node split in a tree, it only considers a random subset
#      of features (typically √Features). This de-correlates the individual trees.
#   3. Aggregation: Individual trees are trained independently. Predictions are aggregated:
#      - Classification: Majority vote across trees.
#      - Regression: Average output across trees.
# This averaging de-noises individual high-variance predictions, stabilizing the ensemble model.
#
# When to use:
# - You have tabular data and want a highly accurate, robust model with low configuration tuning.
# - You want to measure feature importances in a non-linear dataset.
# - You have missing features or complex interaction boundaries.

# ==========================================
# 2. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ==========================================
# 3. Load/Create Dataset
# ==========================================
# Scenario: Credit Card Fraud Detection.
# Features: Transaction Amount ($), Distance from Home (miles), and Time of Day (hours).
np.random.seed(42)
n_samples = 200

amounts = np.random.exponential(scale=50.0, size=n_samples) + 5.0
distances = np.random.exponential(scale=10.0, size=n_samples) + 0.5
hours = np.random.uniform(0, 24, size=n_samples)

# Non-linear fraud rules (Fraud class = 1, otherwise 0)
frauds = []
for amt, dist, hr in zip(amounts, distances, hours):
    # High probability of fraud if amount is large AND distance is far, or if transaction is at midnight
    prob = 0.05
    if amt > 150.0 and dist > 30.0:
        prob = 0.85
    elif (hr < 4.0 or hr > 22.0) and amt > 100.0:
        prob = 0.70
    frauds.append(np.random.choice([0, 1], p=[1 - prob, prob]))

df = pd.DataFrame({
    "amount": amounts,
    "distance": distances,
    "hour": hours,
    "fraud": frauds
})

X = df[["amount", "distance", "hour"]]
y = df["fraud"]

# ==========================================
# 4. Preprocessing
# ==========================================
# Split data into 80% train and 20% test folds
# Note: Random Forest does not require feature scaling, but train-test splits are essential.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 5. Train Model
# ==========================================
# n_estimators: number of trees in the forest (default = 100)
# max_features: number of features to consider when looking for the best split (default = 'sqrt')
model = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
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
print("Random Forest Model Evaluation:")
print("=======================================")
print(f"Number of Trees (n_estimators): {model.n_estimators}")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")
print("=======================================")

# ==========================================
# 8. Simple Interpretation & Conclusion
# ==========================================
print("\n--- Feature Importances Profiling ---")
# Feature importances are calculated based on Gini decrease splits
importances = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)
print(importances)

print("\n--- Interpretation ---")
print(f"1. Random Forest averages the predictions of {model.n_estimators} independent trees.")
print(f"2. The primary fraud feature identified is '{importances.iloc[0]['Feature']}'")
print(f"   with an importance metric of {importances.iloc[0]['Importance']:.4f}.")
print("3. By decorrelating features across splits, Random Forest avoids overfitting to any single attribute.")
print("=======================================")

"""
Key Takeaways:
- Random Forest is an ensemble of decision trees trained independently using Bagging (Bootstrap Aggregation).
- Feature bagging decorrelates trees, reducing ensemble variance compared to single trees.
- It calculates feature importances based on Gini impurity decrease across splits.

Interview Relevance:
- Explain Bootstrap Aggregation (Bagging). (It is a technique that draws multiple random subsets of the data *with replacement* to train individual weak models, averaging outputs to reduce variance).
- How does Random Forest decorrelate individual trees? (By using feature bagging: selecting a random subset of columns to evaluate at each node split, preventing dominant features from dictating every tree).
- What is Out-Of-Bag (OOB) error? (Since rows are sampled with replacement, about 37% of data is left out of each tree. OOB error uses these left-out rows to evaluate performance during training, removing the need for a separate validation set).

AI/ML Relevance:
- Robust Classifiers: Highly useful as an accurate, non-linear classifier for tabular datasets without needing feature scaling.
- Feature Selection: Feature importances aid in ranking features to discard uninformative columns in early ETL pipelines.
"""
