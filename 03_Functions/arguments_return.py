"""
Topic:
Function Arguments and Return Values

Importance:
ML algorithms require highly flexible APIs. Passing hyperparameters dynamically via
variable-length configurations (*args and **kwargs) and returning metrics is a core pattern in libraries like scikit-learn.

This file covers:
- Positional and Keyword arguments
- Default parameters
- Arbitrary positional arguments (*args)
- Arbitrary keyword arguments (**kwargs)
- Returning multiple values from a function
- Practical ML application: Building a model configuration runner
"""

# ==========================================
# 1. Positional, Keyword & Default Arguments
# ==========================================
# Positional: order of values determines the variable assignment.
# Keyword: passing values using argument names.
# Default parameters: assigned values if none are supplied at call.

def print_model_summary(model_name, epochs=50, optimizer="Adam"):
    print(f"Model: {model_name} | Epochs: {epochs} | Optimizer: {optimizer}")

print("--- Default & Keyword Arguments ---")
# Call using positional defaults
print_model_summary("LinearRegression")

# Call using custom positional arguments
print_model_summary("CNN", 100, "SGD")

# Call using keyword arguments (order doesn't matter)
print_model_summary(optimizer="RMSprop", model_name="LSTM", epochs=80)

# ==========================================
# 2. Variable-length Arguments (*args and **kwargs)
# ==========================================
# *args: packs positional arguments into a tuple.
# **kwargs: packs keyword arguments into a dictionary.

# E.g. function to compute average of multiple numeric scores
def average_metrics(*accuracies):
    print(f"\nReceived metrics (Tuple representation): {accuracies}")
    if not accuracies:
        return 0.0
    total = sum(accuracies)
    return total / len(accuracies)

print("\n--- *args Example ---")
avg = average_metrics(0.85, 0.92, 0.78, 0.95)
print(f"Average Accuracy Score: {avg:.4f}")

# E.g. function to initialize model with dictionary configuration
def initialize_model(model_type, **hyperparameters):
    print(f"\nInitializing model '{model_type}'...")
    print(f"Configured parameters (Dict representation): {hyperparameters}")
    
    # Safely get configuration parameters with defaults
    lr = hyperparameters.get("lr", 0.001)
    batch_size = hyperparameters.get("batch_size", 32)
    
    print(f"Executing: learning_rate={lr}, batch_size={batch_size}")

print("\n--- **kwargs Example ---")
initialize_model("XGBoost", lr=0.05, max_depth=6, batch_size=64, subsample=0.8)

# ==========================================
# 3. Returning Multiple Values
# ==========================================
# Python functions return a tuple when multiple values are separated by commas.
# They are easily unpacked in a single line.

def evaluate_predictions(y_true, y_pred):
    """
    Simulates calculating classification evaluation metrics.
    """
    # Dummy calculation
    accuracy = 0.91
    precision = 0.89
    recall = 0.93
    
    # Return multiple metrics
    return accuracy, precision, recall

print("\n--- Returning Multiple Values ---")
# Unpacking the returned tuple
acc, prec, rec = evaluate_predictions([1, 0, 1], [1, 0, 0])
print(f"Evaluation Acc: {acc:.2f} | Precision: {prec:.2f} | Recall: {rec:.2f}")

"""
Key Takeaways:
- Non-default parameters must always be defined BEFORE default parameters.
- *args is a tuple of additional positional parameters; **kwargs is a dictionary of extra keyword arguments.
- Multiple values are returned as a tuple, which can be unpacked immediately.

Interview Relevance:
- What is the difference between *args and **kwargs? (*args packs variable positional arguments into a tuple; **kwargs packs variable keyword arguments into a dict).
- Can we define standard positional arguments after *args? (No, standard parameters after *args must be passed as keyword-only arguments).
- What does a function return if there is no explicit return statement? (It returns None).

AI/ML Relevance:
- PyTorch / TensorFlow modules: When building custom neural networks, `super().__init__(*args, **kwargs)` is used to pass arguments up to the parent model layer class.
- Scikit-Learn APIs: Fit functions take varying arguments, often utilizing default parameters to configure complex models with standard baseline values.
"""
