"""
Topic:
Supervised Learning - Linear Regression

Importance:
Linear Regression is the foundation of predictive regression.
It is highly interpretable, fast, and acts as a baseline model for continuous outcomes.

This file covers:
- Algorithm Explanation & When to use
- Loading/Creating a mock dataset
- Train-test splitting & Feature scaling
- Fitting the LinearRegression model
- Evaluating predictions using MSE, RMSE, and R-squared
"""

# ==========================================
# 1. Algorithm Explanation & When to use
# ==========================================
# Linear Regression models a linear relationship between input features (X)
# and a continuous target variable (y).
# Formula: y = β0 + β1*x1 + β2*x2 + ... + βn*xn + ε
#   - β0 is the intercept.
#   - β1, β2... are the coefficients (slopes) representing feature weights.
#   - ε is the random error term.
# The model optimizes coefficients to minimize the Residual Sum of Squares (RSS)
# using Ordinary Least Squares (OLS).
#
# When to use:
# - The target variable is continuous (e.g. house price, sales volume, temperature).
# - You expect a linear relationship between features and the target.
# - Interpretation of feature importance (slopes) is highly critical.

# ==========================================
# 2. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ==========================================
# 3. Load/Create Dataset
# ==========================================
# Scenario: Predicting house prices based on Square Footage and Number of Bedrooms.
np.random.seed(42)
n_samples = 150

sq_footage = np.random.normal(2000, 500, n_samples)
bedrooms = np.random.choice([2, 3, 4, 5], size=n_samples, p=[0.2, 0.5, 0.2, 0.1])
# House price base: 100k + 150/sq_foot + 30k/bedroom + random noise
prices = 100000 + (sq_footage * 150) + (bedrooms * 30000) + np.random.normal(0, 15000, n_samples)

df = pd.DataFrame({
    "sq_footage": sq_footage,
    "bedrooms": bedrooms,
    "price": prices
})

X = df[["sq_footage", "bedrooms"]]
y = df["price"]

# ==========================================
# 4. Preprocessing
# ==========================================
# Step A: Split dataset into 80% train and 20% test folds
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step B: Scale features (Z-Score Standardization)
# Fit scaler ONLY on training data, transform both train and test splits.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# 5. Train Model
# ==========================================
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# ==========================================
# 6. Predict
# ==========================================
y_pred = model.predict(X_test_scaled)

# ==========================================
# 7. Evaluate
# ==========================================
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("=======================================")
print("Linear Regression Model Evaluation:")
print("=======================================")
print(f"Model Intercept (beta_0):             ${model.intercept_:.2f}")
print(f"Standardized Coefficients (slopes):   {model.coef_}")
print(f"Mean Squared Error (MSE):             {mse:.4f}")
print(f"Root Mean Squared Error (RMSE):       ${rmse:.2f}")
print(f"R-squared Score (R²):                 {r2:.4f}")
print("=======================================")

# ==========================================
# 8. Simple Interpretation & Conclusion
# ==========================================
print("\n--- Interpretation ---")
print(f"1. R-squared value of {r2:.4f} means that {r2*100:.1f}% of the variance in house prices")
print("   is explained by Square Footage and Number of Bedrooms.")
print(f"2. The Root Mean Squared Error (RMSE) shows that our price predictions typically")
print(f"   deviate from the actual house prices by around ${rmse:.2f}.")
print(f"3. Feature Coefficients: Square Footage scale weight is {model.coef_[0]:.2f}, and Bedrooms is {model.coef_[1]:.2f}.")
print("   Both have positive coefficients, showing that larger houses and more bedrooms lead to higher prices.")
print("=======================================")

"""
Key Takeaways:
- Linear Regression optimizes weights using Ordinary Least Squares (OLS) to minimize Mean Squared Error.
- R-squared measures the proportion of variance explained by features; 1.0 is a perfect fit.
- Standardizing variables lets you compare coefficient scales directly to rank feature importances.

Interview Relevance:
- What are the core assumptions of Linear Regression? (Linearity, Independence of errors, Homoscedasticity - constant variance of residuals, Normality of residuals distribution).
- Explain R-squared vs Adjusted R-squared. (R-squared always increases or stays constant when new features are added; Adjusted R-squared adjusts for the number of predictors, penalizing columns that add no predictive power).
- What is multicollinearity and how does it affect Linear Regression? (It refers to high correlations between independent features. It makes coefficient estimates unstable, inflating standard error bounds).

AI/ML Relevance:
- Base Estimates: Acts as a fast, computationally cheap benchmark model for continuous predictions.
- Regularization: Standard OLS can overfit when features are numerous; adding L1 (Lasso) or L2 (Ridge) penalties controls complexity.
"""
