"""
Topic:
Encapsulation in Python

Importance:
Encapsulation restricts direct access to an object's components to prevent accidental modification
and maintain class state integrity.
In AI/ML, encapsulation protects model weights, layer layers configuration state, and checks parameter input limits (like ensuring learning rates are non-negative).

This file covers:
- Access Modifiers: Public, Protected (_), and Private (__) attributes
- Name Mangling under the hood
- Getter and Setter methods
- The @property decorator (Pythonic attribute management)
- Practical ML application: Encapsulating learning rate validation and neural network weights
"""

# ==========================================
# 1. Access Modifiers: Public, Protected, Private
# ==========================================
# In Python, encapsulation conventions are denoted by underscores:
# - public_var: Accessible anywhere.
# - _protected_var: Accessible within class and subclasses (convention check).
# - __private_var: Accessible only inside the class itself. Triggers Name Mangling.

class ModelWeightsContainer:
    def __init__(self, init_weights):
        self.public_id = "weights_v1"        # Public
        self._protected_state = "frozen"     # Protected
        self.__weights = init_weights        # Private

    def print_weights(self):
        # Private variables can be accessed inside class scope
        print("Internal private weights value:", self.__weights)

print("--- Access Modifiers ---")
container = ModelWeightsContainer([0.5, -0.2, 0.9])

print("Accessing Public variable:", container.public_id)
print("Accessing Protected variable (convention check):", container._protected_state)

# Attempting to access private variable directly raises an AttributeError:
# print(container.__weights)

# Name Mangling: Python renames private variables under the hood to _ClassName__variable_name.
# It can still be accessed via its mangled name (though highly discouraged!):
print("Accessing Private variable (via Name Mangling):", container._ModelWeightsContainer__weights)

# ==========================================
# 2. Getters, Setters and the @property Decorator
# ==========================================
# Rather than exposing attributes, we wrap them in getter and setter methods to implement validation logic.
# Python uses `@property` to access methods as standard properties.

class NeuralNetHyperparameters:
    def __init__(self, lr=0.01):
        self.__learning_rate = lr  # Private attribute

    # Getter: Exposes the private attribute using @property
    @property
    def learning_rate(self):
        print("Getter: Fetching learning rate...")
        return self.__learning_rate

    # Setter: Valdiates the input value before saving
    @learning_rate.setter
    def learning_rate(self, value):
        print(f"Setter: Attempting to update learning rate to {value}...")
        if value <= 0:
            raise ValueError("Error: Learning rate must be strictly positive!")
        if value > 1.0:
            raise ValueError("Error: Learning rate value is too high (> 1.0) and will cause gradient explosion!")
        self.__learning_rate = value

print("\n--- Property Decorator Getter / Setter ---")
nn_params = NeuralNetHyperparameters(lr=0.01)

# Call getter (notice no parentheses! Accessed like an attribute)
print("Current learning rate value:", nn_params.learning_rate)

# Call setter (accessed like standard assignment)
nn_params.learning_rate = 0.05
print("Updated learning rate value:", nn_params.learning_rate)

# Test validation constraints
print("\nTesting validation constraint boundary checks:")
try:
    nn_params.learning_rate = -0.5
except ValueError as e:
    print(f"Validation caught error: {e}")

try:
    nn_params.learning_rate = 12.0
except ValueError as e:
    print(f"Validation caught error: {e}")

"""
Key Takeaways:
- Encapsulation groups variables and methods, blocking unauthorized external edits.
- Protected attributes (`_name`) are a developer convention suggesting it should not be accessed outside subclasses.
- Private attributes (`__name`) are enforced via name mangling (`_ClassName__name`).
- The `@property` decorator simplifies syntax for accessing getter and setter methods.

Interview Relevance:
- Does Python have true private variables? (No. Python uses name mangling to rename private variables, but they can still be accessed if the mangled name is used. It is a soft-barrier).
- Explain name mangling. (Python renames double-underscore attributes to `_ClassName__attributeName` to prevent naming conflicts in inheritance).
- What is the advantage of `@property` over traditional `get_val()` and `set_val()` methods? (It keeps attributes clean and allows adding validation layers to attributes later without modifying the code that accesses them).

AI/ML Relevance:
- PyTorch nn.Module: Weights and biases of layers are encapsulated within the network instance. Subclasses access them using properties (like `model.parameters()`) rather than altering raw state matrices.
- Pipeline Safety: Restricting write-access to hyperparameters preventing bugs during parallel training sweeps where values could be corrupted by asynchronous access threads.
"""
