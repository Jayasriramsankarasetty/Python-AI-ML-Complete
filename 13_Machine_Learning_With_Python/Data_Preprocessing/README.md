# Data Preprocessing for Machine Learning

This folder covers the fundamentals of structuring datasets for scikit-learn training estimators, focusing on feature-wise cleanups, standardizations, and column selections.

---

## Preprocessing Sub-modules

1. [missing_values.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Data_Preprocessing/missing_values.py):
   * Demonstrates imputing missing data using `SimpleImputer` (univariate) and `KNNImputer` (multivariate).
2. [encoding.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Data_Preprocessing/encoding.py):
   * Converts categorical parameters to numerical representations using `OneHotEncoder` and `OrdinalEncoder`.
3. [scaling.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Data_Preprocessing/scaling.py):
   * Scales continuous values bounds using `StandardScaler` (Z-scores), `MinMaxScaler` (0 to 1), and `RobustScaler` (medians/IQR).
4. [feature_selection.py](file:///c:/Users/S. Jaya Sri Ram/OneDrive/Desktop/Placements/Python-Journey/13_Machine_Learning_With_Python/Data_Preprocessing/feature_selection.py):
   * Selects important training attributes using `VarianceThreshold`, correlation filtering, and ANOVA `SelectKBest`.
