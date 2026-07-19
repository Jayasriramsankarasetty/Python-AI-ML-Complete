"""
Topic:
Supervised Learning - Support Vector Machines (SVM)

Importance:
SVMs are powerful margin-based models. They are highly effective for binary classification
problems, especially in high-dimensional spaces or when non-linear boundaries are present
via the Kernel Trick.

This file covers:
- Algorithm Explanation & When to use
- Seeding a classification dataset (Circular Non-Linear Boundaries)
- Preprocessing (train-test splits and scaling)
- Fitting the SVC model with RBF Kernel
- Regularization parameters (C, gamma)
- Evaluating performance using Accuracy, Precision, Recall, and F1 Score
"""

# ==========================================
# 1. Algorithm Explanation & When to use
# ==========================================
# Support Vector Machines (SVM) find the optimal decision boundary (hyperplane)
# that maximizes the margin (distance) between different classes.
#   - Support Vectors are the data points closest to the hyperplane.
#   - Regularization 'C' parameter: Controls the trade-off between maximizing the margin
#     and minimizing classification errors. High C values penalize misclassifications,
#     resulting in a narrower margin (risking overfitting).
#   - Kernel Trick: Maps low-dimensional non-linear features into high-dimensional space
#     where they become linearly separable. Common kernels: Linear, Polynomial, RBF (Gaussian).
#   - 'gamma' parameter (for RBF): Controls the influence of a single training point.
#     High gamma means only nearby points are considered, causing a complex boundary (overfitting).
#
# When to use:
# - Clear margin of separation in the data.
# - High-dimensional datasets (e.g. text classification, gene sequencing).
# - Non-linear complex decision boundaries.

# ==========================================
# 2. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ==========================================
# 3. Load/Create Dataset
# ==========================================
# Scenario: Circular target distribution (Non-linear).
# Features: X1, X2 values. Targets lie inside a central radius circle (class 1), else outside (class 0).
np.random.seed(42)
n_samples = 150

X1 = np.random.uniform(-3, 3, n_samples)
X2 = np.random.uniform(-3, 3, n_samples)

# Circular boundary: X1^2 + X2^2 < 2.0 -> Class 1, else 0
y_circles = []
for x1_val, x2_val in zip(X1, X2):
    dist_sq = (x1_val**2) + (x2_val**2)
    # Add noise to boundaries
    prob = 0.90 if dist_sq < 2.2 else 0.05
    y_circles.append(np.random.choice([0, 1], p=[1 - prob, prob]))

df = pd.DataFrame({
    "x1": X1,
    "x2": X2,
    "label": y_circles
})

X = df[["x1", "x2"]]
y = df["label"]

# ==========================================
# 4. Preprocessing
# ==========================================
# Step A: Split data into 80% train and 20% test folds
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step B: Scale features (Z-Score Standardization)
# CRITICAL: SVMs calculate Euclidean distances between vectors.
# Unscaled data causes features with larger ranges to dominate the objective function.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# 5. Train Model
# ==========================================
# We use the Radial Basis Function (RBF) kernel to handle the circular boundary.
# C=1.0, gamma='scale' (auto scale based on features count)
model = SVC(kernel="rbf", C=1.0, gamma="scale", random_state=42)
model.fit(X_train_scaled, y_train)

# ==========================================
# 6. Predict
# ==========================================
y_pred = model.predict(X_test_scaled)

# ==========================================
# 7. Evaluate
# ==========================================
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("=======================================")
print("SVM Classifier Model Evaluation:")
print("=======================================")
print(f"Kernel type used: {model.kernel}")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")
print("=======================================")

# ==========================================
# 8. Simple Interpretation & Conclusion
# ==========================================
print("\n--- Interpretation ---")
print(f"1. RBF Kernel maps the {X.shape[1]}-dimensional space into a higher-dimensional space,")
print("   enabling linear separation of the circular boundaries.")
print("2. Support vectors count:", len(model.support_))
print("   These are the critical threshold border cases used to construct the hyperplane margins.")
print("=======================================")

"""
Key Takeaways:
- SVM maximizes the separation margin between classes; Support Vectors are the closest border points.
- Feature scaling is mandatory since SVM computes vector Euclidean distances.
- RBF Kernel uses radial curves to separate complex, non-linear boundaries.

Interview Relevance:
- What is the Kernel Trick and why is it useful? (It allows SVM to solve non-linear classification problems by mapping data into higher dimensions where it becomes linearly separable, calculating this mapping implicitly without expensive coordinate computations).
- What does the C parameter control in SVM? (It controls the margin trade-off. A small C allows some misclassifications for a wider, generalized margin; a large C penalizes errors heavily, creating a narrow margin that risks overfitting).
- What does the gamma parameter control? (For RBF kernel, gamma controls the reach of individual points. A low gamma means far-away points influence the boundary; a high gamma means only nearby points influence it, creating a wavy, overfitted boundary).

AI/ML Relevance:
- Text Classification: Extremely effective for text classification (like spam or sentiment analysis) because SVM handles high-dimensional sparse representations well.
- Robust Classification: Provides robust margins for small but complex numeric datasets.
"""
