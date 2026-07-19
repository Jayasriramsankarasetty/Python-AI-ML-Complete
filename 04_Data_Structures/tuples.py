"""
Topic:
Tuples in Python

Importance:
Tuples are ordered, immutable sequences. Because they cannot be altered after creation,
they protect critical data configurations from being overwritten.
In AI/ML, tuples represent dimensions (shapes) of tensors/arrays and are returned by coordinate grids.

This file covers:
- Tuple creation and index access
- Tuple Immutability concept
- Unpacking Tuples (and the use of the asterisk variable)
- Single-element tuple syntax
- Tuple methods: count() and index()
- Practical ML application: Representing image dataset shape metadata
"""

# ==========================================
# 1. Creation, Indexing & Immutability
# ==========================================
# Tuples are created using round parentheses ().

print("--- Tuple Creation & Immutability ---")
# Image metadata tuple: (height, width, color_channels)
image_shape = (224, 224, 3)
print(f"Image Shape Tuple: {image_shape}")
print(f"Number of dimensions: {len(image_shape)}")
print(f"Height dimension: {image_shape[0]}")

# Single-element tuple syntax
# Note: You MUST include a trailing comma, otherwise Python treats it as a standard grouped expression.
not_a_tuple = ("cnn")      # type: str
actual_tuple = ("cnn",)    # type: tuple
print(f"\nType with no comma: {type(not_a_tuple)}")
print(f"Type with comma: {type(actual_tuple)}")

# Immutability
# Trying to edit a tuple will raise a TypeError:
# image_shape[0] = 512

# ==========================================
# 2. Tuple Unpacking
# ==========================================
# Unpacking allows assigning tuple elements to individual variables.

print("\n--- Tuple Unpacking ---")
h, w, c = image_shape
print(f"Unpacked variables -> Height: {h}, Width: {w}, Channels: {c}")

# Extended unpacking using * (captures extra elements as a list)
model_metrics = ("ResNet", 0.94, 0.91, 0.88, "Adam", "Epoch 100")
name, acc, *other_metrics, optimizer, epoch = model_metrics

print(f"Model Name: {name}")
print(f"Accuracy: {acc}")
print(f"Captured other metrics (List): {other_metrics}")
print(f"Optimizer: {optimizer} | Epoch: {epoch}")

# ==========================================
# 3. Tuple Methods: count() and index()
# ==========================================
# Since tuples are immutable, they only have two built-in index-search methods.

print("\n--- Tuple Methods ---")
class_labels = ("cat", "dog", "cat", "bird", "dog", "dog")

# count(): Returns number of occurrences of a value
dog_count = class_labels.count("dog")
print(f"Occurrences of 'dog' class: {dog_count}")

# index(): Returns first index position of a value
first_bird_idx = class_labels.index("bird")
print(f"First position of 'bird': {first_bird_idx}")

# ==========================================
# 4. Hands-on ML Use-Case: Tensor Shape Checks
# ==========================================
# Deep learning libraries represent inputs as dimensional shapes.
# Functions check inputs using tuples.
print("\n--- Practical ML Use-Case: Tensor Shapes ---")

def validate_tensor_shape(input_shape):
    """Checks if input matches expected dimensions for convolutional layer"""
    # Expected: (batch_size, channels, height, width)
    expected_dimensions = 4
    
    if len(input_shape) != expected_dimensions:
        print(f"Error: Expected {expected_dimensions}D tensor shape, got {len(input_shape)}D.")
        return False
        
    batch, channels, h, w = input_shape
    print(f"Input is valid: Batch size={batch}, Channels={channels}, Size={h}x{w}")
    return True

# Valid tensor shape input
validate_tensor_shape((32, 3, 224, 224))
# Invalid tensor shape input
validate_tensor_shape((224, 224, 3))

"""
Key Takeaways:
- Tuples are ordered, indexable, and immutable.
- A trailing comma is required to define a single-element tuple: `(value,)`.
- Tuples consume less memory than lists and are optimized for read-only sequences.
- Tuples can be used as keys in dictionaries, whereas lists cannot (because keys must be hashable).

Interview Relevance:
- What is the main difference between lists and tuples? (Lists are mutable and have more methods; tuples are immutable, faster, and hashable if all their items are hashable).
- How do you create a single-element tuple? (Include a trailing comma, e.g., `my_tuple = (5,)`).
- Why are tuples hashable while lists are not? (Since tuples are immutable, their contents cannot change, giving them a constant hash value over their lifetime).

AI/ML Relevance:
- Shapes: PyTorch `tensor.shape` and NumPy `array.shape` always return tuples because dimensions should not be modified in-place accidentally.
- Function outputs: Functions returning multiple variables (like predictions and actual labels or loss values) package them into tuples for clean unpacking.
"""
