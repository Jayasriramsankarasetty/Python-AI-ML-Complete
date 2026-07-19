"""
Topic:
Constructors in Python

Importance:
A constructor is a special method called automatically when an object is instantiated.
It initializes the instance attributes of the object.
In AI/ML, constructors are where we configure network architectures, load initial weights,
or set training parameters.

This file covers:
- The __init__() method (Constructor)
- Parameterized vs Default constructors
- Binding values to instance variables
- Practical ML application: Constructing a model trainer parameter initializer
"""

# ==========================================
# 1. Understanding the __init__() Method
# ==========================================
# In Python, constructors are defined using the special magic method name: __init__.
# Double underscores (dunder) denote special built-in methods.

class ModelHyperparameters:
    # Parameterized Constructor with default values
    def __init__(self, learning_rate=0.01, batch_size=32, epochs=10):
        print("Constructor triggered automatically!")
        # Bind inputs to instance attributes
        self.lr = learning_rate
        self.batch_size = batch_size
        self.epochs = epochs
        
    def display_parameters(self):
        print(f"Configurations -> LR: {self.lr} | Batch Size: {self.batch_size} | Epochs: {self.epochs}")

print("--- Instantiating with Default Constructor Values ---")
# Calls __init__ with default arguments
config_default = ModelHyperparameters()
config_default.display_parameters()

print("\n--- Instantiating with Custom Parameterized Values ---")
# Calls __init__ with explicit arguments
config_custom = ModelHyperparameters(learning_rate=0.0005, batch_size=64, epochs=250)
config_custom.display_parameters()

# ==========================================
# 2. Re-assigning Instantiated Attributes
# ==========================================
# Once an object is created, we can modify its attributes directly or fetch them.

print("\n--- Accessing & Modifying Attributes ---")
print(f"Old learning rate of Custom Model: {config_custom.lr}")
# Reassign
config_custom.lr = 0.001
print(f"Updated learning rate of Custom Model: {config_custom.lr}")

# ==========================================
# 3. Hands-on ML Use-Case: ML Model class
# ==========================================
# We instantiate models by passing configurations to the constructor.
print("\n--- Practical ML Model Class ---")

class SimpleRegressor:
    def __init__(self, algorithm_name, penalty="l2"):
        self.algo = algorithm_name
        self.penalty = penalty
        self.weights = []  # Starts empty before fit()
        self.is_trained = False
        
    def fit(self, x, y):
        print(f"Fitting {self.algo} model on dataset of size {len(x)} with penalty={self.penalty}...")
        # Simulate simple weight fitting (taking average ratio)
        self.weights = [sum(y) / sum(x)]
        self.is_trained = True
        
    def predict(self, x_new):
        if not self.is_trained:
            print("Error: Model has not been trained yet!")
            return None
        return [val * self.weights[0] for val in x_new]

# Instantiating the Regressor
model = SimpleRegressor(algorithm_name="Ridge Regression", penalty="l2")
print("Is model trained before fit() call?", model.is_trained)

# Training inputs and targets
inputs = [1.0, 2.0, 3.0]
targets = [2.0, 4.0, 6.0]

# Fit model
model.fit(inputs, targets)
print("Model Weights (Slope):", model.weights)
print("Is model trained now?", model.is_trained)

# Predict new points
new_inputs = [4.0, 5.0]
predictions = model.predict(new_inputs)
print(f"Predictions for {new_inputs} -> {predictions}")

"""
Key Takeaways:
- The constructor `__init__` initializes instance state when an object is created.
- Double underscores (dunder) represent special python methods.
- Default parameters can be added to constructors to simplify instance creation.
- Instance variables initialized in the constructor are accessed via `self.variable_name`.

Interview Relevance:
- What is the purpose of the `__init__` method in Python? (It is the initializer/constructor method that sets up initial attributes on instantiation).
- Does Python support multiple constructor overloading? (No, you can only define one `__init__` method. However, you can achieve constructor flexibility using default arguments, variable length arguments `*args`/`**kwargs`, or class methods as alternative constructors).
- What is a dunder method? (Double underscore methods like `__init__`, `__str__`, which are pre-defined hook methods in Python's class mechanics).

AI/ML Relevance:
- Model initializations: PyTorch architectures load network layer shapes (`nn.Linear`, `nn.Conv2d`) inside their constructor block, storing layer structures as instance attributes.
- Hyperparameter tracking: Constructors parse input arguments representing rates, regularization values, optimizer preferences, and random seeds to persist them across training epochs.
"""
