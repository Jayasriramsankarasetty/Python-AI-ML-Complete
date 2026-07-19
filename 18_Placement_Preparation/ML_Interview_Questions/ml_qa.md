# Machine Learning Interview Questions & Answers (Top 15)

This document contains 15 key Machine Learning interview questions frequently asked during technical placement screenings.

---

### Q1: Explain the Bias-Variance Tradeoff.
* **Answer**: 
  * **Bias**: Error introduced by approximating complex real-world relationships with simpler models (leads to **underfitting**).
  * **Variance**: Error introduced by a model learning random noise in the training dataset too closely (leads to **overfitting**).
  * **Tradeoff**: As model complexity increases, bias decreases but variance increases. The goal of machine learning is to find the optimal complexity sweet spot that minimizes total prediction error.

---

### Q2: What is regularization and explain the difference between L1 and L2 regularization?
* **Answer**: Regularization adds a penalty term to the model's loss function to discourage learning overly complex coefficients, preventing overfitting:
  * **L1 Regularization (Lasso)**: Adds a penalty proportional to the absolute sum of coefficients: `λ * Σ|w_i|`. It forces less important feature weights to exactly 0.0, performing automatic **feature selection**.
  * **L2 Regularization (Ridge)**: Adds a penalty proportional to the squared sum of coefficients: `λ * Σ(w_i)²`. It shrinks feature weights close to 0.0, but never exactly to zero, keeping all features active.

---

### Q3: What is the difference between Bagging and Boosting?
* **Answer**: Both are ensemble learning techniques, but their sequential build logics differ:
  * **Bagging (Bootstrap Aggregating)**: Trains multiple models (like decision trees) in parallel on different bootstrapped subsets of the training data. The final prediction is a simple average/vote. (e.g. **Random Forest**). Reduces **variance**.
  * **Boosting**: Trains models sequentially. Each new model focuses on correcting the errors (residuals) made by the previous models. (e.g. **XGBoost, Gradient Boosting**). Reduces **bias**.

---

### Q4: Explain the difference between Precision, Recall, and F1-Score.
* **Answer**:
  * **Precision**: Out of all predicted positive cases, how many were actually positive? Formula: `TP / (TP + FP)`.
  * **Recall** (Sensitivity): Out of all actual positive cases, how many did the model capture? Formula: `TP / (TP + FN)`.
  * **F1-Score**: The harmonic mean of Precision and Recall. Useful for evaluating models trained on imbalanced datasets: `2 * (Precision * Recall) / (Precision + Recall)`.

---

### Q5: How does the SVM Kernel Trick work?
* **Answer**: Support Vector Machines (SVMs) find a hyperplane that separates classes. If classes are non-linearly separable in the current feature space, SVMs use a mathematical **kernel function** to compute the dot products of data points in a virtual, higher-dimensional space where they become linearly separable, without physically transforming the coordinates. This avoids high computational complexity.

---

### Q6: What is Gradient Descent and explain the difference between Batch, Stochastic, and Mini-Batch variants?
* **Answer**: Gradient Descent is an optimization algorithm that iteratively adjusts model weights to minimize the cost function by taking steps in the direction of the steepest negative gradient.
  * **Batch**: Computes gradients on the *entire* dataset. Slow for large tables but stable.
  * **Stochastic (SGD)**: Computes gradients and updates weights using exactly *one* random sample per step. Fast but noisy.
  * **Mini-Batch**: Computes gradients on small slices (e.g. size 32, 64, 128). Combines the speed of SGD with the stability of Batch.

---

### Q7: Explain Cross-Validation (K-Fold).
* **Answer**: K-Fold cross-validation splits the training dataset into K equal-sized folds. The model is trained K times, each time using K-1 folds for training and the remaining 1 fold as a validation split. The final performance score is the average score across all K runs. This ensures the model's evaluation metrics are robust and not biased by a single random split.

---

### Q8: What is Overfitting and how do you prevent it?
* **Answer**: Overfitting occurs when a model performs exceptionally well on training data but poorly on unseen test data.
* **Prevention Techniques**:
  1. Add more training data.
  2. Implement regularization (L1/L2 penalties).
  3. Reduce model complexity (e.g. prune decision trees, use fewer layers/neurons).
  4. Use ensemble methods (e.g. Random Forest).
  5. Apply Dropout (in neural networks) or Early Stopping.

---

### Q9: What is the curse of dimensionality?
* **Answer**: As the number of features (dimensions) increases, the volume of the space grows exponentially, causing the data points to become extremely sparse in high-dimensional space. This sparsity makes distance-based algorithms (like KNN and K-Means) ineffective, as all data points appear equidistant from each other.

---

### Q10: Explain the difference between Parametric and Non-Parametric models.
* **Answer**:
  * **Parametric**: Assumes a specific functional form/shape for the data relationship and has a fixed number of parameters (e.g., Linear Regression, Logistic Regression). Fast to train but less flexible.
  * **Non-Parametric**: Makes no assumptions about the underlying data distribution; the number of parameters grows with the size of the training data (e.g., Decision Trees, KNN, SVM). Highly flexible but computationally intensive.

---

### Q11: Explain the difference between K-Means and KNN.
* **Answer**:
  * **K-Means**: An **unsupervised** clustering algorithm that groups unlabeled data points into K clusters based on Euclidean distance centroids.
  * **KNN (K-Nearest Neighbors)**: A **supervised** classification/regression algorithm that predicts a new data point's label based on the majority label of its K nearest labeled neighbors.

---

### Q12: What is ROC-AUC?
* **Answer**:
  * **ROC (Receiver Operating Characteristic) Curve**: Plots the True Positive Rate (Recall) against the False Positive Rate (1 - Specificity) across different probability classification thresholds.
  * **AUC (Area Under the Curve)**: Measures the overall classification performance across all thresholds. A score of 1.0 represents a perfect classifier; 0.5 represents a model making random guesses.

---

### Q13: What is the difference between covariance and correlation?
* **Answer**:
  * **Covariance**: Measures the direction (positive or negative) of the linear relationship between two variables. It is scale-dependent (ranges from -inf to +inf).
  * **Correlation**: Measures both the direction and strength of the linear relationship. It is normalized by standard deviations, making it scale-independent (ranges strictly from -1.0 to +1.0).

---

### Q14: Explain the role of the Sigmoid function in Logistic Regression.
* **Answer**: Logistic Regression outputs linear weights calculations: `z = w • x + b`. To convert this continuous real number into a probability score between 0.0 and 1.0, the output is mapped through the Sigmoid function: `S(z) = 1 / (1 + e^-z)`.

---

### Q15: What is the difference between generative and discriminative models?
* **Answer**:
  * **Generative Models**: Learn the joint probability distribution `P(X, Y)` to model how the data is generated, allowing them to generate new data points (e.g. Naive Bayes, GANs).
  * **Discriminative Models**: Learn the conditional probability distribution `P(Y | X)` to model the decision boundary between classes, mapping inputs to labels directly (e.g. Logistic Regression, SVMs).
