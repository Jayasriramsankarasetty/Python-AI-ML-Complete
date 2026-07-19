# Multiple Choice Questions (MCQs) - Placement Prep

This document contains 20 high-frequency multiple-choice questions spanning Python programming, SQL, Machine Learning, and Generative AI/Deep Learning.

---

## Python MCQs (1-5)

### Q1: What is the output of the following Python code?
```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```
- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]`
- C) `[1, 2, 3, [4]]`
- D) AttributeError
* **Answer**: B
* **Explanation**: In Python, variables pointing to mutable objects (like lists) store references to the same underlying object memory. Thus, modifying `y` modifies `x` as well.

### Q2: Which keyword is used to retrieve values from a generator function?
- A) `return`
- B) `yield`
- C) `raise`
- D) `send`
* **Answer**: B
* **Explanation**: The `yield` keyword pauses function execution and returns a value to the caller, retaining local state so the function can resume from the same line on the next iteration.

### Q3: What is the correct operator to perform floor division?
- A) `/`
- B) `%`
- C) `//`
- D) `**`
* **Answer**: C
* **Explanation**: `//` performs integer/floor division, throwing away any fractional remainder (e.g. `5 // 2` is `2`).

### Q4: How is a circular reference resolved in Python's garbage collection?
- A) By reference counting alone.
- B) By the generational garbage collector traversing reference cycles.
- C) By using local namespaces.
- D) Python cannot resolve circular references, resulting in memory leaks.
* **Answer**: B
* **Explanation**: Reference counting cannot detect self-referencing loops (ref counts never drop to 0). Python uses a cyclic garbage collector to scan object graphs periodically.

### Q5: What is the output of `type(lambda x: x)`?
- A) `class`
- B) `function`
- C) `lambda`
- D) `type`
* **Answer**: B
* **Explanation**: Lambda expressions create anonymous functions, which are instances of the standard `<class 'function'>`.

---

## SQL MCQs (6-10)

### Q6: Which HTTP equivalent operation does a SQL `UPDATE` represent?
- A) GET
- B) POST
- C) PUT/PATCH
- D) DELETE
* **Answer**: C
* **Explanation**: PUT/PATCH requests are used to update existing resources on a server, similar to database `UPDATE` modifications.

### Q7: What does the `HAVING` clause do?
- A) Filters rows before grouping aggregates are calculated.
- B) Filters aggregated grouped rows after `GROUP BY` is executed.
- C) Sorts query outputs alphabetically.
- D) Acts as a join constraint key.
* **Answer**: B
* **Explanation**: `HAVING` is specifically designed to filter summary/grouped columns (e.g. `HAVING COUNT(id) > 5`).

### Q8: Which join returns all records from the left table and matching records from the right table?
- A) INNER JOIN
- B) LEFT OUTER JOIN
- C) RIGHT OUTER JOIN
- D) FULL JOIN
* **Answer**: B
* **Explanation**: `LEFT JOIN` (or LEFT OUTER JOIN) preserves all rows from the left table, filling right table columns with NULL where no match exists.

### Q9: Which database property ensures that a transaction is processed as an "all or nothing" unit?
- A) Atomicity
- B) Consistency
- C) Isolation
- D) Durability
* **Answer**: A
* **Explanation**: **Atomicity** ensures that if any command inside a transaction block fails, the entire transaction is aborted and rolled back.

### Q10: What is the primary drawback of adding index trees to columns?
- A) SELECT queries become slower.
- B) Database storage size increases and INSERT/UPDATE writes become slower.
- C) Referential integrity is disabled.
- D) Aggregates cannot be calculated on indexed columns.
* **Answer**: B
* **Explanation**: Indexes occupy physical storage disk space, and since index binary trees must be updated on every write, writes become slower.

---

## Machine Learning MCQs (11-15)

### Q11: What is the main symptom of an overfitted model?
- A) Low training accuracy, low validation accuracy.
- B) High training accuracy, low validation accuracy.
- C) Low training accuracy, high validation accuracy.
- D) High training accuracy, high validation accuracy.
* **Answer**: B
* **Explanation**: Overfitting occurs when the model memorizes the training data (including noise), failing to generalize to unseen test/validation data.

### Q12: Which regularization technique can force feature coefficients to exactly 0.0?
- A) L1 Regularization (Lasso)
- B) L2 Regularization (Ridge)
- C) ElasticNet
- D) Dropout
* **Answer**: A
* **Explanation**: Lasso uses absolute weight values which create sharp geometric corners in cost functions, forcing coefficients to exactly 0.0 for sparse feature selection.

### Q13: What does the 'B' in bagging stand for?
- A) Boosting
- B) Binary
- C) Bootstrap
- D) Boundary
* **Answer**: C
* **Explanation**: Bagging stands for **Bootstrap Aggregating**, which trains models on randomized, bootstrapped data subsets.

### Q14: Which metric is calculated as `TP / (TP + FP)`?
- A) Recall
- B) Precision
- C) F1-Score
- D) Accuracy
* **Answer**: B
* **Explanation**: **Precision** measures the ratio of true positive predictions out of all predicted positive labels.

### Q15: In K-Means clustering, how are cluster assignments determined?
- A) By checking labels using KNN.
- B) By minimizing Euclidean distance to cluster centroids.
- C) By maximizing entropy split values.
- D) By computing logistic sigmoids.
* **Answer**: B
* **Explanation**: K-Means iteratively assigns data points to their nearest centroid based on spatial distance calculations.

---

## AI & Deep Learning MCQs (16-20)

### Q16: What is the core formula of self-attention?
- A) `S(W * x + b)`
- B) `softmax(Q • K^T / sqrt(d_k)) * V`
- C) `w_t - learning_rate * grad`
- D) `1 / (1 + e^-z)`
* **Answer**: B
* **Explanation**: The self-attention matrix query dot products Keys, scales, applies softmax, and multiplies by the Value vector.

### Q17: Which activation function outputs values between 0.0 and 1.0?
- A) ReLU
- B) LeakyReLU
- C) Sigmoid
- D) Tanh
* **Answer**: C
* **Explanation**: The Sigmoid function `1 / (1 + e^-z)` compresses any real number input into a probability scale between 0.0 and 1.0.

### Q18: What is the main advantage of RAG over fine-tuning for question answering?
- A) RAG updates the weights of the LLM directly.
- B) RAG does not require training data or gradient computation and accesses live document bases directly.
- C) RAG is computationally slower.
- D) RAG eliminates the need for prompt formatting templates.
* **Answer**: B
* **Explanation**: RAG performs contextual lookup at query time, meaning it does not alter weights and can access updated files instantly.

### Q19: Which problem is residual skip connections in ResNet designed to resolve?
- A) Overfitting
- B) Vanishing Gradients in deep networks
- C) Input validation errors
- D) High learning rates
* **Answer**: B
* **Explanation**: Residual skip connections allow gradients to flow backward directly through addition layers, bypassing weight multiplications to prevent vanishing gradients.

### Q20: What is the primary role of the forget gate in an LSTM cell?
- A) To reset the learning rate.
- B) To determine which cell state values are discarded from memory.
- C) To map inputs through a ReLU activation.
- D) To output final predictions.
* **Answer**: B
* **Explanation**: The forget gate outputs values between 0.0 (discard entirely) and 1.0 (retain completely) to regulate what cell state memory values are cleared.
