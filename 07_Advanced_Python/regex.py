"""
Topic:
Regular Expressions (re module) in Python

Importance:
Regular Expressions (regex) allow pattern matching and text parsing.
In NLP data cleaning pipelines, regex removes html tags, usernames, punctuation,
and pulls specific values (like accuracies or percentages) from raw text logs.

This file covers:
- Python re module basics (match, search, findall, sub)
- Using raw strings (r"...") for regex patterns
- Grouping matches
- Practical ML application: Cleaning dataset labels and parsing values from training logs
"""

import re

# ==========================================
# 1. Core Regex Functions (match, search, findall)
# ==========================================
# - re.match(pattern, string): checks for a match ONLY at the beginning of the string.
# - re.search(pattern, string): scans the string for a match anywhere, returning a match object.
# - re.findall(pattern, string): returns all matches as a list of strings.

log_text = "Training epoch 45 completed. Loss: 0.245, Accuracy: 0.9125, Time: 12.4s"

print("--- Regex Functions ---")
# Match at start
match_obj = re.match(r"Training", log_text)
print("re.match results (start check):", bool(match_obj))

# Search anywhere: find accuracy decimal value
# r"\d+\.\d+" -> matches digits followed by period and digits (decimal floats)
search_obj = re.search(r"Accuracy:\s*(\d+\.\d+)", log_text)
if search_obj:
    print("re.search results (Match found):", search_obj.group(0))  # Full match
    print("re.search groups (Captured decimal):", search_obj.group(1))  # Capture group 1

# findall: find all numbers (integers or decimals)
# r"\d+\.?\d*" -> matches digits optionally followed by period and more digits
all_numbers = re.findall(r"\d+\.?\d*", log_text)
print("re.findall results (All numbers list):", all_numbers)

# ==========================================
# 2. Text Substitutions (re.sub)
# ==========================================
# re.sub(pattern, replacement, string): replaces matches in a string.

print("\n--- Regex Substitutions ---")
raw_html_tweet = "User @john_doe says: Learn #NLP with <b>Antigravity AI</b>! Visit: https://example.com"

# A. Remove HTML tags: <anything>
clean_text = re.sub(r"<[^>]+>", "", raw_html_tweet)
print("Removed HTML tags:", clean_text)

# B. Remove URLs
clean_text = re.sub(r"https?://\S+", "", clean_text)
print("Removed URLs:", clean_text)

# C. Remove Usernames (@name) and Hashtags (#tag)
# [a-zA-Z0-9_] is represented by \w (word character)
clean_text = re.sub(r"@\w+|#\w+", "", clean_text)
print("Removed usernames and hashtags:", clean_text.strip())

# ==========================================
# 3. Hands-on ML Use-Case: Log Parser
# ==========================================
# Simulating parsing structured info from raw console dumps.
print("\n--- Practical ML Use-Case: Log Parser ---")

raw_console_dump = """
[INFO] 2026-07-19 02:00:00 - Epoch 1/3 finished. val_loss=0.4501, val_acc=0.8250
[INFO] 2026-07-19 02:05:00 - Epoch 2/3 finished. val_loss=0.3120, val_acc=0.8990
[INFO] 2026-07-19 02:10:00 - Epoch 3/3 finished. val_loss=0.1985, val_acc=0.9420
"""

# Regex pattern using named capture groups to pull loss and accuracies
# (?P<name>pattern) defines a named capture group
pattern = r"Epoch\s+(?P<epoch>\d+)/\d+.*?val_loss=(?P<loss>\d+\.\d+).*?val_acc=(?P<acc>\d+\.\d+)"

print("Parsing epochs logs history:")
for match in re.finditer(pattern, raw_console_dump):
    # Retrieve named capture groups dictionary
    data = match.groupdict()
    print(f"  Parsed -> Epoch: {data['epoch']} | Loss: {float(data['loss']):.4f} | Accuracy: {float(data['acc']):.2%}")

"""
Key Takeaways:
- Always prefix regex patterns with `r` (raw string, e.g. `r"\n"`) so Python doesn't parse backslashes as escape characters.
- Use `re.search()` to find patterns anywhere in strings, and `re.findall()` to find all occurrences.
- Use named capture groups `(?P<name>...)` inside patterns to make output extraction code highly readable.

Interview Relevance:
- What is the difference between `re.match()` and `re.search()`? (`re.match()` checks only at the exact start of a string; `re.search()` scans the entire string).
- Explain the role of raw strings in Python regex. (It prevents Python from treating backslashes `\` as escape characters before passing them to the regex compiler).
- How do you replace all non-alphanumeric characters in a string using regex? (Use `re.sub(r'[^a-zA-Z0-9]', '', string)`).

AI/ML Relevance:
- NLP Preprocessing: Regex is the foundational step of tokenizers (like BERT's WordPiece) to strip punctuation, handles casing anomalies, and remove garbage characters.
- Metrics Extraction: Training frameworks parse output files from command-line scripts using regex to log metrics automatically.
"""
