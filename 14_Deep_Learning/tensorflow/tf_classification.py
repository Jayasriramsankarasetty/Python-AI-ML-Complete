"""
Topic:
Deep Learning with TensorFlow - Sequential MLP Classifier

Importance:
TensorFlow (developed by Google) is one of the most widely used enterprise-level deep learning frameworks.
Knowing how to build sequential networks, compile optimizers/loss functions, and train models
using the Keras API is a core skill for deep learning developers.

This file covers:
- Concept: Sequential Model building
- Defining Dense layers and activation functions (ReLU, Sigmoid)
- Compiling models (Adam Optimizer, Binary Cross-Entropy loss)
- Training epochs and testing evaluations
- Automatic fallback to scikit-learn's MLPClassifier if TensorFlow is not installed
"""

# ==========================================
# 1. Concept Explanation & When to use
# ==========================================
# TensorFlow Keras structures neural network layers sequentially using Sequential:
#   - Dense Layer: Represents a fully connected neural network layer.
#   - Activation: ReLU is standard for hidden layers (prevents vanishing gradients);
#     Sigmoid is standard for binary output (maps outputs to 0-1 probability).
#   - Compilation requires:
#     1. Optimizer (e.g. Adam): Adjusts weights dynamically based on learning rate updates.
#     2. Loss Function (e.g. Binary Crossentropy): Measures error differences.
#     3. Metrics (e.g. Accuracy): Evaluates classification success rates.
#
# When to use:
# - Building standard neural network layers (Dense, Convolutional, Recurrent).
# - Developing deep neural networks for large-scale structured or unstructured datasets.
# - Production deployments requiring optimized Tensor graph acceleration (GPUs/TPUs).

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Try importing tensorflow; fallback if not present
use_tf = True
try:
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    print("Using TensorFlow / Keras framework.")
except ImportError:
    from sklearn.neural_network import MLPClassifier
    use_tf = False
    print("TensorFlow library not found. Falling back to scikit-learn MLPClassifier.")

# ==========================================
# 2. Setup Dummy Classification Dataset
# ==========================================
# Binary Classification: predicting student exam pass/fail (1 or 0)
# Features: Hours Studied, Attendance Rate (%)
np.random.seed(42)
n_samples = 150

hours = np.random.uniform(1.0, 10.0, n_samples)
attendance = np.random.uniform(50.0, 100.0, n_samples)

# Boundary: passing if hours * 10 + attendance > 110
y = []
for h, a in zip(hours, attendance):
    val = h * 10 + a
    prob = 0.90 if val > 110 else 0.10
    y.append(np.random.choice([0, 1], p=[1 - prob, prob]))

X = np.column_stack((hours, attendance))
y = np.array(y)

# Preprocessing splits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale inputs (Crucial for deep neural networks learning stability)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# 3. Model Training & Evaluation
# ==========================================
if use_tf:
    # Build Keras Sequential model
    model = Sequential([
        # Input layer feeding into a 4-node hidden layer with ReLU activation
        Dense(units=4, activation="relu", input_shape=(X_train_scaled.shape[1],)),
        # Output layer with 1 node using Sigmoid activation (for binary probability)
        Dense(units=1, activation="sigmoid")
    ])
    
    # Compile model with Adam optimizer and binary crossentropy loss
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    
    print("\nTraining Keras Model...")
    # Train the model for 30 epochs
    history = model.fit(
        X_train_scaled, y_train,
        epochs=30,
        batch_size=8,
        validation_split=0.1,
        verbose=0  # quiet logging
    )
    
    # Evaluate model
    loss, accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
    print("=======================================")
    print("TensorFlow Model Evaluation:")
    print("=======================================")
    print(f"Final Test Loss:     {loss:.4f}")
    print(f"Final Test Accuracy: {accuracy:.4f}")
    print("=======================================")

else:
    # Fallback execution using scikit-learn MLPClassifier
    model = MLPClassifier(
        hidden_layer_sizes=(4,),
        activation="relu",
        solver="adam",
        max_iter=500,
        random_state=42
    )
    model.fit(X_train_scaled, y_train)
    accuracy = model.score(X_test_scaled, y_test)
    print("=======================================")
    print("MLPClassifier Fallback Evaluation:")
    print("=======================================")
    print(f"Final Test Accuracy: {accuracy:.4f}")
    print("=======================================")

"""
Key Takeaways:
- Sequential models compile stack layers linearly from inputs to outputs.
- Adam optimizer adjusts learning rates adaptively; Binary Cross-Entropy is standard for binary targets.
- Input feature scaling is highly critical to prevent weight gradients from diverging.

Interview Relevance:
- Explain the role of Dense layers in Keras. (A Dense layer is a fully connected neural network layer where every neuron receives inputs from all neurons of the previous layer, computing linear combinations and activations).
- What does the 'Adam' optimizer do? (Adaptive Moment Estimation (Adam) combines RMSProp and Momentum gradient steps, adjusting learning rates dynamically for each parameter based on first and second moments).
- Why is validation_split useful during training? (It sets aside a portion of the training data to monitor loss after each epoch, helping detect overfitting early before deploying to test splits).

AI/ML Relevance:
- Framework Choice: TensorFlow excels in building enterprise-scale graph architectures, supporting highly accelerated operations across servers.
"""
