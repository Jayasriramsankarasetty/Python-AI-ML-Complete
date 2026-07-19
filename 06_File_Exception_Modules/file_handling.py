"""
Topic:
File Handling in Python

Importance:
Loading raw data inputs (CSVs, JSONs, TXTs) and saving results (checkpoints, metrics, logs)
is the first step of any data science pipeline. Using standard context managers protects 
resource allocations.

This file covers:
- Opening and closing files safely
- Reading from a text file (read(), readline(), readlines())
- Writing and appending to files ('w', 'a' modes)
- The context manager ('with' keyword)
- Practical ML application: Writing training logs and reading simple mock CSV values
"""

# ==========================================
# 1. Writing to a File
# ==========================================
# 'w' mode opens a file for writing (overwrites if it exists).
# 'a' mode appends to the file.
# The 'with' keyword acts as a context manager, closing the file automatically when the block exits.

print("--- Writing and Appending Files ---")
log_filepath = "training_logs.txt"

# Writing a clean log file
with open(log_filepath, "w") as file:
    file.write("Epoch,Loss,Accuracy\n")  # Header
    file.write("1,0.543,0.812\n")
    file.write("2,0.321,0.884\n")

print(f"Log header and first epochs written to: '{log_filepath}'")

# Appending a new epoch log to the end
with open(log_filepath, "a") as file:
    file.write("3,0.187,0.932\n")

print(f"Epoch 3 appended to: '{log_filepath}'")

# ==========================================
# 2. Reading from a File
# ==========================================
# 'r' mode opens file for reading (default mode).

print("\n--- Reading Files (Methods) ---")

# Method A: read() - reads the entire file as a single string
with open(log_filepath, "r") as file:
    entire_content = file.read()
print("A. Read entire file:\n", entire_content)

# Method B: readlines() - reads all lines into a list of strings
with open(log_filepath, "r") as file:
    lines = file.readlines()
print("B. Read lines as list:", lines)

# Method C: Line-by-line loop (Memory-efficient for huge datasets)
print("C. Iterating line-by-line:")
with open(log_filepath, "r") as file:
    for line in file:
        # strip() removes trailing newline \n
        print("  Line:", line.strip())

# ==========================================
# 3. Hands-on ML Use-Case: Mock CSV Parsing
# ==========================================
# We will create a small CSV dataset file and parse its contents to calculate average columns.
print("\n--- Practical ML Use-Case: CSV Parsing ---")

csv_filepath = "mock_dataset.csv"
dataset_content = """size,price
1500,300000
2000,400000
1200,250000
1800,360000
"""

# Save the dataset
with open(csv_filepath, "w") as file:
    file.write(dataset_content)

# Read and parse values
sizes = []
prices = []

with open(csv_filepath, "r") as file:
    # Read the header line first to skip it
    header = file.readline()
    
    # Iterate through data rows
    for line in file:
        # Split row by comma
        row = line.strip().split(",")
        if len(row) == 2:
            # Cast raw string numbers to numerical types
            sizes.append(float(row[0]))
            prices.append(float(row[1]))

print("Parsed Sizes list:", sizes)
print("Parsed Prices list:", prices)

# Simple analysis calculations
avg_size = sum(sizes) / len(sizes)
avg_price = sum(prices) / len(prices)
print(f"Average Housing Size: {avg_size:.2f} sqft")
print(f"Average Housing Price: ${avg_price:.2f}")

# Cleanup generated files (standard practice is handled by os module, but we leave the files for inspection)

"""
Key Takeaways:
- Always use the `with` statement to open files. It guarantees the file is closed, preventing memory leaks.
- 'w' mode overwrites; 'a' mode appends; 'r' mode reads.
- Iterating directly over the file object `for line in file:` is memory-efficient because it reads line-by-line instead of loading the whole file into RAM.

Interview Relevance:
- Why is it preferred to use the `with` statement when opening files? (It ensures proper cleanup/closing of the file stream even if exceptions are raised inside the block).
- What is the difference between `.read()`, `.readline()`, and `.readlines()`?
- How do you append text to a file without overwriting it? (Open with mode='a').

AI/ML Relevance:
- Custom parser loops: While libraries like Pandas (`pd.read_csv`) are standard, writing raw python parser loops is critical when reading massive log files or cleaning custom text datasets line-by-line.
- Training tracking: ML training loops dump epoch metrics, evaluation scores, and model parameter flags into text logs periodically for auditability.
"""
