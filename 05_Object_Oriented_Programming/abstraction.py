"""
Topic:
Abstraction in Python

Importance:
Abstraction hides internal complexity and exposes only essential features.
By defining abstract base classes, we establish clean API contracts (interfaces)
that enforce consistent method declarations across subclasses.
In AI/ML, estimator architectures (like scikit-learn's BaseEstimator) use abstract designs.

This file covers:
- Abstract Classes and Abstract Methods
- The 'abc' module (ABC class and @abstractmethod decorator)
- Preventing instantiation of abstract parent classes
- Enforcing child class implementations
- Practical ML application: Constructing a BaseEstimator abstract template
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. Defining an Abstract Class
# ==========================================
# To make a class abstract:
# 1. Inherit from 'ABC' (Abstract Base Class)
# 2. Mark its key signatures with the '@abstractmethod' decorator.
# Note: Abstract classes CANNOT be instantiated directly.

class BaseEstimator(ABC):
    """
    Abstract Base Class for all ML Estimators.
    Enforces that all child models must implement fit and predict methods.
    """
    
    @abstractmethod
    def fit(self, x, y):
        """Forces subclasses to implement model training."""
        pass
        
    @abstractmethod
    def predict(self, x):
        """Forces subclasses to implement model inference/prediction."""
        pass

    # Abstract classes can also contain regular concrete methods!
    def display_welcome_banner(self):
        print("Welcome to Abstract Estimator interface engine!")

# ==========================================
# 2. Child Implementation & Verification
# ==========================================

class CustomLinearRegressor(BaseEstimator):
    def __init__(self, weight=2.0):
        self.w = weight
        
    # Implementing the abstract fit method
    def fit(self, x, y):
        print("CustomLinearRegressor -> Implementing fit() logic...")
        # Simplistic fit: assigning slope weight
        self.w = sum(y) / sum(x)
        
    # Implementing the abstract predict method
    def predict(self, x):
        print("CustomLinearRegressor -> Implementing predict() logic...")
        return [val * self.w for val in x]

# ==========================================
# 3. Executing and Handling Errors
# ==========================================
print("--- 1. Attempting Abstract Instantiation ---")
try:
    # This will raise a TypeError because BaseEstimator is abstract and has abstract methods
    base = BaseEstimator()
except TypeError as e:
    print(f"Instantiation failed as expected: {e}")

print("\n--- 2. Instantiating Concrete Child Estimator ---")
model = CustomLinearRegressor()
model.display_welcome_banner()  # Calling concrete inherited method

# Call implemented abstract methods
model.fit([1, 2, 3], [3, 6, 9])
predictions = model.predict([10, 20])
print("Predictions:", predictions)

# ==========================================
# 4. Incomplete Child Class (Demonstration)
# ==========================================
# If a child class fails to implement ANY abstract method of its parent, it cannot be instantiated either.

class IncompleteRegressor(BaseEstimator):
    def fit(self, x, y):
        print("Fit implemented, but predict left out...")
    # predict() is missing!

print("\n--- 3. Testing Incomplete Subclass ---")
try:
    incomplete_model = IncompleteRegressor()
except TypeError as e:
    print(f"Incomplete class instantiation failed: {e}")

"""
Key Takeaways:
- Abstraction focuses on 'what' a class does rather than 'how' it does it.
- Inheriting from `ABC` and decorating with `@abstractmethod` blocks direct instantiation of the parent.
- Subclasses must implement all abstract methods to be instantiated.
- Abstract classes can contain both abstract (empty) methods and concrete (implemented) methods.

Interview Relevance:
- What is an abstract class and how is it created in Python? (Explain: inherit from `ABC` from the `abc` module and use `@abstractmethod` decorators).
- Can you instantiate an abstract class? (No, Python prevents instantiation of classes containing unimplemented abstract methods).
- What is the difference between an Interface and an Abstract Class? (In Python, there is no separate 'interface' keyword. Abstract classes containing only abstract methods act as interfaces, while classes containing a mix of abstract and concrete methods are abstract classes).

AI/ML Relevance:
- Scikit-learn Design: All custom transformers must inherit from `BaseEstimator` and override fit/transform structures to integrate with `Pipeline` grids.
- Unified APIs: Abstraction makes it easy to switch out complex models (e.g. swap SVM with LightGBM) in production because they share identical interface calls.
"""
