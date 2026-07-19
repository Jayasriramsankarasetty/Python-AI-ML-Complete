"""
Topic:
Strings and Basic Text Preprocessing

Importance:
Strings are ordered sequences of Unicode characters. Unlike lists, strings are immutable.
In AI/ML, strings are the input format for all Natural Language Processing (NLP) models.
Text cleaning (normalization, whitespace stripping, word tokenization) relies on string methods.

This file covers:
- String creation, indexing, and slicing
- Immutability of strings
- Core string methods: split(), join(), strip(), replace(), lower(), upper(), find()
- Practical NLP application: Cleaning raw conversational chatbot text
"""

# ==========================================
# 1. Indexing, Slicing & Immutability
# ==========================================
# Strings can be wrapped in single, double, or triple quotes.

print("--- String Basics & Slicing ---")
sample_text = "Natural Language Processing"

# Indexing
print("Character at index 0:", sample_text[0])
print("Last character:", sample_text[-1])

# Slicing: text[start:stop:step]
print("Slice 'Natural':", sample_text[:7])
print("Slice 'Language':", sample_text[8:16])
print("Reverse the string:", sample_text[::-1])

# Immutability
# Attempting to assign a character will raise a TypeError:
# sample_text[0] = "n"

# ==========================================
# 2. Essential String Methods
# ==========================================
print("\n--- String Methods ---")

# lower() and upper()
print("Lowercase:", sample_text.lower())
print("Uppercase:", sample_text.upper())

# strip(): Removes leading and trailing whitespace (or other custom characters)
dirty_input = "   Acc: 0.925 \n"
clean_input = dirty_input.strip()
print(f"Original dirty string: '{dirty_input}'")
print(f"Stripped string: '{clean_input}'")

# replace(old, new)
replaced_text = sample_text.replace("Natural", "Artificial")
print(f"Replaced text: {replaced_text}")

# split(separator): splits string into a list of substrings
sentence = "deep-learning-is-powerful"
tokens_list = sentence.split("-")
print(f"Split list: {tokens_list}")

# join(iterable): merges list elements into a single string
joined_sentence = " ".join(tokens_list)
print(f"Joined with spaces: '{joined_sentence}'")

# find(substring): returns first index location of substring, or -1 if missing
print("Location of 'Language':", sample_text.find("Language"))
print("Location of 'CV':", sample_text.find("CV"))

# ==========================================
# 3. Practical NLP Use-Case: Text Preprocessing
# ==========================================
# NLP pipelines clean sentences before tokenizing them into models.
print("\n--- Practical NLP Text Cleaning Pipeline ---")

raw_tweets = [
    "  #MachineLearning is AWESOME!   ",
    "NLP is a branch of AI...  ",
    "  data science and deep learning   "
]

def preprocess_text(text):
    """
    Cleans a text input by:
    1. Lowercasing characters
    2. Stripping whitespace
    3. Replacing specific symbols
    4. Splitting into tokens
    """
    # Step 1: Lowercase
    cleaned = text.lower()
    
    # Step 2: Strip whitespaces
    cleaned = cleaned.strip()
    
    # Step 3: Replace hashtags or punctuation (simple demo)
    cleaned = cleaned.replace("#", "")
    cleaned = cleaned.replace("!", "")
    cleaned = cleaned.replace(".", "")
    
    # Step 4: Tokenize (split by space)
    tokens = cleaned.split()
    return tokens

print("Executing cleaning pipeline:")
for tweet in raw_tweets:
    processed_tokens = preprocess_text(tweet)
    print(f"Raw: '{tweet}' -> Tokens: {processed_tokens}")

"""
Key Takeaways:
- Strings are immutable. Methods like `.replace()` or `.lower()` return a NEW string.
- Slicing syntax works identically to lists (`[start:stop:step]`).
- `.split()` is used to break text down into tokens; `.join()` reconstructs strings from sequences.

Interview Relevance:
- Why are strings immutable in Python? (Immutability makes strings hashable so they can be keys in dicts, and ensures reference safety in memory optimization).
- How do you reverse a string in a Pythonic way? (Using slicing: `text[::-1]`).
- What is the difference between `.find()` and `.index()`? (Both search for a substring, but `.find()` returns -1 if missing while `.index()` raises a ValueError).

AI/ML Relevance:
- Tokenization: Before training text architectures (like BERT or GPT), raw sentences are cleaned and split into lists of words/tokens using string operations.
- Regex and Strings: Clean parsing of dataset files (like CSVs or log files) requires text cleaning via string replacements and splitting.
"""
