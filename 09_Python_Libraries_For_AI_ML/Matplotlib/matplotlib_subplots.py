"""
Topic:
Matplotlib Subplots, Histograms, and Custom Styling

Importance:
Displaying multiple charts in a single figure grid (e.g. comparing features correlations side by side)
helps organize visual data. Histograms let us check feature distributions for skewness and norm.

This file covers:
- Histograms (frequency distributions, bin sizes)
- Subplot grids layout (`plt.subplots(2, 2)`)
- Using Matplotlib style sheets (e.g. 'ggplot', 'classic')
- Adjusting subplots overlapping (`plt.tight_layout()`)
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import numpy as np

# Apply a style theme globally (using 'ggplot' for sleek visualization aesthetics)
plt.style.use("ggplot")

# ==========================================
# 1. Histogram (Frequency distribution)
# ==========================================
print("--- Creating Histogram ---")
# Generate normal distribution data
normal_data = np.random.randn(1000)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(normal_data, bins=30, color="purple", edgecolor="white", alpha=0.7)

ax.set_title("Frequency Distribution of Feature X (Normal)", fontsize=14)
ax.set_xlabel("Value Range")
ax.set_ylabel("Frequency Count")

plt.savefig("09_Python_Libraries_For_AI_ML/Matplotlib/histogram.png")
plt.close()
print("Saved: 'histogram.png'")

# ==========================================
# 2. Subplot Grid Layout (2x2 Matrix)
# ==========================================
print("\n--- Creating 2x2 Subplot Grid ---")
x = np.linspace(0, 10, 100)

# Create 2x2 grid of subplots (returns a figure and a 2D array of axes)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Subplot 1 (Top-Left): Sine wave
axs[0, 0].plot(x, np.sin(x), color="green")
axs[0, 0].set_title("Sine Wave")

# Subplot 2 (Top-Right): Cosine wave
axs[0, 1].plot(x, np.cos(x), color="blue")
axs[0, 1].set_title("Cosine Wave")

# Subplot 3 (Bottom-Left): Tangent wave
axs[1, 0].plot(x, np.tan(x), color="darkorange")
axs[1, 0].set_title("Tangent Wave")
axs[1, 0].set_ylim(-5, 5)  # limit vertical limits because tan has asymptotes

# Subplot 4 (Bottom-Right): Exponential curve
axs[1, 1].plot(x, np.exp(x / 3), color="red")
axs[1, 1].set_title("Exponential Growth")

# Adjust padding between subplots to prevent overlapping labels and titles
plt.tight_layout()

# Save the grid figure
plt.savefig("09_Python_Libraries_For_AI_ML/Matplotlib/subplots_grid.png", dpi=150)
plt.close()
print("Saved: 'subplots_grid.png'")

"""
Key Takeaways:
- Style sheets can be applied globally using `plt.style.use()`. Common styles include `'ggplot'`, `'seaborn-v0_8-whitegrid'`, and `'classic'`.
- Histograms count value occurrence frequencies across intervals called `bins`.
- Subplot matrices are initialized via `plt.subplots(rows, cols)`, returning a nested numpy array of axes objects (e.g. `axs[row_idx, col_idx]`).
- `plt.tight_layout()` dynamically adjusts spacing bounds to prevent subplots titles overlapping axis labels.

Interview Relevance:
- How do you create multiple plots in a single figure? (Use `plt.subplots(rows, cols)` which returns a figure and an array of axes, then plot on each axis using `axs[r, c].plot()`).
- What does plt.tight_layout() do? (Automatically adjusts subplot parameters so that labels and titles do not overlap).
- How do you change style themes in Matplotlib? (Use `plt.style.use('theme_name')` globally).

AI/ML Relevance:
- Feature Skewness Check: Plotting histograms of dataset features allows machine learning engineers to see if features are normally distributed or need log transformations.
- Multi-Model Analysis: Plotting prediction results of four different models side-by-side in a 2x2 grid helps in model selection comparisons.
"""
