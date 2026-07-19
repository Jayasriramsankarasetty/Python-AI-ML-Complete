"""
Topic:
Polymorphism in Python

Importance:
Polymorphism ("many forms") allows different objects to respond to the same method call
in their own unique ways.
In AI/ML, polymorphism is used to design unified prediction loops where different algorithms
(e.g., SVM, DecisionTree, LogisticRegression) all share a common `.predict()` interface.

This file covers:
- Polymorphism via Method Overriding (duck typing)
- Overloading functions (simulating overloading in Python)
- Operator Overloading using magic methods (__str__, __add__)
- Practical ML application: Uniform model prediction loop and adding model weight objects
"""

# ==========================================
# 1. Polymorphism via Method Overriding
# ==========================================
# Different classes can define a method with the same name.

class DecisionTree:
    def predict(self, data):
        print("DecisionTree -> Running tree boundary checks...")
        return [1 if val > 5 else 0 for val in data]

class SVM:
    def predict(self, data):
        print("SVM -> Running hyperplane margin calculations...")
        return [1 if val > 2 else 0 for val in data]

# A unified function that invokes predict() polymorphically (Duck Typing)
def execute_model_predictions(model_object, data):
    # Calling predict() without caring about concrete type
    results = model_object.predict(data)
    print(f"Results: {results}")

print("--- Polymorphic Execution ---")
test_data = [1.5, 6.2, 3.8]

dt_clf = DecisionTree()
svm_clf = SVM()

execute_model_predictions(dt_clf, test_data)
execute_model_predictions(svm_clf, test_data)

# ==========================================
# 2. Simulating Method Overloading
# ==========================================
# Unlike languages like Java/C++, Python does NOT support method overloading (multiple methods with same name but different parameters).
# If you define two methods with the same name, the last one overrides the previous ones.
# In Python, we simulate overloading using default arguments or check variable types.

class ParameterCalculator:
    def compute_loss(self, actual, predicted, reduction="mean"):
        # Simulated overloading check
        diffs = [a - p for a, p in zip(actual, predicted)]
        if reduction == "mean":
            return sum(diffs) / len(diffs)
        elif reduction == "sum":
            return sum(diffs)
        else:
            return diffs

print("\n--- Simulated Overloading ---")
calc = ParameterCalculator()
print("Loss (Mean):", calc.compute_loss([10, 12], [8, 9]))
print("Loss (Sum):", calc.compute_loss([10, 12], [8, 9], reduction="sum"))

# ==========================================
# 3. Operator Overloading & Magic Methods
# ==========================================
# Python allows re-defining behavior of operators (+, -, *, etc.) using special dunder methods.

class ModelWeights:
    def __init__(self, val_list):
        self.vals = val_list
        
    # Overloading the addition (+) operator
    def __add__(self, other):
        # Adds corresponding weights together
        added_vals = [a + b for a, b in zip(self.vals, other.vals)]
        return ModelWeights(added_vals)
        
    # Overloading print() output representation
    def __str__(self):
        return f"Weights array: {self.vals}"

print("\n--- Operator Overloading ---")
w1 = ModelWeights([0.25, 0.45, -0.10])
w2 = ModelWeights([0.10, 0.15, 0.30])

# Combines weights using '+'
w_combined = w1 + w2

print("w1:", w1)
print("w2:", w2)
print("Combined (w1 + w2):", w_combined)

"""
Key Takeaways:
- Polymorphism allows different classes to share a method interface.
- Python is dynamically typed and uses "Duck Typing" (if it walks like a duck, it is a duck).
- Method overloading is simulated in Python using default parameters or type checking.
- Operator overloading redefines arithmetic actions via special dunder methods (`__add__`, `__sub__`, `__mul__`).

Interview Relevance:
- Does Python support Method Overloading? (Not natively by writing duplicate method names. We simulate it using default/keyword arguments or variable arguments `*args`/`**kwargs`).
- What is Duck Typing? (The concept that an object's suitability is determined by the presence of certain methods/attributes rather than actual inheritance).
- Which magic method is overridden to overload the '+' operator? (The `__add__` method).

AI/ML Relevance:
- Model ensembles: In ensemble learning (like Random Forests or Voting Classifiers), predictions from multiple independent base estimators are averaged by looping over estimator objects polymorphically.
- Parameter optimization: Federated Learning merges weight updates from edge devices by overloading addition (`+`) and division (`/`) on model weights.
"""
