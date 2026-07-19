"""
Topic:
Instance, Class, and Static Methods in Python

Importance:
Understanding the different method scopes is crucial for writing clean APIs.
- Instance methods: Operate on unique object state.
- Class methods: Operate on class-level parameters or serve as factory initializers.
- Static methods: Utility functions with no access to class/object state.

This file covers:
- Instance methods (self parameter)
- Class methods (@classmethod decorator, cls parameter)
- Static methods (@staticmethod decorator)
- Practical ML application: Building a model factory utility
"""

# ==========================================
# 1. Understanding Method Types
# ==========================================

class ModelConfiguration:
    # Class Attribute
    supported_frameworks = ["PyTorch", "TensorFlow"]
    
    def __init__(self, name, lr):
        # Instance Attributes
        self.model_name = name
        self.learning_rate = lr

    # A. Instance Method: Accesses/modifies instance state using 'self'
    def print_details(self):
        print(f"Instance Method -> Model: {self.model_name} | LR: {self.learning_rate}")
        # Can access class variable too:
        # print(self.supported_frameworks)

    # B. Class Method: Accesses/modifies class-level attributes using 'cls'. Cannot access instance variables.
    # Often used as "alternative constructors" or factory initializers.
    @classmethod
    def load_from_config_string(cls, config_str):
        # Parse simple string: "CNN-0.005"
        name, lr_str = config_str.split("-")
        lr = float(lr_str)
        print(f"Class Method (Factory) -> Creating instance of {cls.__name__} for {name}")
        # Returns a new instance of the class (equivalent to ModelConfiguration(name, lr))
        return cls(name, lr)

    @classmethod
    def print_frameworks(cls):
        print(f"Class Method -> Supported frameworks of {cls.__name__}: {cls.supported_frameworks}")

    # C. Static Method: behave like simple utility functions.
    # They don't take self or cls, and cannot access class or instance state directly.
    @staticmethod
    def is_valid_learning_rate(lr):
        print(f"Static Method -> Checking validity of LR {lr}...")
        # Simple logical check: learning rate should be positive and small
        return 0.0 < lr <= 1.0

# ==========================================
# 2. Executing & Comparing Runtimes
# ==========================================
print("--- 1. Testing Instance Methods ---")
model1 = ModelConfiguration("ResNet", 0.01)
model1.print_details()

print("\n--- 2. Testing Class Methods (Factory) ---")
# Instantiate model using the factory classmethod
model2 = ModelConfiguration.load_from_config_string("LSTM-0.0003")
model2.print_details()

# Executing class method to view frameworks
ModelConfiguration.print_frameworks()

print("\n--- 3. Testing Static Methods ---")
# Static methods are called on the class name directly without instantiation
val_1 = ModelConfiguration.is_valid_learning_rate(0.05)
val_2 = ModelConfiguration.is_valid_learning_rate(-0.1)
print(f"Is 0.05 valid? {val_1}")
print(f"Is -0.1 valid? {val_2}")

"""
Key Takeaways:
- Instance methods take `self` as the first argument, allowing them to access and modify unique object state.
- Class methods take `cls` and are decorated with `@classmethod`. They access class-level state and are often used as factory functions.
- Static methods are decorated with `@staticmethod`. They don't take `self` or `cls` and act as isolated helper functions.

Interview Relevance:
- What is the difference between `@classmethod` and `@staticmethod`? (Class methods have access to class attributes via the `cls` parameter and can modify class state; static methods have no access to class or instance variables and act as utility helpers).
- How do you implement a factory pattern in Python? (Using `@classmethod` as alternative constructors to parse file types, strings, or JSON data to return instantiated class objects).
- Can a class method call an instance method? (No, because class methods are not bound to any specific instance; they have no access to `self`).

AI/ML Relevance:
- Loading model weights: Large language models use classmethods to instantiate models from checkpoints (e.g. Hugging Face `AutoModel.from_pretrained()`).
- Data Validation: Static methods validate shape checks, value boundaries (e.g., checking if image pixels are in range [0, 255]), or string parameters before model training starts.
"""
