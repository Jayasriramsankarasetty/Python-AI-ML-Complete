# Seaborn Statistical Visualization Guide

Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. It integrates closely with Pandas DataFrames and automatically calculates statistical aggregations under the hood (like confidence intervals and distribution densities).

---

## Seaborn vs Matplotlib

| Feature | Matplotlib | Seaborn |
| :--- | :--- | :--- |
| **Abstraction Level** | Low-level. Requires manual configuration of titles, labels, colors, and line coordinates. | High-level. Single functions generate complex charts (like regressions or pairwise plots) directly from DataFrames. |
| **Default Styling** | Basic browser defaults, often requiring boilerplate customization code. | Modern default aesthetic themes (`darkgrid`, `whitegrid`, `ticks`) with curated color palettes. |
| **Statistical Calculations** | None. Data must be grouped/aggregated in NumPy/Pandas before plotting. | Computes confidence intervals, linear regressions, kernel density estimates (KDE), and bins automatically. |

---

## Files in this Folder

1. [seaborn_basics.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/09_Python_Libraries_For_AI_ML/Seaborn/seaborn_basics.py):
   * Relational plots (`scatterplot`, `lineplot`), and categorical plots (`boxplot`, `violinplot`, `countplot`) utilizing Seaborn's default themes.
2. [seaborn_advanced.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/09_Python_Libraries_For_AI_ML/Seaborn/seaborn_advanced.py):
   * Regression plots (`regplot`), correlation matrix heatmaps with text annotations, and multidimensional pairwise plots grids (`pairplot`).
