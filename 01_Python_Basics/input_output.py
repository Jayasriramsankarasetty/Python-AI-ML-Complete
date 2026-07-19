"""
Topic:
Input and Output (I/O) Operations in Python

Importance:
I/O operations are the bridge between the program and the external environment.
F-strings are industry-standard for formatting logs, printing model stats, and generating files dynamically.
Taking interactive user inputs is helpful for configuring lightweight scripts or terminal-based tools.

This file covers:
- Output printing with print()
- Specifying custom separators (sep) and line ends (end)
- Formatting outputs using f-strings (f"...")
- Reading interactive user inputs with input()
"""

# ==========================================
# 1. Standard Output with print()
# ==========================================
# Simple prints
print("--- Standard Output ---")
print("Hello World!")
print("Model training started...")

# Multiple values in print
# By default, arguments are separated by a space
print("Loss:", 0.435, "Accuracy:", 0.89)

# ==========================================
# 2. Custom Separator (sep) and End (end)
# ==========================================
# 'sep' specifies what goes between multiple arguments (default is ' ')
# 'end' specifies what prints at the very end of the statement (default is '\n')

print("\n--- Custom Separator and End ---")
# Example of formatting a date or path prefix
print("2026", "07", "19", sep="-")
print("path", "to", "dataset", "data.csv", sep="/")

# Changing the end parameter is useful for status bars or single-line updates
print("Loading model weights...", end=" ")
# The next print continues on the same line
print("Done!")

# ==========================================
# 3. String Formatting with F-Strings (Python 3.6+)
# ==========================================
# F-strings (formatted string literals) make it extremely clean to insert variables into strings.
# They are fast, readable, and support direct evaluations inside curly braces.
print("\n--- F-Strings Formatting ---")
model = "NeuralNetwork"
epoch = 5
loss = 0.023456
val_accuracy = 0.9452

# Basic interpolation
print(f"Model {model} is currently training.")

# Formatting float precision (e.g. limiting loss to 4 decimal places)
print(f"Epoch: {epoch} | Loss: {loss:.4f} | Val Accuracy: {val_accuracy:.2%}")

# Expressions inside f-strings
print(f"Total training runtime projection (for 100 epochs): {100 * 0.5} seconds")

# ==========================================
# 4. Reading Input with input()
# ==========================================
# The input() function always reads the input as a string.
print("\n--- Interactive User Input ---")

# Let's prompt for simulated configuration (since scripts running automatically might freeze on input(),
# we use pre-defined fallback check values if needed, but we demonstrate the standard code)
user_name = input("Enter your name (Default: Candidate): ") or "Candidate"
selected_model = input("Enter model to run (e.g., LogisticRegression/SVM): ") or "LogisticRegression"

# Let's display the input back using f-string
print(f"Hello, {user_name}! We will run the {selected_model} model for you.")

# Input type conversion (input is always read as string!)
# If we need numeric input, we must explicitly convert it (Typecasting, which is explored next in detail)
epochs_input = input("Enter number of training epochs (Default: 50): ") or "50"
epochs_int = int(epochs_input)  # Converting string to integer
print(f"Configured training for {epochs_int} epochs. Next epoch value will be: {epochs_int + 1}")

"""
Key Takeaways:
- print() defaults to separating variables by space and ending with a newline.
- 'sep' and 'end' parameters give granular control over how text is printed.
- F-strings (`f"..."`) allow clean expression evaluation and string interpolation, with easy formatting (e.g. `.4f` or `:.2%`).
- input() reads inputs dynamically from standard input ALWAYS as a string.

Interview Relevance:
- Explain what f-strings are and why they are preferred over older format methods like `%` or `.format()`.
- How can you print a message without a newline? (Use `end=""` or `end=" "`).
- What datatype does `input()` return? (Always `str`).

AI/ML Relevance:
- Epoch progress logs: All major libraries (TensorFlow, PyTorch, Hugging Face) write custom output formatting to show loss and accuracy trends per epoch.
- When loading dataset text dynamically, you'll format folder names using f-strings, e.g. `f"data/splits/train_{epoch}.csv"`.
"""
