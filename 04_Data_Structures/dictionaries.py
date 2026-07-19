"""
Topic:
Dictionaries in Python

Importance:
Dictionaries are unordered (ordered by insertion since Python 3.7), mutable mappings of key-value pairs.
Like sets, dictionaries use hash tables and provide fast O(1) average lookup speed.
In AI/ML, dictionaries represent configurations, hyperparameters, metrics storage, and raw JSON logs.

This file covers:
- Dictionary creation and key constraints
- Accessing values safely using get()
- Modifying and adding values
- Common dictionary methods: keys(), values(), items(), update(), pop()
- Iterating over key-values
- Nested dictionaries (representing hyperparameter tuning grids)
- Practical ML application: Mapping prediction probability logits to class name labels
"""

# ==========================================
# 1. Creation, Accessing & Constraints
# ==========================================
# Keys must be unique and hashable (immutable - e.g. strings, numbers, tuples).
# Values can be any data type, mutable or immutable.

print("--- Dictionary Basics ---")
# Model hyperparameters config
hyperparams = {
    "model_name": "RandomForest",
    "n_estimators": 100,
    "max_depth": 10,
    "bootstrap": True
}

# Accessing values (raises KeyError if key is not found)
print("Model name:", hyperparams["model_name"])

# Safely accessing values using get(key, default) - returns default if key missing
learning_rate = hyperparams.get("learning_rate", 0.001)  # returns 0.001 instead of error
print("Learning rate (safely fetched):", learning_rate)

# ==========================================
# 2. Modifying and Common Methods
# ==========================================
print("\n--- Modifying & Methods ---")

# Adding a new key-value or modifying existing
hyperparams["learning_rate"] = 0.01      # Add new key
hyperparams["max_depth"] = 15            # Modify existing key
print("Modified config:", hyperparams)

# keys() and values(): returns view objects of keys and values
print("Keys view:", list(hyperparams.keys()))
print("Values view:", list(hyperparams.values()))

# items(): returns a list of (key, value) tuple pairs
print("\nItems view:")
for key, value in hyperparams.items():
    print(f"  {key} -> {value}")

# update(): merges another dictionary
new_updates = {"criterion": "entropy", "min_samples_split": 2}
hyperparams.update(new_updates)
print("\nConfig after update():", hyperparams)

# pop(): removes a key and returns its value
removed_value = hyperparams.pop("bootstrap")
print(f"Popped value: {removed_value} | Remaining dict: {hyperparams}")

# ==========================================
# 3. Nested Dictionaries
# ==========================================
# Nested dictionaries are commonly used to store structural information like grids of parameters.

print("\n--- Nested Dictionaries ---")
model_tuning_grid = {
    "LogisticRegression": {
        "C": [0.1, 1.0, 10.0],
        "penalty": ["l1", "l2"]
    },
    "SVM": {
        "C": [1.0, 100.0],
        "kernel": ["linear", "rbf"]
    }
}

# Accessing nested structures
svm_kernels = model_tuning_grid["SVM"]["kernel"]
print(f"SVM kernels to search: {svm_kernels}")

# ==========================================
# 4. Hands-on ML Use-Case: Logit Probability Map
# ==========================================
# Simulating model prediction outputs where a network returns index weights,
# and we must map the winning index back to class name mappings.
print("\n--- Practical ML Use-Case: Classification Map ---")

# Index to Class name dictionary mapping
index_to_label = {
    0: "Negative/Spam",
    1: "Positive/Ham",
    2: "Neutral/Flagged"
}

# Model outputs probability vector for a sentence (softmax logits output)
raw_logits = [0.12, 0.08, 0.80]  # Index 2 has the highest weight

# Find index of maximum value
max_val = max(raw_logits)
winning_idx = raw_logits.index(max_val)

# Resolve target name
predicted_class_name = index_to_label.get(winning_idx, "Unknown")

print(f"Raw Probabilities: {raw_logits}")
print(f"Winning Index: {winning_idx} (Max probability: {max_val})")
print(f"Prediction Label Result: {predicted_class_name}")

"""
Key Takeaways:
- Dictionaries map unique keys to values. Keys must be hashable.
- `dict.get(key, default)` is the industry-standard way to avoid runtime KeyErrors.
- Dictionaries are mutable; values can be updated or popped.
- Iterating over a dictionary defaults to iterating over its keys. Use `.items()` for key-value tuple iterations.

Interview Relevance:
- How does a dictionary store and retrieve elements in O(1) time complexity? (Explain hash function mappings to array buckets, resolving collisions via chaining or open addressing).
- Can a list be used as a key in a dictionary? (No, lists are mutable and therefore unhashable).
- What is the difference between dict.keys() view object and a list? (The view object is dynamic; it updates automatically when the dictionary updates, and consumes minimal memory).

AI/ML Relevance:
- Configuration: Hyperparameters of deep learning training runs are specified as dictionaries and dumped as JSON configuration files.
- Serialization: ML model states (like PyTorch `state_dict`) save model weights and biases maps as python dictionaries mapping string layer-weights to tensor arrays.
"""
