# Python Interview Questions & Answers (Top 15)

This document contains 15 advanced Python interview questions frequently asked during technical placement screenings.

---

### Q1: What is the Global Interpreter Lock (GIL) and how does it affect multi-threaded applications in Python?
* **Answer**: The GIL is a mutex (mutual exclusion lock) that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once.
* **Implication**: Python multi-threading is concurrency but NOT true parallelism. For CPU-bound tasks, multi-threading will not yield performance improvements (and can even slow down due to lock overhead). To achieve parallelism, developers use multiprocessing (which spawns separate OS processes with individual memory space and GIL instances) or write extensions in C/C++.

---

### Q2: Explain the difference between Deep Copy and Shallow Copy.
* **Answer**: 
  * **Shallow Copy**: Creates a new object, but inserts references to the original nested objects. Modifying a mutable nested object inside the copy alters the original object as well. (Created via `copy.copy()`).
  * **Deep Copy**: Recursively copies both the parent object and all nested objects inside it. Modifying the copy has zero impact on the original. (Created via `copy.deepcopy()`).

---

### Q3: What are Python Generators and why are they memory efficient?
* **Answer**: Generators are functions that return an iterator using the `yield` keyword instead of `return`. 
* **Implication**: Unlike regular functions that compute the entire list of values in memory and return it at once, generators yield one element at a time on demand (lazy evaluation). This keeps memory consumption constant (O(1)) even when working with infinite streams or multi-gigabyte data files.

---

### Q4: How does memory management work in Python?
* **Answer**: Python uses two primary mechanisms:
  1. **Reference Counting**: Every Python object tracks how many references point to it. When an object's reference count drops to 0, its memory is immediately deallocated.
  2. **Generational Garbage Collector (GC)**: Reference counting alone cannot detect circular references (e.g. Object A points to Object B, and Object B points back to Object A). Python's GC detects circular reference loops by periodically traversing objects across three generational cycles (Gen 0, Gen 1, Gen 2).

---

### Q5: What is Duck Typing?
* **Answer**: Duck Typing is a programming concept associated with dynamic typing, summarized by the phrase: *"If it walks like a duck and quacks like a duck, it's a duck."*
* **Implication**: In Python, we do not verify the exact class type of an object before invoking a method. We simply invoke the method. If the object implements the interface, Python executes it. For example, if an object implements the `__iter__` method, it can be looped over, regardless of whether it inherits from `list` or `dict`.

---

### Q6: What are Decorators and how do you write a custom one?
* **Answer**: A decorator is a function that takes another function as an argument, extends its behavior without modifying its source code, and returns the wrapper function.
* **Example**:
  ```python
  def my_decorator(func):
      def wrapper(*args, **kwargs):
          print("Before function execution")
          result = func(*args, **kwargs)
          print("After function execution")
          return result
      return wrapper
  ```

---

### Q7: Explain `*args` and `**kwargs` in function signatures.
* **Answer**: 
  * `*args`: Collects positional arguments as a tuple.
  * `**kwargs`: Collects keyword arguments as a dictionary.
* **Implication**: Allows functions to accept variable numbers of arguments, facilitating flexible interface designs and decorator wrappers.

---

### Q8: What is the difference between `list` and `tuple`?
* **Answer**: 
  * **List**: Mutable, dynamically sized, and consumes slightly more memory (pre-allocates extra space).
  * **Tuple**: Immutable, fixed size, and consumes less memory. Tuples can be used as keys in dictionaries (since they are hashable), whereas lists cannot.

---

### Q9: What are Metaclasses?
* **Answer**: A metaclass is the class of a class. It defines how a class behaves. Just as an object is an instance of a class, a class in Python is an instance of a metaclass (by default, `type`). Metaclasses are used to intercept class creation, validate inheritance rules, or auto-register classes.

---

### Q10: How do you handle exceptions in Python and what is the role of `finally`?
* **Answer**: Exceptions are handled using `try`, `except`, `else`, and `finally` blocks:
  * `try`: The code block that might raise an error.
  * `except`: Captures and handles the exception.
  * `else`: Executes if no exceptions were raised.
  * `finally`: Executed under all circumstances (whether an exception was raised, caught, or unhandled). Typically used for resource cleanups (closing database connections or file streams).

---

### Q11: Explain list comprehensions and dict comprehensions.
* **Answer**: Syntactic sugar to construct lists and dictionaries from iterables in a single line.
* **Example**:
  ```python
  squares = [x**2 for x in range(10)]
  square_dict = {x: x**2 for x in range(5)}
  ```

---

### Q12: What is the difference between `is` and `==`?
* **Answer**: 
  * `==` checks for **value equality**: returns True if the values of the two variables are equal.
  * `is` checks for **identity equality**: returns True only if both variables point to the exact same object address in memory (`id(a) == id(b)`).

---

### Q13: Explain Namespace and Scope resolution (LEGB rule) in Python.
* **Answer**: Scope resolution follows the LEGB hierarchy:
  1. **L (Local)**: Defined inside the current active function.
  2. **E (Enclosing)**: Defined inside nested/outer parent functions.
  3. **G (Global)**: Defined at the module level.
  4. **B (Built-in)**: Names pre-loaded by Python (e.g. `print`, `len`).

---

### Q14: What is the difference between `__str__` and `__repr__`?
* **Answer**:
  * `__str__`: Returns an easy-to-read, user-friendly string representation of an object (called by `print()`).
  * `__repr__`: Returns an unambiguous, developer-friendly string representation of an object (typically displays class name and memory address, ideally representing valid python code to recreate the object).

---

### Q15: What is Method Resolution Order (MRO) in Python?
* **Answer**: MRO is the order in which Python searches for inherited methods in a class hierarchy when using multiple inheritance. Python uses the **C3 Linearization** algorithm to determine MRO, which preserves local precedence order and monotonicity. MRO can be inspected on any class using the `__mro__` attribute or `mro()` method.
