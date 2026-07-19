"""
Topic:
Supervised Learning - Logistic Regression

Importance:
Logistic Regression is the standard baseline algorithm for binary classification problems.
It outputs probabilities, is fast to train, and serves as an industry standard for credit scoring
and conversion propensity modeling.

This file covers:
- Algorithm Explanation & When to use
- Seeding a binary classification dataset (Employee Churn)
- Train-test splitting & scaling preprocessing
- Fitting the LogisticRegression model
- Extracting class predictions and probability scores
- Evaluating performance using Accuracy, Precision, Recall, F1, and Confusion Matrix
"""

# ==========================================
# 1. Algorithm Explanation & When to use
# ==========================================
# Logistic Regression predicts the probability that an input sample belongs to a binary class (0 or 1).
# It applies the Sigmoid (Logistic) Function to map real-valued output ranges into [0, 1] probability limits.
# Sigmoid Formula: P(y = 1 | X) = 1 / (1 + e^-z)
#   - where z = β0 + β1*x1 + ... + βn*xn (log-odds linear projection).
# If P >= 0.5, class prediction = 1 (Positive class); else 0 (Negative class).
# Optimization uses Cross-Entropy (Log Loss) function minimization.
#
# When to use:
# - Target variable is binary categorical (e.g. Yes/No, Spam/Ham, Churn/Retained).
# - You need class probability outputs (e.g. 78% probability of transaction fraud).
# - You need an interpretable, fast baseline classification model.

# ==========================================
# 2. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# ==========================================
# 3. Load/Create Dataset
# ==========================================
# Scenario: Predicting employee attrition (Churn_Status: 1 = Left, 0 = Retained)
# Features: Satisfaction_Score (1-10) and Monthly_Salary ($).
np.random.seed(42)
n_samples = 150

satisfaction = np.random.normal(6.0, 2.0, n_samples)
satisfaction = np.clip(satisfaction, 1, 10)  # constrain between 1 and 10

salary = np.random.normal(6000, 1500, n_samples)

# Probabilistic churn rules (higher churn when satisfaction is low)
log_odds = 5.0 - (satisfaction * 1.2) - (salary * 0.0002)
probs = 1 / (1 + np.exp(-log_odds))
churn = np.random.binomial(1, probs)

df = pd.DataFrame({
    "satisfaction": satisfaction,
    "salary": salary,
    "churn": churn
})

X = df[["satisfaction", "salary"]]
y = df["churn"]

# ==========================================
# 4. Preprocessing
# ==========================================
# Step A: Split data into 80% train and 20% test folds
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step B: Scale features (Z-Score Standardization)
# Crucial for Logistic Regression regularized optimization solver bounds.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# 5. Train Model
# ==========================================
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# ==========================================
# 6. Predict
# ==========================================
# Predict hard class labels (0 or 1)
y_pred = model.predict(X_test_scaled)

# Predict continuous probability scores (P(y=0), P(y=1))
y_prob = model.predict_proba(X_test_scaled)[:, 1]

# ==========================================
# 7. Evaluate
# ==========================================
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("=======================================")
print("Logistic Regression Model Evaluation:")
print("=======================================")
print("Confusion Matrix:\n", conf_matrix)
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")
print("=======================================")

# ==========================================
# 8. Simple Interpretation & Conclusion
# ==========================================
print("\n--- Interpretation ---")
print(f"1. Accuracy of {accuracy*100:.1f}% indicates the proportion of correct classification flags.")
print(f"2. Precision of {precision*100:.1f}% means that out of all employees predicted to churn,")
print("   that percentage actually did leave.")
print(f"3. Recall of {recall*100:.1f}% means we successfully captured that percentage of the total actual churned pool.")
print("   If HR wants to minimize miss rates, they should focus on improving Recall.")
print("=======================================")

"""
Key Takeaways:
- Logistic Regression maps continuous log-odds equations to probability scores [0, 1] using the Sigmoid curve.
- Confusion Matrix segments classification results into: TP (True Positives), FP (False Positives), TN (True Negatives), and FN (False Negatives).
- Accuracy measures general correctness; Precision filters false alarm costs; Recall checks target capture rates.

Interview Relevance:
- Why do we use Log Loss instead of Mean Squared Error (MSE) in Logistic Regression? (MSE with sigmoid outputs creates a non-convex optimization surface with multiple local minima. Log Loss is convex, guaranteeing that gradient descent finds the global minimum).
- What are L1 and L2 regularization in Logistic Regression? (L1 / Lasso penalizes absolute weight magnitudes, forcing uninformative coefficients to exactly 0 for feature selection; L2 / Ridge penalizes squared magnitudes, shrinking coefficients towards 0 to reduce overfitting).
- Explain the difference between Precision and Recall. (Precision = TP / (TP + FP) -> out of predicted positives, how many are actual positives. Recall = TP / (TP + FN) -> out of actual positives, how many did we successfully find).

AI/ML Relevance:
- Target Probability: Used in credit risk underwriting systems where predicting exact default probability (e.g. 5%) is needed to calculate price interest rate structures.
- Fast Inference: Extremely lightweight, requiring minimal compute resources to run predictions on millions of production client requests.
"""
