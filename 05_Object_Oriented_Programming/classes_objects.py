"""
Topic:
Classes and Objects in Python

Importance:
Object-Oriented Programming (OOP) organizes code by bundling state (attributes) and behavior (methods)
into reusable blueprints.
In AI/ML, classes represent datasets, models, neural network layers, and training pipelines.

This file covers:
- Defining a Class and instantiating an Object
- The 'self' parameter
- Class variables vs Instance variables
- Accessing and modifying attributes
- Practical ML application: Creating a Dataset metadata container
"""

# ==========================================
# 1. Defining a Class and Instantiating
# ==========================================
# A Class is a blueprint. An Object is an instance of a Class.
# The 'self' parameter represents the current instance of the class and is used to access its attributes.

class SimpleModelBlueprint:
    # A simple class method
    def train(self):
        print("Training activated on the model instance!")

print("--- Class Instantiation ---")
# Instantiating an object
model_instance = SimpleModelBlueprint()
print(f"Object Memory Address Reference: {model_instance}")
# Calling a method
model_instance.train()

# ==========================================
# 2. Class Variables vs Instance Variables
# ==========================================
# - Class Variables: Shared across all instances of the class. Defined directly in the class body.
# - Instance Variables: Unique to each instance. Defined inside methods (typically using self).

class MLDataset:
    # Class Variable (Shared among all dataset objects)
    supported_formats = ["csv", "json", "parquet"]
    
    def set_dataset_details(self, name, size_rows):
        # Instance Variables (Unique to each object)
        self.dataset_name = name
        self.rows = size_rows

print("\n--- Variables Scope (Class vs Instance) ---")
# Instantiate dataset 1
train_data = MLDataset()
train_data.set_dataset_details("train_house_prices", 10000)

# Instantiate dataset 2
test_data = MLDataset()
test_data.set_dataset_details("test_house_prices", 2500)

# Accessing Instance Variables
print(f"Train Dataset: {train_data.dataset_name} | Rows: {train_data.rows}")
print(f"Test Dataset: {test_data.dataset_name} | Rows: {test_data.rows}")

# Accessing Class Variables (can be accessed via class name or instance)
print("Formats (via Class name):", MLDataset.supported_formats)
print("Formats (via train_data instance):", train_data.supported_formats)

# Modifying a class variable updates it for all instances
MLDataset.supported_formats.append("txt")
print("Formats after adding 'txt' via class update:", test_data.supported_formats)

"""
Key Takeaways:
- A class is a blueprint; an object is the concrete instantiation of that blueprint.
- The `self` parameter must be the first parameter of any instance method, pointing to the calling object.
- Instance variables are unique to each object; class variables are shared across all instances.
- Standard variable names use lowercase snake_case; Class names use PascalCase (CamelCase starting with uppercase).

Interview Relevance:
- What is the difference between a class variable and an instance variable? (Class variables are shared and defined in class scope; instance variables are unique to instances and defined on `self`).
- What does the 'self' parameter do? (It acts as a reference to the active object, allowing access to instance attributes and other methods).
- What happens if you omit 'self' from an instance method definition? (It raises a TypeError when called on an instance, because Python automatically passes the instance as the first argument).

AI/ML Relevance:
- Object models: In PyTorch, models are defined by subclassing `torch.nn.Module`. In scikit-learn, estimators (like `LinearRegression`) are classes holding model weights as instance attributes.
- State persistence: Storing data pathways, training weights, and flags inside class scopes prevents global namespace pollution.
"""
