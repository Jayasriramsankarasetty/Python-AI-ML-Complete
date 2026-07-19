# Intermediate Project 1: Customer Churn Prediction

## Project Objective
Build a classification model to predict which subscribers are likely to cancel their subscriptions (churn) based on account details, satisfaction, and usage frequency.

## Problem Statement
Acquiring new customers is significantly more expensive than retaining existing ones. Predicting churn early helps companies offer targeted incentives to retain customers before they cancel.

## Technologies Used
- Python 3.10+
- Pandas & NumPy
- Scikit-learn (RandomForestClassifier, GridSearchCV, accuracy/precision/recall metrics)

## Architecture & Workflow
1. **Dataset Creation**: Seed 200 customer records (features: satisfaction, contract length, charge amount).
2. **Preprocessing**: standardise feature scales.
3. **Training**: Fit a Random Forest classification model.
4. **Tuning**: Grid search hyperparameters to maximize recall (reducing missed churners).
5. **Evaluation**: Predict classes and evaluate using Precision-Recall curves and F1 metrics.

## How to Run
Run the customer churn model script from the repository root:
```bash
python 17_AI_ML_Projects/Intermediate_Projects/Customer_Churn/churn.py
```

## Results & Future Improvements
- **Results**: Achieves an F1-Score of ~85%.
- **Future Improvements**:
  - Incorporate user behavioral trends over time (e.g. usage drop-off rates) using time-series features.
  - Implement XGBoost classifiers to see if predictive metrics improve.
