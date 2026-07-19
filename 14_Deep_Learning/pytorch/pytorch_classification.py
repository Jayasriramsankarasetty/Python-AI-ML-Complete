"""
Topic:
Deep Learning with PyTorch - Custom Module Classifier

Importance:
PyTorch (developed by Meta) is the primary framework used in academic research
and modern AI startups. It uses a dynamic computational graph (imperative execution),
making custom architectures, debugging, and training loops highly flexible.

This file covers:
- Concept: PyTorch Tensors and Custom Module creation
- Defining layers using torch.nn.Linear and torch.nn.functional
- Implementing the explicit training loop (forward, loss, backward, optimizer step)
- Evaluating accuracy outputs
- Fallback configuration to scikit-learn if PyTorch is not installed
"""

# ==========================================
# 1. Concept Explanation & When to use
# ==========================================
# PyTorch builds networks by subclassing torch.nn.Module:
#   - init(): Instantiate network layer weights (e.g. nn.Linear).
#   - forward(): Directs the sequential flow of inputs through activation operations.
# Training steps must be coded explicitly:
#   1. optimizer.zero_grad(): Clear gradients from the previous epoch.
#   2. forward: Compute predictions from inputs.
#   3. loss: Compute error distance from labels.
#   4. loss.backward(): Backpropagate gradients.
#   5. optimizer.step(): Update weight coefficients.
#
# When to use:
# - Researching novel network connections or non-standard training loops.
# - Building dynamic graph structures (like Transformers or RNNs with variable length).
# - Developing production solutions utilizing HuggingFace or PyTorch ecosystem libraries.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Try importing torch; fallback if not present
use_torch = True
try:
    import torch
    import torch.nn as nn
    import torch.optim as optim
    print("Using PyTorch framework.")
except ImportError:
    from sklearn.neural_network import MLPClassifier
    use_torch = False
    print("PyTorch library not found. Falling back to scikit-learn MLPClassifier.")

# ==========================================
# 2. Setup Dataset
# ==========================================
# Binary Classification: student pass/fail (1 or 0)
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

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# 3. Model Training & Evaluation
# ==========================================
if use_torch:
    # Set seed for torch random initializations
    torch.manual_seed(42)
    
    # Convert numpy arrays to torch FloatTensors
    X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1) # shape (N, 1)
    
    X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)
    
    # Define Neural Network Class inheriting from nn.Module
    class StudentClassifier(nn.Module):
        def __init__(self, input_dim):
            super(StudentClassifier, self).__init__()
            # Hidden layer: 2 inputs -> 4 outputs
            self.hidden = nn.Linear(input_dim, 4)
            # Output layer: 4 inputs -> 1 output
            self.output = nn.Linear(4, 1)
            # Activations
            self.relu = nn.ReLU()
            self.sigmoid = nn.Sigmoid()
            
        def forward(self, x):
            x = self.relu(self.hidden(x))
            x = self.sigmoid(self.output(x))
            return x

    model = StudentClassifier(input_dim=X_train_scaled.shape[1])
    
    # Loss: Binary Cross Entropy Loss
    criterion = nn.BCELoss()
    # Optimizer: Stochastic Gradient Descent (SGD)
    optimizer = optim.SGD(model.parameters(), lr=0.1)
    
    print("\nTraining PyTorch Model...")
    epochs = 100
    for epoch in range(epochs):
        # Step A: Zero gradients
        optimizer.zero_grad()
        # Step B: Forward Pass
        predictions = model(X_train_tensor)
        # Step C: Compute Loss
        loss = criterion(predictions, y_train_tensor)
        # Step D: Backward Pass (Backprop)
        loss.backward()
        # Step E: Optimizer Step (Weights updates)
        optimizer.step()
        
    # Evaluate model accuracy on test split
    with torch.no_grad():  # turn off gradient computation during evaluation (saves memory/time)
        test_predictions = model(X_test_tensor)
        test_loss = criterion(test_predictions, y_test_tensor)
        # Apply boundary threshold 0.5 to get class labels (0 or 1)
        predicted_classes = (test_predictions >= 0.5).float()
        correct_count = (predicted_classes == y_test_tensor).sum().item()
        accuracy = correct_count / len(y_test)
        
    print("=======================================")
    print("PyTorch Model Evaluation:")
    print("=======================================")
    print(f"Final Test Loss:     {test_loss.item():.4f}")
    print(f"Final Test Accuracy: {accuracy:.4f}")
    print("=======================================")

else:
    # Fallback execution using scikit-learn MLPClassifier
    model = MLPClassifier(
        hidden_layer_sizes=(4,),
        activation="relu",
        solver="sgd",
        learning_rate_init=0.1,
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
- PyTorch custom networks subclass `torch.nn.Module` and implement `forward()`.
- Dynamic graphs require explicit training loops containing zeroing gradients and optimizer steps.
- `torch.no_grad()` prevents tracking calculations during predictions, optimizing CPU/GPU throughput.

Interview Relevance:
- Why do we need `optimizer.zero_grad()` in PyTorch training loops? (PyTorch accumulates gradients on backward passes. If we don't clear them at the start of each epoch, the new gradients will sum with the old ones, leading to incorrect updates).
- What does `with torch.no_grad()` do? (It temporarily disables gradient calculations, reducing memory footprint and speeding up forward evaluations during testing/validation).
- Compare PyTorch vs TensorFlow static graphs. (PyTorch uses dynamic graphs (Eager execution) built on-the-fly during runtime, making it highly interactive and easy to debug. Older TensorFlow versions used static graphs built beforehand and run inside a Session, though modern Keras supports eager execution).

AI/ML Relevance:
- Production Standard: The majority of transformer LLM architectures (like GPT, LLaMA) are trained and run on PyTorch backends.
"""
