# Beginner Project 2: SMS Spam Classifier

## Project Objective
Develop a text classifier to label incoming emails/SMS messages as either SPAM (unsolicited commercial) or HAM (legitimate personal/business communication).

## Problem Statement
Spam messages waste time and network resources. This project builds a text processing pipeline to filter out spam automatically using statistical occurrences.

## Technologies Used
- Python 3.10+
- Pandas & NumPy
- Scikit-learn (TfidfVectorizer, MultinomialNB Naive Bayes model, accuracy metrics)

## Architecture & Workflow
1. **Corpus Loading**: Load an email database containing labeled strings.
2. **Text Vectorization**: Convert raw words into high-dimensional TF-IDF vectors.
3. **Training**: Fit a Multinomial Naive Bayes classifier.
4. **Evaluation**: Predict classes on test phrases and calculate Accuracy, Precision, Recall, and F1 Score metrics.

## How to Run
Run the spam classifier script from the repository root:
```bash
python 17_AI_ML_Projects/Beginner_Projects/Spam_Classifier/classify.py
```

## Results & Future Improvements
- **Results**: Achieves ~90% text classification accuracy.
- **Future Improvements**:
  - Implement text cleaning steps (lowercasing, punctuation stripping, stopword filtering).
  - Compare Naive Bayes performance against Logistic Regression or SVM classifiers.
