# Intermediate Project 3: Credit Card Fraud Detection

## Project Objective
Develop a classification pipeline capable of identifying fraudulent credit card transactions from highly imbalanced transaction streams.

## Problem Statement
Fraudulent transactions make up less than 0.5% of total card swipes. Normal classifiers trained on imbalanced datasets will optimize accuracy by labeling everything as non-fraud, completely missing active fraud patterns. This project builds a balanced classifier to maximize recall on minority fraud classes.

## Technologies Used
- Python 3.10+
- Pandas & NumPy
- Scikit-learn (RandomForestClassifier with class balancing weights, Train-test splits, Confusion Matrix, Precision, Recall, F1 metrics)

## Architecture & Workflow
1. **Imbalanced Dataset Creation**: Seed a dataset containing 1000 samples, with exactly 2% (20 samples) set to Fraud class (1).
2. **Feature Engineering**: Generate numeric features for Transaction Amount and Distance from Home.
3. **Training**: Fit a RandomForestClassifier. Use class balance weights (`class_weight='balanced'`) to adjust penalty calculations on the minority class.
4. **Evaluation**: Predict on test data. Measure accuracy, precision, recall, F1, and visualize the Confusion Matrix.

## How to Run
Run the fraud detection classifier script from the repository root:
```bash
python 17_AI_ML_Projects/Intermediate_Projects/Fraud_Detection/detect.py
```

## Results & Future Improvements
- **Results**: Captures over 85% of fraud cases (Recall) while maintaining high precision.
- **Future Improvements**:
  - Implement advanced sampling techniques like SMOTE (Synthetic Minority Over-sampling Technique) using `imbalanced-learn`.
  - Train anomaly detection models (Isolation Forest or One-Class SVM) to detect fraud without needing labeled historical fraud cases.
