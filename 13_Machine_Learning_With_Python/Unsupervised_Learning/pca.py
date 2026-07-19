"""
Topic:
Unsupervised Learning - Principal Component Analysis (PCA)

Importance:
PCA is the standard linear dimensionality reduction technique.
It projects high-dimensional datasets containing hundreds of features onto a lower-dimensional
orthogonal space (principal components) that maximizes variance representation. This speeds up
training and eliminates collinearity.

This file covers:
- Algorithm Explanation & When to use
- Seeding a highly correlated, multi-dimensional dataset
- Preprocessing (Z-Score Standardization - mandatory)
- Fitting the PCA model
- Transforming/projecting columns onto Principal Components
- Evaluating explained variance ratios and cumulative sums
- Interpretation of components loadings weights
"""

# ==========================================
# 1. Algorithm Explanation & When to use
# ==========================================
# Principal Component Analysis (PCA) performs an orthogonal coordinate transformation:
#   1. Centers the dataset by subtracting the mean of each feature.
#   2. Calculates the Covariance Matrix of the features.
#   3. Calculates the Eigenvalues and Eigenvectors of the covariance matrix.
#   4. Eigenvectors define the directions of new axes (Principal Components).
#      - First Principal Component (PC1) points in the direction of maximum data variance.
#      - Second Principal Component (PC2) is orthogonal (90 degrees) to PC1, capturing the next highest variance.
#   5. Eigenvalues indicate the amount of variance captured by each component.
#
# When to use:
# - You have too many features (high dimensionality), causing models to train slowly.
# - Independent variables are highly correlated (multicollinearity).
# - You want to visualize high-dimensional data in 2D or 3D plots.

# ==========================================
# 2. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# ==========================================
# 3. Load/Create Dataset
# ==========================================
# Scenario: House features. Many columns are highly correlated.
# Features: Sq_Footage, Rooms_Count, Bathrooms_Count, Annual_Tax, and Age.
np.random.seed(42)
n_samples = 100

sq_footage = np.random.normal(2000, 400, n_samples)
rooms = sq_footage / 400.0 + np.random.normal(0, 0.5, n_samples)
bathrooms = rooms * 0.5 + np.random.normal(0, 0.2, n_samples)
taxes = sq_footage * 1.5 + np.random.normal(0, 100, n_samples)
age = np.random.uniform(5, 50, n_samples)  # independent age feature

df = pd.DataFrame({
    "sq_footage": sq_footage,
    "rooms": rooms,
    "bathrooms": bathrooms,
    "taxes": taxes,
    "age": age
})
X = df.copy()

print("=======================================")
print("Original Dataset Features (first 3 rows):")
print("=======================================")
print(X.head(3))

# ==========================================
# 4. Preprocessing
# ==========================================
# CRITICAL: Standardization is mandatory for PCA.
# If features are not scaled, variables with the largest raw numerical ranges (taxes)
# will dominate variance measurements, aligning components artificially to that single feature.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================================
# 5. Train Model
# ==========================================
# We initialize PCA. Without specifying n_components, it keeps all components (n_components = features count)
# to evaluate cumulative explained variance.
pca = PCA()
pca.fit(X_scaled)

# ==========================================
# 6. Transform
# ==========================================
# Project original scaled features onto the new principal components axes
X_pca = pca.transform(X_scaled)
df_pca = pd.DataFrame(X_pca, columns=[f"PC{i+1}" for i in range(X.shape[1])])

# ==========================================
# 7. Evaluate
# ==========================================
# Explained Variance Ratio indicates the proportion of total variance captured by each component.
explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

print("\n=======================================")
print("PCA Explained Variance Metrics:")
print("=======================================")
for idx, var in enumerate(explained_variance):
    print(f"Principal Component PC{idx+1} explained variance: {var:.4f} (Cumulative: {cumulative_variance[idx]:.4f})")
print("=======================================")

# ==========================================
# 8. Simple Interpretation & Conclusion
# ==========================================
# Check feature loadings (weights of original features in first principal component)
loadings = pd.DataFrame(
    pca.components_.T,
    columns=[f"PC{i+1}" for i in range(X.shape[1])],
    index=X.columns
)

print("\n--- Component Loadings (Weights) ---")
print(loadings[["PC1", "PC2"]])

print("\n--- Interpretation ---")
print(f"1. PC1 alone explains {explained_variance[0]*100:.1f}% of the total dataset variance.")
print(f"2. Cumulative variance of PC1 and PC2 is {cumulative_variance[1]*100:.1f}%.")
print("   This means we can compress our 5 features into just 2 dimensions while preserving")
print(f"   {cumulative_variance[1]*100:.1f}% of all information, eliminating 60% of columns.")
print("3. Looking at PC1 loadings: sq_footage, rooms, bathrooms, and taxes have high positive weights (~0.5).")
print("   This means PC1 represents 'House Size and Cost'. PC2 has a high weight on 'age' (~0.95),")
print("   representing the independent dimension of 'House Age'.")
print("=======================================")

"""
Key Takeaways:
- PCA is a variance-maximization linear transformation.
- Feature scaling is mandatory to prevent large-magnitude features from dominating components.
- Explained variance ratios help determine the number of dimensions to keep (typically keeping components that capture 90%+ cumulative variance).

Interview Relevance:
- Why must we standardize features before applying PCA? (If features are on different scales, PCA will align its first component with the feature that has the largest variance/scale, ignoring others).
- What are eigenvalues and eigenvectors in the context of PCA? (Eigenvectors represent the directions of the principal components; eigenvalues represent the magnitude of variance captured along those directions).
- How do you select the number of principal components to retain? (Use the Scree Plot: plot eigenvalues vs components index and find the elbow point. Alternatively, set a threshold for cumulative explained variance, e.g. retaining components that cover 90% or 95% of total variance).

AI/ML Relevance:
- Multicollinearity: PCA creates orthogonal (uncorrelated) components, making it a perfect preprocessing step before running Linear/Logistic regression.
- Compute Speed: Squeezing 100 features down to 10 principal components speeds up model training times in production pipelines.
"""
