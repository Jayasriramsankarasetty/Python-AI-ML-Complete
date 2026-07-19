# Unsupervised Learning Algorithms

Unsupervised Learning algorithms analyze datasets containing input features without target labels. The model identifies structural associations, clusters samples together, or reduces feature dimension sizes.

---

## Folder Contents

This sub-folder contains detailed algorithm implementations:

1. [kmeans.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Unsupervised_Learning/kmeans.py):
   * Partitions data points into K clusters by minimizing within-cluster distance variances.
2. [hierarchical_clustering.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Unsupervised_Learning/hierarchical_clustering.py):
   * Connects closest nodes recursively to build cluster hierarchies (Agglomerative).
3. [pca.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Unsupervised_Learning/pca.py):
   * Projects high-dimensional feature systems onto orthogonal directions maximizing explained variance.

---

## Coding Format Rules for Unsupervised Files

Every file includes:
1. **Algorithm Explanation** in comments.
2. **When to use** guidelines.
3. **Dataset Seeding** example.
4. **Data preprocessing** structures (scaling).
5. **Model training** fit step.
6. **Prediction/Transform** cluster predictions or dimension outputs.
7. **Evaluation metrics** print checks (Inertia, Silhouette score, or Explained Variance).
8. **Simple Interpretation** of outputs.
