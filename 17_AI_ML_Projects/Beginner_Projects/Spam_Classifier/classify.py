"""
Topic:
Beginner Project - SMS Spam Classifier using Multinomial Naive Bayes

Importance:
Naive Bayes is highly effective for text classification. This project
demonstrates converting unstructured text into structured numeric inputs.

This file covers:
- Loading text messages (Ham vs Spam labels)
- Transforming text using TfidfVectorizer
- Training a MultinomialNB classifier
- Evaluating classification reports (Accuracy, Precision, Recall, F1)
"""

# ==========================================
# 1. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ==========================================
# 2. Load/Create Dataset
# ==========================================
# Mock SMS corpus
corpus = [
    ("Congratulations! You won a free iPhone. Claim now!", 1),  # Spam
    ("URGENT: Your bank account is locked. Log in here to unlock.", 1),  # Spam
    ("Free trial membership available. Click here.", 1),  # Spam
    ("Hi Mom, I will be home by 6 PM tonight.", 0),  # Ham
    ("Hey buddy, are we still meeting for lunch tomorrow?", 0),  # Ham
    ("Please review the attached project proposal details.", 0),  # Ham
    ("Get cash loans in minutes. No credit check required.", 1),  # Spam
    ("Can you send me the link to that website?", 0),  # Ham
    ("Claim your $500 gift card today! Winner code 4492.", 1),  # Spam
    ("Let's go watch a movie this weekend.", 0)  # Ham
]

df = pd.DataFrame(corpus, columns=["message", "label"])
X = df["message"]
y = df["label"]

# ==========================================
# 3. Preprocessing
# ==========================================
# Use TF-IDF to tokenize and represent text messages numerically
vectorizer = TfidfVectorizer()
X_vectors = vectorizer.fit_transform(X)

# Split vectors (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_vectors, y, test_size=0.2, random_state=42)

# ==========================================
# 4. Train Model
# ==========================================
model = MultinomialNB()
model.fit(X_train, y_train)

# ==========================================
# 5. Predict & Evaluate
# ==========================================
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("=======================================")
print("SMS Spam Classifier Project Results:")
print("=======================================")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")
print("=======================================")

"""
Key Takeaways:
- TF-IDF transforms string texts into weighted vocabulary matrices.
- Multinomial Naive Bayes uses Bayes' Theorem probability math to classify text features.
- Text pipelines must process raw files into tokenized coordinates before model fits.

Interview Relevance:
- Why is Naive Bayes popular for text classification? (It is computationally fast, performs well with high-dimensional sparse text vectors, and handles class probabilities natively).
- What does the 'Naive' represent? (The conditional independence assumption: it assumes that the presence of a particular word in a class is completely unrelated to the presence of any other word).

AI/ML Relevance:
- Text processing: Establishes base NLP parsing logic templates for document routing.
"""
