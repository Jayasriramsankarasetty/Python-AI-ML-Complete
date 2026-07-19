"""
Topic:
Iterators and Iterables in Python

Importance:
Iterators enable lazy evaluation, loading and yielding data elements one-by-one
rather than keeping entire massive datasets in RAM.
In AI/ML, data loading streams (like PyTorch Dataloader loops) rely on the iterator protocol.

This file covers:
- Iterable vs Iterator definition
- The Iterator Protocol (__iter__() and __next__() magic methods)
- Creating a custom Iterator class
- Practical ML application: Building a custom mini-batch index iterator
"""

# ==========================================
# 1. Iterable vs Iterator
# ==========================================
# - Iterable: An object that can return an iterator (defines __iter__(), e.g. Lists, Tuples, Strings).
# - Iterator: An object that maintains state to yield the next element (defines __next__() and returns self on __iter__()).

print("--- Iterable vs Iterator ---")
numbers_list = [10, 20, 30]

# Check if list is an iterator (it is NOT, it is an iterable)
print("Is list an iterator?", hasattr(numbers_list, "__next__"))  # False

# Get iterator from list using iter()
list_iterator = iter(numbers_list)
print("Is list_iterator an iterator?", hasattr(list_iterator, "__next__"))  # True

# Fetching elements using next()
print("First next():", next(list_iterator))
print("Second next():", next(list_iterator))
print("Third next():", next(list_iterator))

# Next call raises StopIteration exception because list has no more elements:
# next(list_iterator)

# ==========================================
# 2. Creating a Custom Iterator
# ==========================================
# To create an iterator:
# 1. implement __iter__() returning the iterator object itself (typically self).
# 2. implement __next__() returning the next item, or raising StopIteration when finished.

class PowerOfTwoIterator:
    """Generates powers of two up to a specified limit"""
    def __init__(self, limit):
        self.limit = limit
        self.exponent = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.exponent > self.limit:
            raise StopIteration
        
        result = 2 ** self.exponent
        self.exponent += 1
        return result

print("\n--- Testing Custom Iterator ---")
# Instantiate
powers = PowerOfTwoIterator(limit=4)

# We can iterate using next() or standard loops (loops call iter() and next() under the hood!)
for p in powers:
    print(p, end=" ")
print()

# ==========================================
# 3. Hands-on ML Use-Case: Batch Iterator
# ==========================================
# Dataloaders slice high-dimensional datasets into chunks (mini-batches) of indices recursively.
print("\n--- Practical ML Use-Case: Batch Iterator ---")

class BatchIterator:
    """
    Slices a dataset list into mini-batches of size 'batch_size'.
    """
    def __init__(self, data_list, batch_size):
        self.data = data_list
        self.batch_size = batch_size
        self.index = 0  # Track current position
        
    def __iter__(self):
        return self
        
    def __next__(self):
        # Stop condition
        if self.index >= len(self.data):
            raise StopIteration
            
        # Slice batch
        batch = self.data[self.index : self.index + self.batch_size]
        self.index += self.batch_size
        return batch

# Create raw dataset features list
mock_dataset = [f"sample_{i}" for i in range(1, 11)]  # 10 samples
batch_loader = BatchIterator(mock_dataset, batch_size=3)

# Iterate through batches
for epoch in range(1, 3):
    print(f"Epoch {epoch}:")
    # Reset loader index state for new epoch
    batch_loader.index = 0
    
    for batch_idx, batch in enumerate(batch_loader):
        print(f"  Batch {batch_idx + 1}: {batch}")

"""
Key Takeaways:
- Iterables represent lists of elements; Iterators maintain state and yield elements one-by-one.
- The Iterator Protocol consists of `__iter__()` (returns the iterator) and `__next__()` (returns the next value).
- `StopIteration` exception is raised when there are no more elements, terminating loops cleanly.

Interview Relevance:
- What is the difference between an iterable and an iterator? (Iterable has `__iter__()` returning an iterator; iterator has both `__iter__()` and `__next__()` and retains iteration state).
- What exception signals the end of an iteration? (StopIteration).
- Why do custom iterators return self on `__iter__()`? (To make the iterator itself an iterable, allowing it to be used in standard `for` loops directly).

AI/ML Relevance:
- PyTorch Dataloaders: Models train on mini-batches loaded dynamically from storage using custom PyTorch dataset iterators to avoid RAM spikes on large multi-gigabyte image folders.
- Streaming: Online learning feeds live streaming dataset points into models sequentially using active iterators.
"""
