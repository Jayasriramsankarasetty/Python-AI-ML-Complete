# Supervised Learning Algorithms

Supervised Learning models train on labeled datasets containing input features and a matching target label. The algorithm infers a mapping function to predict labels on unseen test records.

---

## Folder Contents

This sub-folder contains detailed algorithm implementations from scratch utilizing scikit-learn and XGBoost:

1. [linear_regression.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Supervised_Learning/linear_regression.py):
   * Regression model predicting continuous values (Home Prices) using Ordinary Least Squares (OLS) fit.
2. [logistic_regression.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Supervised_Learning/logistic_regression.py):
   * Probabilistic classification model classifying customer churn using sigmoid functions.
3. [decision_tree.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Supervised_Learning/decision_tree.py):
   * Non-parametric classification tree splitting nodes using Gini impurity thresholds.
4. [random_forest.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Supervised_Learning/random_forest.py):
   * Bagging ensemble method combining multiple decision trees to stabilize variance.
5. [svm.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Supervised_Learning/svm.py):
   * Margin classifier maximizing separations boundaries using linear/radial kernels.
6. [xgboost.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Supervised_Learning/xgboost.py):
   * Gradient boosting ensemble training weak trees sequentially to minimize residual loss.

---

## Coding Format Rules for ML files

Every file includes:
1. **Algorithm Explanation** in comments.
2. **When to use** guidelines.
3. **Dataset Seeding** example.
4. **Data preprocessing** structures (splits & scaling).
5. **Model training** fit step.
6. **Prediction** predictions output.
7. **Evaluation metrics** print checks.
8. **Simple Interpretation** of outputs.
