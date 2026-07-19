"""
Topic:
Sets in Python

Importance:
Sets are unordered collections of unique elements. They do not allow duplicate values.
Because sets are implemented using hash tables under the hood, checking membership (x in set)
is extremely fast: O(1) time complexity.
In AI/ML, sets are used to identify unique classes, handle text vocabularies, and perform database-like filter operations.

This file covers:
- Set creation and filtering duplicates
- Set membership testing efficiency
- Set modifications: add(), remove(), discard(), clear()
- Mathematical set operations: Union, Intersection, Difference, Symmetric Difference
- Practical ML application: Isolating unique category labels and stop-word filtering
"""

# ==========================================
# 1. Creation and Duplicates Filtering
# ==========================================
# Sets are defined using curly braces {} or the set() constructor.
# Note: Empty curly braces {} create an empty dictionary! Use set() for an empty set.

print("--- Set Creation & Unique Elements ---")
# List with duplicate labels
target_column = ["cat", "dog", "cat", "bird", "dog", "cat", "bird"]

# Cast list to set to extract unique values
unique_classes = set(target_column)
print(f"Target column data (List): {target_column}")
print(f"Unique class labels (Set): {unique_classes}")

# Creating empty structures
empty_dict = {}
empty_set = set()
print(f"\nType of {{}}: {type(empty_dict)}")
print(f"Type of set(): {type(empty_set)}")

# ==========================================
# 2. Set Modification & Membership
# ==========================================
# Sets are mutable, but their elements must be immutable/hashable.

print("\n--- Modifying Sets & Membership ---")
vocab = {"data", "science", "model"}

# add(): Adds an element
vocab.add("python")
vocab.add("model")  # Adding duplicate: will be ignored silently
print(f"Vocab set: {vocab}")

# Membership check: extremely fast O(1) lookup
print(f"Is 'science' in vocab? {'science' in vocab}")
print(f"Is 'regression' in vocab? {'regression' in vocab}")

# remove() vs discard():
# remove() raises a KeyError if the element does not exist.
# discard() ignores the request safely without error if the element is missing.
vocab.discard("regression")  # Safe, no error
# vocab.remove("regression")  # Uncommenting raises KeyError

vocab.remove("model")
print(f"Vocab after removing 'model': {vocab}")

# ==========================================
# 3. Mathematical Set Operations
# ==========================================
# Sets support classic Venn diagram operations.

print("\n--- Set Mathematics ---")
features_dataset_a = {"age", "income", "zipcode", "gender"}
features_dataset_b = {"income", "credit_score", "zipcode", "loan_status"}

# A. Union: elements in set A OR set B (all features)
all_features = features_dataset_a.union(features_dataset_b)  # or: features_dataset_a | features_dataset_b
print(f"Union (All Features): {all_features}")

# B. Intersection: elements in set A AND set B (common features)
common_features = features_dataset_a.intersection(features_dataset_b)  # or: features_dataset_a & features_dataset_b
print(f"Intersection (Common): {common_features}")

# C. Difference: elements in set A but not in set B
only_in_a = features_dataset_a.difference(features_dataset_b)  # or: features_dataset_a - features_dataset_b
print(f"Difference (Only in A): {only_in_a}")

# D. Symmetric Difference: elements in A or B, but NOT in both
unique_to_each = features_dataset_a.symmetric_difference(features_dataset_b)  # or: features_dataset_a ^ features_dataset_b
print(f"Symmetric Difference (Unshared): {unique_to_each}")

# ==========================================
# 4. Hands-on ML Use-Case: NLP Stop-Words Filter
# ==========================================
# In NLP, stop-words (common words like 'the', 'is', 'a') are filtered out of text inputs.
print("\n--- Practical ML Use-Case: Stop-Words Filter ---")

stop_words = {"the", "is", "a", "an", "and", "or", "in", "to"}
sentence_tokens = ["the", "classifier", "is", "trained", "on", "a", "clean", "and", "scaled", "dataset"]

# Filtering tokens using membership checks
filtered_tokens = []
for token in sentence_tokens:
    if token not in stop_words:
        filtered_tokens.append(token)

print(f"Original text tokens: {sentence_tokens}")
print(f"Stop-word filtered tokens: {filtered_tokens}")

"""
Key Takeaways:
- Sets contain only unique, unordered elements.
- Membership checking (`value in set`) has a time complexity of O(1).
- Sets can perform mathematical operations like Union (`|`), Intersection (`&`), Difference (`-`), and Symmetric Difference (`^`).
- Empty sets must be created using `set()`, not `{}`.

Interview Relevance:
- What is the time complexity of checking if an element is in a list vs a set? (List: O(N) because it scans sequentially. Set: O(1) because it uses a hash lookup).
- Why cannot we add a list to a set? (Sets require elements to be hashable/immutable. Since lists are mutable, their contents can change, which changes their hash, so they are not allowed).
- Explain the difference between `remove()` and `discard()`.

AI/ML Relevance:
- Categorical features: Before encoding text categories (like "Country" column), set() is used to extract the distinct categories list.
- Vocabulary construction: Large language models and text models build their vocabulary sets from training corpora to map tokens to ID keys.
"""
