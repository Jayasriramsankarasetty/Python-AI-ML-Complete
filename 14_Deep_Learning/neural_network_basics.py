"""
Topic:
Deep Learning - Neural Network Basics from Scratch (NumPy)

Importance:
Understanding backpropagation and gradient descent updates from scratch is a
highly high-frequency requirement for deep learning interview loops. It proves
you understand the mathematical optimization steps underneath framework abstractions.

This file covers:
- Concept Explanation & Neural network architecture
- Sigmoid activation function and its derivative
- Forward propagation (linear projection + activation)
- Mean Squared Error (MSE) loss computation
- Backpropagation (computing gradients using chain rule)
- Gradient descent updates
- Training loop on XOR logic dataset
- Prediction testing
"""

# ==========================================
# 1. Concept Explanation
# ==========================================
# A Neural Network consists of layers of nodes (neurons):
#   - Input Layer: Receives input features.
#   - Hidden Layer: Computes intermediate representations.
#   - Output Layer: Computes final class or value predictions.
# Each connection between nodes carries a Weight (w), and each node has a Bias (b).
# Math operations:
#   - Linear Combination: z = X * W + b
#   - Activation Function: a = f(z)  (Non-linearity, like Sigmoid or ReLU)
# Forward Propagation: Projects inputs sequentially layer-by-layer to get predictions.
# Loss Function: Measures discrepancy between predictions and target labels.
# Backpropagation: Computes the partial derivatives of the loss with respect to weights
#   and biases using the mathematical Chain Rule of calculus.
# Optimization: Updates weights and biases opposite to the gradient: W = W - learning_rate * dW.

import numpy as np

# ==========================================
# 2. Activation Function & Derivative
# ==========================================
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid_derivative(sigmoid_output):
    # If a = sigmoid(z), then da/dz = a * (1 - a)
    return sigmoid_output * (1.0 - sigmoid_output)

# ==========================================
# 3. Simple Neural Network Implementation
# ==========================================
class SimpleNeuralNetwork:
    def __init__(self, input_dim, hidden_dim, output_dim, lr=0.1):
        self.lr = lr
        
        # Initialize weights randomly, biases to zero
        # W1: input_dim -> hidden_dim
        self.W1 = np.random.normal(0, 0.1, (input_dim, hidden_dim))
        self.b1 = np.zeros((1, hidden_dim))
        
        # W2: hidden_dim -> output_dim
        self.W2 = np.random.normal(0, 0.1, (hidden_dim, output_dim))
        self.b2 = np.zeros((1, output_dim))
        
    def forward(self, X):
        # Step A: Input to Hidden
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = sigmoid(self.z1)
        
        # Step B: Hidden to Output
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2
        
    def backward(self, X, y, output):
        # Calculate gradients using the Chain Rule
        # Loss = 0.5 * (y - output)^2
        # dLoss/dOutput = -(y - output)
        error_output = output - y
        
        # Delta at output layer: dL/dz2 = (dLoss/da2) * (da2/dz2)
        delta_output = error_output * sigmoid_derivative(output)
        
        # Gradients for hidden-to-output connection
        dW2 = np.dot(self.a1.T, delta_output)
        db2 = np.sum(delta_output, axis=0, keepdims=True)
        
        # Delta at hidden layer: dL/dz1 = (dL/dz2 * W2^T) * (da1/dz1)
        error_hidden = np.dot(delta_output, self.W2.T)
        delta_hidden = error_hidden * sigmoid_derivative(self.a1)
        
        # Gradients for input-to-hidden connection
        dW1 = np.dot(X.T, delta_hidden)
        db1 = np.sum(delta_hidden, axis=0, keepdims=True)
        
        # Update weights and biases using Gradient Descent
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2

# ==========================================
# 4. Training Process Demo (XOR Gate problem)
# ==========================================
if __name__ == "__main__":
    # XOR dataset (X1, X2 inputs, y binary target)
    # XOR cannot be separated by a single linear line (requires a hidden layer)
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    y = np.array([
        [0],
        [1],
        [1],
        [0]
    ])
    
    # Initialize NN: 2 inputs, 4 hidden nodes, 1 output node
    nn = SimpleNeuralNetwork(input_dim=2, hidden_dim=4, output_dim=1, lr=0.5)
    
    print("=======================================")
    print("Training 2-Layer Neural Network from Scratch (XOR)")
    print("=======================================")
    
    epochs = 10000
    for epoch in range(epochs):
        output = nn.forward(X)
        nn.backward(X, y, output)
        
        # Print loss occasionally
        if epoch % 2000 == 0:
            loss = np.mean(0.5 * (y - output) ** 2)
            print(f"Epoch {epoch:5d} | Mean Squared Error Loss: {loss:.6f}")
            
    # ==========================================
    # 5. Prediction Example
    # ==========================================
    print("\nTraining Complete! Prediction Results:")
    predictions = nn.forward(X)
    for x_in, pred, target in zip(X, predictions, y):
        print(f"Input: {x_in} | Predicted: {pred[0]:.4f} (Target: {target[0]})")
    print("=======================================")

"""
Key Takeaways:
- Forward propagation flows data inputs layer-by-layer to generate class probabilities.
- Backpropagation uses the Chain Rule of calculus to compute gradient updates for all weights.
- Multi-layer perceptrons (MLPs) can resolve non-linear separation tasks (like XOR gates) which single-layer perceptrons cannot.

Interview Relevance:
- Explain Backpropagation in simple terms. (It is the process of calculating the gradients of the loss function with respect to the weights of the neural network, starting from the output layer and propagating backward using the calculus chain rule).
- Why do we need Activation Functions? (To introduce non-linearity into the network. Without activation functions, any number of stacked layers would contract mathematically into a single linear projection, failing to model complex non-linear shapes).
- Why is Sigmoid rarely used in hidden layers of modern deep networks? (It causes the Vanishing Gradient Problem. For large input values, the derivative of sigmoid approaches 0, causing weight gradients to become tiny and stopping model training updates).

AI/ML Relevance:
- Optimization foundations: Standard neural network layers in PyTorch (`nn.Linear`) and TensorFlow Keras (`Dense`) perform these linear dot products and backpropagation checks behind their module wrappers.
"""
