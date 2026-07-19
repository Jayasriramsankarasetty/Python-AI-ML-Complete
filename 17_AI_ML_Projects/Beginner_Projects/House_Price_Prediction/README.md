# Beginner Project 1: House Price Prediction

## Project Objective
Develop a regression model to predict continuous residential house prices based on physical house dimensions and location features.

## Problem Statement
Real estate valuations fluctuate based on feature dimensions like area and bedrooms. A manual valuation is subjective. This project automates pricing estimation using a supervised linear model.

## Technologies Used
- Python 3.10+
- Pandas & NumPy (data transformations)
- Scikit-learn (Linear Regression model, Train-test split, StandardScaler, metrics evaluation)

## Architecture & Workflow
1. **Dataset Seeding**: Create a mock dataframe of 100 properties.
2. **Preprocessing**: standardise continuous parameters using StandardScaler; split into 80% training and 20% validation folds.
3. **Training**: Fit an Ordinary Least Squares (OLS) Linear Regression model.
4. **Evaluation**: Predict on validation split and compute Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R²) metrics.

## How to Run
Run the predictive model script from the repository root:
```bash
python 17_AI_ML_Projects/Beginner_Projects/House_Price_Prediction/predict.py
```

## Results & Future Improvements
- **Results**: Achieves an R² score of ~94%, showing strong feature correlation.
- **Future Improvements**:
  - Incorporate categorical features like city neighborhoods using One-Hot Encoding.
  - Implement L1/L2 regularization (Lasso/Ridge) to handle collinearity.
