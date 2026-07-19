"""
Topic:
Matplotlib Visualization Basics

Importance:
Visualizing model metrics (like training loss over epochs) or features distributions
allows machine learning engineers to diagnose fitting states and extract insights.

This file covers:
- Non-interactive backend setup (`matplotlib.use('Agg')`)
- Line Plots (customizing lines, markers, legends)
- Scatter Plots (variable color mapping and sizing)
- Bar Charts
- Titles, labels, grids, and saving figures to file
"""

# Configure Matplotlib backend to 'Agg' BEFORE importing pyplot.
# This prevents GUI window launch errors in non-interactive terminal systems.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import numpy as np

# ==========================================
# 1. Line Plot (Loss curve example)
# ==========================================
print("--- Creating Line Plot ---")
epochs = np.arange(1, 11)
training_loss = [0.9, 0.7, 0.55, 0.45, 0.38, 0.32, 0.28, 0.25, 0.22, 0.20]
validation_loss = [0.95, 0.8, 0.62, 0.52, 0.48, 0.44, 0.42, 0.41, 0.43, 0.45]  # note overfitting at end

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# Plot lines with custom styling
ax.plot(epochs, training_loss, label="Training Loss", color="blue", linewidth=2, marker="o")
ax.plot(epochs, validation_loss, label="Validation Loss", color="red", linewidth=2, linestyle="--", marker="s")

# Customize axes labels and titles
ax.set_title("Training & Validation Loss Over Epochs", fontsize=14, fontweight="bold")
ax.set_xlabel("Epochs", fontsize=12)
ax.set_ylabel("Loss (Cross Entropy)", fontsize=12)

# Enable grid lines and legend
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(fontsize=10)

# Save to disk
plt.savefig("09_Python_Libraries_For_AI_ML/Matplotlib/line_plot_loss.png", dpi=150)
plt.close()  # close figure memory
print("Saved: 'line_plot_loss.png'")

# ==========================================
# 2. Scatter Plot (Feature distribution example)
# ==========================================
print("\n--- Creating Scatter Plot ---")
# Random feature values
x_features = np.random.randn(50)
y_features = np.random.randn(50)
# Variable size and color mappings
colors = np.random.rand(50)
sizes = 500 * np.random.rand(50)

fig, ax = plt.subplots(figsize=(8, 5))
scatter = ax.scatter(x_features, y_features, c=colors, s=sizes, alpha=0.7, cmap="viridis")

ax.set_title("Feature Dimension Distribution Mapping", fontsize=14)
ax.set_xlabel("Feature X Dimension")
ax.set_ylabel("Feature Y Dimension")
ax.grid(True, alpha=0.3)

# Add colorbar legend
fig.colorbar(scatter, ax=ax, label="Cluster Value Code")

plt.savefig("09_Python_Libraries_For_AI_ML/Matplotlib/scatter_plot.png")
plt.close()
print("Saved: 'scatter_plot.png'")

# ==========================================
# 3. Bar Chart (Category count example)
# ==========================================
print("\n--- Creating Bar Chart ---")
departments = ["HR", "IT", "Sales", "Marketing", "Finance"]
headcounts = [15, 42, 28, 12, 20]

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(departments, headcounts, color="teal", edgecolor="black", alpha=0.85)

ax.set_title("Employee Headcounts by Department", fontsize=14)
ax.set_xlabel("Departments")
ax.set_ylabel("Number of Employees")
ax.grid(axis="y", linestyle="--", alpha=0.7)  # grid only on y-axis

plt.savefig("09_Python_Libraries_For_AI_ML/Matplotlib/bar_chart.png")
plt.close()
print("Saved: 'bar_chart.png'")

"""
Key Takeaways:
- Non-interactive scripts must import `matplotlib` and set `matplotlib.use('Agg')` before importing `pyplot` to avoid GUI errors.
- Always call `plt.close()` after saving to prevent memory leaks during batch plot generation.
- Sizing and color parameters `s` and `c` in `.scatter()` allow expressing multidimensional datapoints.
- `ax.grid(axis='y')` limits grids strictly horizontally, improving bar chart scanning.

Interview Relevance:
- What is the difference between plt.show() and plt.savefig()? (`plt.show()` relies on interactive window servers to render GUI windows; `plt.savefig()` writes the figure directly to static files like PNG/PDF, which is essential for server automation).
- How do you customize plot elements like legends, gridlines, and titles? (Call `ax.set_title()`, `ax.legend()`, and `ax.grid()`).
- Why is it important to close figures using plt.close()? (Matplotlib does not automatically garbage-collect figures; leaving them open leads to warnings and memory leaks).

AI/ML Relevance:
- Loss Curve Auditing: Charting epochs vs training/validation losses identifies if a model is overfitting (validation loss rises while training loss falls) or underfitting.
- Outliers Detection: Scatter plotting feature coordinates isolates outliers visually.
- Label Distribution: Bar charting categorical classes assesses target label balance prior to training classifiers.
"""
