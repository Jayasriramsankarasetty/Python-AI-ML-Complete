"""
Topic:
Inheritance in Python

Importance:
Inheritance allows a new class (child/derived) to adopt attributes and methods from an
existing class (parent/base). This promotes code reuse and structures hierarchical setups.
In ML framework architectures, neural network models inherit from structural base classes (like PyTorch nn.Module).

This file covers:
- Base class (Parent) and Derived class (Child)
- Method overriding
- Using the super() function to access parent attributes/constructors
- Multilevel Inheritance (brief example)
- Practical ML application: Base Regressor parent inherited by LinearRegressor child
"""

# ==========================================
# 1. Base Class and Derived Class
# ==========================================

class ModelBase:
    """Parent Class holding general configuration metrics"""
    def __init__(self, task_type):
        self.task_type = task_type
        self.is_trained = False
        print(f"Parent constructor loaded for task: {self.task_type}")
        
    def evaluate(self):
        print("Evaluating generic performance index...")

# ==========================================
# 2. Child Class & Method Overriding (using super())
# ==========================================
# Child class inherits parent by passing ParentName inside class parameters: Class Child(Parent)

class Regressor(ModelBase):
    """Child Class representing regression algorithms"""
    def __init__(self, algo_name, penalty="None"):
        # super() calls the constructor of the parent class (ModelBase)
        super().__init__(task_type="Regression")
        self.algo = algo_name
        self.penalty = penalty
        
    # Method Overriding: Redefining evaluate() to add specific regression details
    def evaluate(self):
        # We can call the parent's evaluate() using super()
        super().evaluate()
        print(f"Child Override -> Calculating Mean Squared Error (MSE) for {self.algo}...")

# ==========================================
# 3. Multilevel Inheritance
# ==========================================
# A child class can itself act as a parent class to another subclass.

class LinearRegressor(Regressor):
    """Grandchild class representing Linear Regression specifically"""
    def __init__(self, learning_rate=0.01):
        # Calls constructor of Regressor
        super().__init__(algo_name="Linear Regression", penalty="l2")
        self.lr = learning_rate
        
    def fit_gradients(self):
        print(f"Executing gradient updates with learning rate {self.lr}...")

# ==========================================
# 4. Executing Classes
# ==========================================
print("--- Instantiating Base Child Model ---")
basic_regressor = Regressor("RandomForestRegressor")
print("Task type inherited:", basic_regressor.task_type)
basic_regressor.evaluate()

print("\n--- Instantiating Grandchild Model ---")
linear_model = LinearRegressor(learning_rate=0.05)
print(f"Inherited properties -> Algo: {linear_model.algo} | Penalty: {linear_model.penalty} | Task: {linear_model.task_type}")
linear_model.fit_gradients()
linear_model.evaluate()

"""
Key Takeaways:
- Inheritance passes properties and methods from parent to child classes, reducing code redundancy.
- Use `super()` to call parent constructors (`super().__init__()`) and override parent methods.
- Method overriding allows a subclass to provide a specific implementation of a method already defined in its parent class.

Interview Relevance:
- Explain what the super() function does. (It returns a proxy object that delegates method calls to a parent or sibling class of type).
- Does Python support multiple inheritance? (Yes. A class can inherit from multiple parent classes, e.g. `class Child(ParentA, ParentB)`. The method resolution order is resolved via the MRO algorithm).
- What is Method Resolution Order (MRO)? (It is the order in which Python searches for inherited methods. You can view it by calling `ClassName.mro()` or ClassName.__mro__).

AI/ML Relevance:
- Custom Network Layers: When building models in PyTorch, custom neural networks must inherit from `torch.nn.Module`, and the child constructor MUST run `super().__init__()` to register layer components properly.
- Dataset Loaders: PyTorch custom dataset classes inherit from `torch.utils.data.Dataset` to override the length (`__len__`) and index access (`__getitem__`) methods.
"""
