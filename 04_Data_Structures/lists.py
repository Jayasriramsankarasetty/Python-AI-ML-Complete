"""
Topic:
Lists in Python

Importance:
Lists are ordered, mutable, and allow duplicate elements.
They are heavily used in data pipelines, for iterating through files, keeping track of epoch losses,
and building basic numerical structures before converting them to NumPy arrays.

This file covers:
- List creation and indexing (positive and negative)
- Slicing lists
- Common list methods: append(), extend(), insert(), remove(), pop(), sort()
- Shallow vs Deep reference copy concepts
- Practical ML application: Storing training log history and slicing mini-batches
"""

# ==========================================
# 1. Creation, Indexing & Slicing
# ==========================================
# Lists are created using square brackets [].

print("--- List Basics & Indexing ---")
features = ["age", "salary", "purchased", "gender", "country"]

# Positive Indexing (starts at 0)
print("First feature:", features[0])

# Negative Indexing (starts at -1 from end)
print("Last feature:", features[-1])

# Slicing: list[start:stop:step] - excludes 'stop' index
print("\n--- Slicing Examples ---")
print("First three features:", features[0:3])  # indices 0, 1, 2
print("All features except first:", features[1:])
print("Features at even indices (step=2):", features[::2])
print("Reverse the features list:", features[::-1])

# ==========================================
# 2. Modifying Lists & Common Methods
# ==========================================
# Lists are mutable (can be changed in-place).

print("\n--- List Modifications & Methods ---")
# Start with empty list of epoch losses
loss_history = []

# append(): Adds element to the end of the list
loss_history.append(0.85)
loss_history.append(0.62)
loss_history.append(0.44)
print("Loss history after appends:", loss_history)

# insert(): Adds element at specific index
loss_history.insert(1, 0.77)  # inserts 0.77 at index 1
print("Loss history after insert:", loss_history)

# extend(): Merges another list to the end
additional_losses = [0.31, 0.22]
loss_history.extend(additional_losses)
print("Loss history after extend:", loss_history)

# remove(): Removes first occurrence of a value
loss_history.remove(0.77)
print("Loss history after remove:", loss_history)

# pop(): Removes and returns element at index (defaults to last element if index omitted)
popped_loss = loss_history.pop()  # removes 0.22
print(f"Popped loss: {popped_loss} | Remaining list: {loss_history}")

# sorting lists
loss_history.sort()  # sorts in ascending order in-place
print("Loss history sorted ascending:", loss_history)
loss_history.sort(reverse=True)  # sorts descending
print("Loss history sorted descending:", loss_history)

# ==========================================
# 3. Reference Copying vs Copying Values
# ==========================================
# Directly assigning a list to a new variable copy does NOT duplicate it. It copies the reference!

print("\n--- Copying Concepts ---")
list_original = [1, 2, 3]

# Reference Assignment
list_reference = list_original
list_reference.append(99)
print(f"Original: {list_original} (Affected because reference was modified!)")

# Shallow Copying values (creates a new list object)
list_actual_copy = list_original.copy()  # or list_original[:]
list_actual_copy.append(1000)
print(f"Original: {list_original} (Not affected by actual copy modification!)")
print(f"Copy: {list_actual_copy}")

# ==========================================
# 4. Hands-on ML Use-Case: Mini-Batch Generation
# ==========================================
# Slicing lists is a common way to split data into batches when writing dataloaders from scratch.
print("\n--- Practical ML Use-Case: Mini-Batches ---")

all_data = list(range(100, 110))  # List of numbers [100, 101, ... 109]
batch_size = 3

print(f"Total dataset: {all_data}")
for i in range(0, len(all_data), batch_size):
    batch = all_data[i : i + batch_size]
    print(f"  Batch starting at index {i}: {batch}")

"""
Key Takeaways:
- Lists are ordered, mutable, dynamic sequences.
- Negative indexing is a convenient way to access elements from the end (e.g. -1 is last, -2 is second last).
- Slicing creates a new list copy containing the selected elements.
- Reassigning list variables `b = a` copies only the memory reference. Use `.copy()` or `a[:]` for a value copy.

Interview Relevance:
- What is the difference between append() and extend()? (append adds the object as a single element; extend merges the elements of the iterable).
- What is the time complexity of inserting or popping elements from the middle of a list? (O(N) because elements have to be shifted in memory. Popping from the end is O(1)).
- Explain list copying (Shallow Copy vs Deep Copy).

AI/ML Relevance:
- Storing logs: Accuracy, loss, precision, recall values computed across epochs are stored in lists to plot trends using Matplotlib.
- Feature subsets: Selecting combinations of features for cross-validation subsets is done via list indexing and slicing.
"""
