"""
Topic:
Beginner Project - House Price Prediction using Linear Regression

Importance:
Regression is a cornerstone of ML. This project models continuous values,
showing a complete pipeline from mock data to prediction and metrics checking.

This file covers:
- Loading mock house datasets (Square Footage, Rooms Count)
- Splitting train-test subsets
- Standardizing features
- Training a LinearRegression estimator
- Outputting MSE, RMSE, R-squared evaluation metrics
"""

# ==========================================
# 1. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ==========================================
# 2. Load/Create Dataset
# ==========================================
# Features: sq_footage, rooms
np.random.seed(42)
n_samples = 100

sq_footage = np.random.normal(1800, 400, n_samples)
rooms = np.round(sq_footage / 450.0 + np.random.normal(1, 0.5, n_samples))
rooms = np.clip(rooms, 1, 5)

# Price = 50k + 120/sq_foot + 25k/room + noise
prices = 50000 + (sq_footage * 120) + (rooms * 25000) + np.random.normal(0, 10000, n_samples)

df = pd.DataFrame({
    "sq_footage": sq_footage,
    "rooms": rooms,
    "price": prices
})

X = df[["sq_footage", "rooms"]]
y = df["price"]

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
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# ==========================================
# 5. Predict & Evaluate
# ==========================================
y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("=======================================")
print("House Price Prediction Project Results:")
print("=======================================")
print(f"Model Intercept: ${model.intercept_:.2f}")
print(f"Feature Weights: {model.coef_}")
print(f"Test RMSE:       ${rmse:.2f}")
print(f"R-squared Score: {r2:.4f}")
print("=======================================")

"""
Key Takeaways:
- Standard OLS calculates line coordinates to minimize residuals squared distances.
- RMSE provides a clear metric of pricing errors in original dollar units.
- R-squared gauges the percentage of pricing variance explained by the model.

Interview Relevance:
- Explain what the coefficients represent in multiple linear regression. (They represent the change in the target variable for a one-unit change in that feature, holding all other features constant).
- What is the cost function of Linear Regression? (Mean Squared Error: (1/N) * Σ(y - y_hat)²).

AI/ML Relevance:
- Baseline builds: Exposes the primary regression benchmarks used to baseline real estate platforms.
"""
