"""
Topic:
Comprehensions (List, Dictionary, and Set)

Importance:
Comprehensions offer a concise syntax to create collections from existing collections.
They run faster than traditional loops because they are optimized at the C-level in Python.
In AI/ML, comprehensions are constantly used to transform dataset features, filter outliers,
and build vocabulary indexing dictionaries.

This file covers:
- List Comprehension (Basic & Conditional)
- List Comprehension with If-Else logic
- Dictionary Comprehension
- Set Comprehension
- Nested List Comprehension (brief overview)
- Practical ML application: Building a vocabulary tokenizer dictionary
"""

# ==========================================
# 1. List Comprehensions
# ==========================================
# Syntax: [expression for item in iterable if condition]

print("--- List Comprehension ---")
raw_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional loop to square even numbers
traditional_squares = []
for x in raw_data:
    if x % 2 == 0:
        traditional_squares.append(x ** 2)
print("Traditional Loop Squares:", traditional_squares)

# Equivalent List Comprehension
comprehension_squares = [x ** 2 for x in raw_data if x % 2 == 0]
print("List Comprehension Squares:", comprehension_squares)

# List Comprehension with If-Else (Ternary) logic
# Syntax: [value_if_true if condition else value_if_false for item in iterable]
# Example: Binary thresholding probabilities
probabilities = [0.85, 0.42, 0.61, 0.23, 0.95]
binary_predictions = [1 if prob >= 0.5 else 0 for prob in probabilities]
print(f"Probabilities: {probabilities}")
print(f"Binary Predictions: {binary_predictions}")

# ==========================================
# 2. Dictionary & Set Comprehensions
# ==========================================
# Dictionary Syntax: {key_expr: val_expr for item in iterable}
# Set Syntax: {expr for item in iterable}

print("\n--- Dict & Set Comprehensions ---")

# Set comprehension: extract unique normalized feature names
dirty_features = ["  Age ", " Income  ", " Age", " Credit_Score "]
clean_features_set = {feat.strip().lower() for feat in dirty_features}
print("Clean Features Set:", clean_features_set)

# Dictionary comprehension: Square values
numbers = [1, 2, 3, 4]
squares_dict = {num: num ** 2 for num in numbers}
print("Squares Dictionary:", squares_dict)

# ==========================================
# 3. Nested List Comprehensions (For Matrices)
# ==========================================
# Creating a 3x3 identity-like matrix structure
# Outer bracket represents rows; inner bracket represents elements
print("\n--- Nested List Comprehension ---")
matrix_3x3 = [[1 if row == col else 0 for col in range(3)] for row in range(3)]
print("Matrix 3x3:")
for row in matrix_3x3:
    print(row)

# ==========================================
# 4. Hands-on ML Use-Case: NLP Vocab Tokenizer
# ==========================================
# In text preprocessing, words are mapped to unique integer IDs.
# We will use comprehensions to create a vocabulary dictionary (word -> index ID).
print("\n--- Practical ML Use-Case: NLP Vocabulary Generator ---")

raw_documents = [
    "deep learning is neural networks",
    "neural networks compute patterns",
    "learning patterns requires data"
]

# Step 1: Flatten all words into a single list, strip them, and convert to lower
# Traditional nested loop flattened into one list comprehension!
all_words = [word for doc in raw_documents for word in doc.lower().split()]

# Step 2: Use set comprehension to extract unique vocabulary
vocab_set = {word for word in all_words}
# Sort vocabulary alphabetically for consistency
sorted_vocab = sorted(list(vocab_set))

# Step 3: Use dictionary comprehension to map: word -> unique_integer_index
word_to_id = {word: idx for idx, word in enumerate(sorted_vocab)}

print(f"Raw Corpus:\n  {raw_documents}")
print(f"Sorted Vocabulary List:\n  {sorted_vocab}")
print(f"Vocabulary Word-to-ID Index Mapping:\n  {word_to_id}")

"""
Key Takeaways:
- Comprehensions provide a concise way to create lists, dictionaries, and sets.
- If-conditions go at the END of the comprehension: `[x for x in list if x > 5]`.
- If-else ternary structures go at the START of the comprehension: `[x if x > 5 else 0 for x in list]`.
- Comprehensions are computationally optimized in Python, running faster than equivalent standard loop appends.

Interview Relevance:
- Rewrite a nested loop as a list comprehension.
- Where does the 'if' condition go in a list comprehension when combined with an 'else' block? (At the beginning, e.g. `[x if x > 0 else 0 for x in list]`).
- What is the difference between list comprehensions and generator expressions? (List comprehensions build the list in memory immediately using `[]`; generator expressions compute values lazily on demand using `()`, saving memory).

AI/ML Relevance:
- Categorical mappings: Generating index mappings (like `label_to_index`) is standard practice for preparing text data for PyTorch embeddings.
- Array scaling: Comprehensions scale small arrays or coordinates list before feeding them to visualization graphs or matrix utilities.
"""
