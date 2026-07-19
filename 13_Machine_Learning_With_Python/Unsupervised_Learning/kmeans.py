"""
Topic:
Unsupervised Learning - K-Means Clustering

Importance:
K-Means is the standard baseline clustering algorithm.
It partitions unstructured data points (e.g. market customer segmentation)
into homogeneous groups to analyze cohort characteristics.

This file covers:
- Algorithm Explanation & When to use
- Seeding a multi-cluster dataset
- Preprocessing (Standardization)
- Fitting the KMeans model
- Predicting cluster labels
- Evaluating performance using Inertia and Silhouette Score
- Interpretation and Elbow rule
"""

# ==========================================
# 1. Algorithm Explanation & When to use
# ==========================================
# K-Means clustering partitions a dataset into 'K' distinct, non-overlapping subgroups.
# Process:
#   1. Initialize K random centroids.
#   2. Assign: Assign each data point to its closest centroid (Euclidean distance).
#   3. Update: Re-compute centroids as the mean of all points assigned to that cluster.
#   4. Repeat steps 2 and 3 until centroids stabilize (convergence).
# Objective: Minimize Within-Cluster Sum of Squares (Inertia).
#
# When to use:
# - Tabular dataset lacks target class labels.
# - You want to group similar samples together (customer segmentation, anomaly detection).
# - Clusters are spherical and similar in scale size.

# ==========================================
# 2. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ==========================================
# 3. Load/Create Dataset
# ==========================================
# Scenario: E-commerce customer profiling based on:
#   - Purchase Frequency (transactions per year)
#   - Average Spend per transaction ($)
np.random.seed(42)
n_samples = 150

# We simulate three distinct customer segments:
# Segment 1: Low frequency, Low spend
freq_1 = np.random.normal(5, 2, 50)
spend_1 = np.random.normal(20, 5, 50)

# Segment 2: High frequency, Medium spend
freq_2 = np.random.normal(30, 5, 50)
spend_2 = np.random.normal(50, 10, 50)

# Segment 3: Low frequency, High spend
freq_3 = np.random.normal(10, 3, 50)
spend_3 = np.random.normal(150, 20, 50)

df = pd.DataFrame({
    "frequency": np.concatenate([freq_1, freq_2, freq_3]),
    "spend": np.concatenate([spend_1, spend_2, spend_3])
})

X = df[["frequency", "spend"]]

# ==========================================
# 4. Preprocessing
# ==========================================
# CRITICAL: Feature scaling is mandatory for K-Means.
# Since it calculates Euclidean distances, features with larger ranges (spend)
# will dominate features with smaller ranges (frequency) if not scaled.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================================
# 5. Train Model
# ==========================================
# We initialize KMeans with k=3 based on our simulated setup.
# n_init='auto' defaults to 10 random centroid initializations to prevent local minimum traps.
model = KMeans(n_clusters=3, n_init="auto", random_state=42)
model.fit(X_scaled)

# ==========================================
# 6. Predict
# ==========================================
# Output predicted cluster labels (0, 1, 2)
labels = model.predict(X_scaled)
df["cluster"] = labels

# ==========================================
# 7. Evaluate
# ==========================================
# Inertia: Sum of squared distances of samples to their closest cluster center.
inertia = model.inertia_

# Silhouette Score: Measures how similar a point is to its own cluster compared to other clusters.
# Range: -1 (poor) to +1 (perfect separation).
sil_score = silhouette_score(X_scaled, labels)

print("=======================================")
print("K-Means Clustering Evaluation (k=3):")
print("=======================================")
print(f"Model Inertia (WCSS):           {inertia:.4f}")
print(f"Silhouette Score:               {sil_score:.4f}")
print("=======================================")

# ==========================================
# 8. Simple Interpretation & Conclusion
# ==========================================
print("\n--- Cluster Profile Summaries ---")
profiles = df.groupby("cluster").mean()
print(profiles)

print("\n--- Interpretation ---")
print(f"1. Silhouette Score of {sil_score:.4f} indicates a strong separation between clusters.")
print("2. Looking at the profiles:")
print("   - One cluster represents High Frequency & Medium Spend customers.")
print("   - One cluster represents Low Frequency & High Spend customers.")
print("   - One cluster represents Low Frequency & Low Spend customers.")
print("   This matches our engineered setup, proving K-Means successfully segmented customer types.")
print("=======================================")

"""
Key Takeaways:
- K-Means is a distance-based clustering algorithm requiring prior feature scaling.
- Inertia measures within-cluster compactness; Silhouette Score measures boundary separation.
- Centroid initializations (K-Means++) are used to avoid local minima traps during optimization.

Interview Relevance:
- How do you select the optimal number of clusters (K)? (Use the Elbow Method: plot Inertia vs K and look for an 'elbow' bend where inertia reduction rate slows down. Also verify using the Silhouette method).
- Why is scaling necessary for K-Means? (Because it uses Euclidean distances. Unscaled features with large numerical magnitudes dominate distance calculations).
- What are the limitations of K-Means? (Sensitive to outliers, struggles with non-spherical shapes, and requires pre-defining the number of clusters K).

AI/ML Relevance:
- Customer Profiling: Used in market analytics to group customer demographics for tailored marketing campaigns.
- Anomaly Detection: Data points located extremely far from any centroid can be flagged as anomalies or fraud patterns.
"""
