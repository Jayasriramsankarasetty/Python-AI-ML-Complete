"""
Topic:
Model Tuning - Hyperparameter Optimization (GridSearchCV & RandomizedSearchCV)

Importance:
Default model parameters are rarely optimal for a specific dataset.
Systematically searching hyperparameter spaces (like tree counts, tree depth limits)
ensures we capture the absolute best model score bounds without manual guesswork.

This file covers:
- Concepts: Parameters vs Hyperparameters
- GridSearchCV (Exhaustive search)
- RandomizedSearchCV (Randomized sampling search)
- Preprocessing & scaling steps
- Seeding data & Random Forest classifier tuning
- Evaluating scores and identifying best parameter selections
"""

# ==========================================
# 1. Concept Explanation & When to use
# ==========================================
# Parameters are learned by the model during training (e.g. weights, biases, tree node splits).
# Hyperparameters are set by the engineer before training (e.g. learning rate, tree count, tree depth).
# Optimization Strategies:
#   1. GridSearchCV: Evaluates *every* possible combination of hyperparameters in a defined grid.
#      Guarantees finding the best grid point, but is computationally slow.
#   2. RandomizedSearchCV: Randomly samples combinations from defined distributions for a fixed count
#      of iterations (n_iter). Highly efficient, fast, and close in accuracy to Grid Search.
#
# When to use:
# - Scaling up baseline model accuracy.
# - Tuning ensemble parameters (n_estimators, max_depth, max_features).
# - Optimizing support vector margins (C, kernel, gamma) or regularization weights.

# ==========================================
# 2. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# ==========================================
# 3. Load/Create Dataset
# ==========================================
# Make a binary classification dataset using sklearn utility
X_raw, y_raw = make_classification(
    n_samples=150, 
    n_features=5, 
    n_informative=3, 
    n_classes=2, 
    random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(X_raw, y_raw, test_size=0.2, random_state=42)

# ==========================================
# 4. Define Hyperparameter Space
# ==========================================
# Param Grid for Random Forest
# We search combinations of:
#   - n_estimators: [10, 30, 50]
#   - max_depth: [3, 5, 8]
#   - min_samples_split: [2, 5]
param_grid = {
    "n_estimators": [10, 30, 50],
    "max_depth": [3, 5, 8],
    "min_samples_split": [2, 5]
}

# ==========================================
# 5. GridSearchCV Demonstration
# ==========================================
print("=======================================")
print("1. Running GridSearchCV (Exhaustive Search)...")
print("=======================================")
# Total runs: 3 (n_estimators) * 3 (max_depth) * 2 (min_splits) = 18 combinations
# cv=3 means 18 * 3 = 54 total training iterations
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=3,
    scoring="accuracy",
    n_jobs=-1  # use all available CPU cores
)
grid_search.fit(X_train, y_train)

print(f"Grid Search Best Accuracy Score: {grid_search.best_score_:.4f}")
print("Grid Search Best Parameters:    ", grid_search.best_params_)

# ==========================================
# 6. RandomizedSearchCV Demonstration
# ==========================================
print("\n=======================================")
print("2. Running RandomizedSearchCV (Random Sampling)...")
print("=======================================")
# n_iter=5 means we only evaluate 5 random combinations
# cv=3 means 5 * 3 = 15 total training iterations
random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_grid,
    n_iter=5,
    cv=3,
    scoring="accuracy",
    random_state=42,
    n_jobs=-1
)
random_search.fit(X_train, y_train)

print(f"Randomized Search Best Score:    {random_search.best_score_:.4f}")
print("Randomized Search Best Params:   ", random_search.best_params_)

# ==========================================
# 7. Evaluate Best Model on Test Set
# ==========================================
best_model = grid_search.best_estimator_
test_accuracy = best_model.score(X_test, y_test)

print("\n=======================================")
print("Best Model Test Evaluation:")
print("=======================================")
print(f"Accuracy of best model on Test Set: {test_accuracy:.4f}")
print("=======================================")

# ==========================================
# 8. Simple Interpretation & Conclusion
# ==========================================
print("\n--- Interpretation ---")
print("1. Grid Search checked all 18 combinations, finding the absolute maximum accuracy parameters.")
print(f"2. Randomized Search checked only 5 random samples (reducing search compute time by ~72%),")
print(f"   yet achieved a comparable accuracy score.")
print("   For large hyperparameter grids, RandomizedSearchCV is the preferred industry approach.")
print("=======================================")

"""
Key Takeaways:
- Hyperparameters are configured before training, whereas parameters are learned during training.
- GridSearchCV performs exhaustive search; RandomizedSearchCV randomly samples combinations, saving compute.
- Always evaluate tuned models on a separate test split to verify generalization accuracy.

Interview Relevance:
- What is the difference between GridSearchCV and RandomizedSearchCV? (GridSearchCV evaluates every possible parameter combination, which is computationally expensive; RandomizedSearchCV samples a fixed number of random parameter combinations, which is significantly faster and often yields close-to-optimal results).
- How do you prevent overfitting during hyperparameter tuning? (Run hyperparameter searches using Cross-Validation, which evaluates performance across multiple data splits instead of overfitting to a single split).
- What does n_jobs=-1 do in scikit-learn searches? (It forces the engine to run the cross-validation fits in parallel across all available CPU cores, significantly speeding up execution times).

AI/ML Relevance:
- Fine-Tuning: Vital step in ML workflows to maximize model scores before deployment.
- Pipeline Optimization: Automatically searches preprocessor parameters (like SelectKBest 'k') alongside model parameters within scikit-learn Pipelines.
"""
