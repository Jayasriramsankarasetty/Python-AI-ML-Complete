"""
Topic:
Unsupervised Learning - Hierarchical Clustering (Agglomerative)

Importance:
Hierarchical clustering builds a tree-like hierarchy of clusters.
Unlike K-Means, it does not require pre-specifying the number of clusters (K) upfront,
allowing engineers to analyze relationships at different granularities.

This file covers:
- Algorithm Explanation & When to use
- Seeding a numeric clustering dataset
- Preprocessing (Standardization)
- Fitting the AgglomerativeClustering model
- Calculating linkage matrices and plotting dendrogram structures (in comments/console logs)
- Evaluating using Silhouette Score
- Interpretation of dendrogram boundaries
"""

# ==========================================
# 1. Algorithm Explanation & When to use
# ==========================================
# Hierarchical clustering is structured either as:
#   - Divisive (Top-down): Start with one big cluster, split recursively.
#   - Agglomerative (Bottom-up): Start with each point as a separate cluster,
#     merge the closest pairs recursively until one single cluster remains.
# Distance between clusters is defined by Linkages:
#   - Ward Linkage: Minimizes variance increase in merged clusters.
#   - Single Linkage: Distance between closest points of two clusters.
#   - Complete Linkage: Distance between furthest points of two clusters.
#   - Average Linkage: Average distance between all points of two clusters.
# Results are visualized as a Dendrogram (tree diagram showing merge distances).
#
# When to use:
# - You need a visual tree showing hierarchical nested groups.
# - You do not want to predefine the number of clusters.
# - The dataset size is relatively small (Hierarchical clustering has O(N³) complexity).

# ==========================================
# 2. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

# ==========================================
# 3. Load/Create Dataset
# ==========================================
# Scenario: Customer Segment grouping
np.random.seed(42)
n_samples = 60

# Seeding three tiny clusters
cluster_A = np.random.normal(loc=[2, 2], scale=0.5, size=(20, 2))
cluster_B = np.random.normal(loc=[8, 8], scale=0.5, size=(20, 2))
cluster_C = np.random.normal(loc=[5, 12], scale=0.5, size=(20, 2))

X_raw = np.concatenate([cluster_A, cluster_B, cluster_C])
df = pd.DataFrame(X_raw, columns=["metric_1", "metric_2"])

# ==========================================
# 4. Preprocessing
# ==========================================
# Standarize features since linkage uses Euclidean distance calculations
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# ==========================================
# 5. Train Model
# ==========================================
# AgglomerativeClustering with ward linkage, setting n_clusters=3
model = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="ward")
labels = model.fit_predict(X_scaled)
df["cluster"] = labels

# ==========================================
# 6. Linkage Matrix (for Dendrogram calculation)
# ==========================================
# linkage calculates the hierarchical tree merges matrix
linkage_matrix = linkage(X_scaled, method="ward")

# ==========================================
# 7. Evaluate
# ==========================================
sil_score = silhouette_score(X_scaled, labels)

print("=======================================")
print("Hierarchical Clustering Evaluation:")
print("=======================================")
print(f"Number of leaf nodes:          {model.n_leaves_}")
print(f"Silhouette Score (k=3):        {sil_score:.4f}")
print("=======================================")

# Print first 5 steps of the linkage merge matrix
# Columns: [Node index A, Node index B, Distance between them, Sample count in new cluster]
print("\n--- First 5 cluster merge steps in linkage matrix: ---")
print(linkage_matrix[:5])

# ==========================================
# 8. Simple Interpretation & Conclusion
# ==========================================
print("\n--- Interpretation ---")
print(f"1. Silhouette Score of {sil_score:.4f} highlights solid separations between clusters.")
print("2. The linkage matrix shows merging steps. For instance, step 1 merged two samples")
print(f"   at a distance of {linkage_matrix[0][2]:.4f} to create a cluster containing {int(linkage_matrix[0][3])} points.")
print("=======================================")

"""
Key Takeaways:
- Agglomerative clustering merges closest pairs bottom-up based on linkage rules.
- Dendrogram cuts at a threshold distance height define the active number of clusters.
- O(N³) time and O(N²) space complexity makes it unsuitable for large-scale production.

Interview Relevance:
- Explain the difference between K-Means and Hierarchical Clustering. (K-Means is flat, requires predefining K, has O(N) complexity, and is suited for large data; Hierarchical is tree-structured, doesn't require predefining K, has O(N³) complexity, and is suited for smaller datasets).
- What are the common linkage criteria? (Ward: minimizes variance within clusters; Single: uses closest point distance; Complete: uses furthest point distance; Average: uses mean pair distance).
- How do you select the number of clusters from a dendrogram? (Draw a horizontal cut line across the dendrogram's tallest vertical lines that don't cross any merge nodes; the number of vertical lines crossed equals the number of clusters).

AI/ML Relevance:
- Taxonomy Construction: Used to group biological species, topics, or products into structured hierarchies.
- Social Networks: Grouping communities or sub-networks into nested cohort circles.
"""
