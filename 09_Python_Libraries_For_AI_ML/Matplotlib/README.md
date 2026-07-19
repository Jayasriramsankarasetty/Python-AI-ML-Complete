# Matplotlib Data Visualization Guide

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It provides an object-oriented API for embedding plots into applications.

---

## Anatomy of a Matplotlib Figure

Understanding the component hierarchy prevents formatting errors:
* **Figure**:
   * The global container window that tracks all child Axes, titles, legends, and canvases.
* **Axes**:
   * The actual plotting canvas (with x and y coordinate limits) that contains labels, ticks, and line plot curves. A Figure can have multiple Axes subplots.

---

## Non-Interactive Backends (`Agg`)

In headless environments (like automated CI/CD servers or remote terminal clusters), running `plt.show()` throws errors because there is no graphical display window server active.
* To prevent this, configure the backend to use `Agg` (Anti-Grain Geometry engine) before importing pyplot:
  ```python
  import matplotlib
  matplotlib.use('Agg')
  import matplotlib.pyplot as plt
  ```
* This compiles plots to static image buffers that can be saved directly as `.png` files via `plt.savefig('output.png')` without attempting to launch interactive windows.

---

## Files in this Folder

1. [matplotlib_basics.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/09_Python_Libraries_For_AI_ML/Matplotlib/matplotlib_basics.py):
   * Basic plot types: Line plots (custom styling, legends), Scatter plots, and Bar charts, using the `Agg` non-interactive backend.
2. [matplotlib_subplots.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/09_Python_Libraries_For_AI_ML/Matplotlib/matplotlib_subplots.py):
   * Histograms, subplot grid layouts, style themes, and layout adjustments.
