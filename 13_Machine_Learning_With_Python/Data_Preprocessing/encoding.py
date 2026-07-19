"""
Topic:
Data Preprocessing - Categorical Encoding (One-Hot & Ordinal Encoding)

Importance:
Machine Learning algorithms deal strictly with numbers. Categorical features
(like colors, departments, education levels) must be mapped to numeric matrices.
Using scikit-learn's OneHotEncoder (for nominal variables) and OrdinalEncoder (for ordered classes)
maintains structured mathematical shapes.

This file covers:
- Setting up nominal (unordered) and ordinal (ordered) categorical features
- Implementing OneHotEncoder with binary sparse matrix conversions
- Implementing OrdinalEncoder with predefined rank mappings
- Converting encoded output matrices back to DataFrames
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

# ==========================================
# 1. Setup Mock Categorical Dataset
# ==========================================
# Nominal feature: "city" (New York, Los Angeles, Chicago - unordered)
# Ordinal feature: "edu_level" (High School, Bachelor, Master, PhD - ordered rank)
raw_data = {
    "employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "city": ["New York", "Los Angeles", "Chicago", "New York", "Los Angeles"],
    "edu_level": ["Master", "High School", "Bachelor", "PhD", "Bachelor"]
}

df = pd.DataFrame(raw_data)
print("=======================================")
print("Original Categorical DataFrame:")
print("=======================================")
print(df)

# ==========================================
# 2. Nominal Encoding: OneHotEncoder
# ==========================================
print("\n--- 1. Nominal Encoding (One-Hot Encoding) ---")
# sparse_output=False returns a dense numpy array directly instead of a sparse matrix
# handle_unknown='ignore' prevents errors when testing on unseen categories in production
ohe = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
encoded_city_array = ohe.fit_transform(df[["city"]])

# Create a DataFrame containing the binary column representations
# get_feature_names_out gets the generated category headings: ['city_Chicago', 'city_Los Angeles', ...]
city_cols = ohe.get_feature_names_out(["city"])
df_ohe_city = pd.DataFrame(encoded_city_array, columns=city_cols)

print("One-Hot Encoded City columns:")
print(df_ohe_city)

# ==========================================
# 3. Ordinal Encoding: OrdinalEncoder
# ==========================================
print("\n--- 2. Ordinal Encoding (OrdinalEncoder) ---")
# Define the order mapping structure from lowest level to highest level
edu_categories = [["High School", "Bachelor", "Master", "PhD"]]

ord_encoder = OrdinalEncoder(categories=edu_categories)
df["edu_encoded"] = ord_encoder.fit_transform(df[["edu_level"]])

print("DataFrame after Ordinal Encoding:")
print(df[["employee", "edu_level", "edu_encoded"]])

# ==========================================
# 4. Final Merged Output Dataset
# ==========================================
print("\n=======================================")
print("Final Encoded Dataset for training:")
print("=======================================")
# Concatenate the original identifiers, the ordinal code, and the OHE features
df_final = pd.concat([df[["employee", "edu_encoded"]], df_ohe_city], axis=1)
print(df_final)
print("=======================================")

"""
Key Takeaways:
- Nominal columns (unordered labels) require One-Hot Encoding, creating binary columns.
- Ordinal columns (ordered labels) use OrdinalEncoder with predefined sequence maps.
- Avoid treating nominal attributes as ordinal values, as it implies false order relationships.

Interview Relevance:
- What is the Dummy Variable Trap? (A scenario where multi-collinearity exists due to one-hot columns being highly correlated. If we have N categories, we can represent them using N-1 columns. The remaining column can be dropped using `drop='first'` in scikit-learn).
- When would you use Ordinal Encoding instead of One-Hot Encoding? (Use Ordinal Encoding when the variable has a logical order, like education level or survey answers, or when One-Hot Encoding would create too many columns, causing the curse of dimensionality).
- What is Target Encoding? (A technique where categories are replaced by the mean target label value for that category. It is highly effective but risks overfitting/data leakage if not regularized).

AI/ML Relevance:
- Linear Models: Multi-collinearity from one-hot columns inflates weight variances. Use `drop='first'` to prevent standard regression inflation errors.
- Deep Learning: High-cardinality features (like zip codes) create thousands of columns. Using embeddings or target encoding is preferred to limit computational overhead.
"""
