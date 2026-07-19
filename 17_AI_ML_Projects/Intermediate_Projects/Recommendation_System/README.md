# Intermediate Project 2: Collaborative Filtering Recommendation System

## Project Objective
Develop an item-to-item recommendation engine that computes similarities between products based on historical user rating patterns.

## Problem Statement
E-commerce businesses need to display relevant product suggestions to improve conversion rates and average order values. This project constructs an item-similarity engine to generate recommendations.

## Technologies Used
- Python 3.10+
- Pandas & NumPy
- Scikit-learn (Cosine Similarity matrix calculations)

## Architecture & Workflow
1. **User-Item Matrix Creation**: Construct a pivot DataFrame representing user ratings (1-5) across a catalog of movies.
2. **Similarity Computation**: Calculate pairwise cosine similarities across columns (movies/items).
3. **Recommendation Lookup**: Build a query function to retrieve the top K items most similar to a user's highly rated products.

## How to Run
Run the recommendation engine script from the repository root:
```bash
python 17_AI_ML_Projects/Intermediate_Projects/Recommendation_System/recommend.py
```

## Results & Future Improvements
- **Results**: Generates accurate product correlation matches based on spatial similarities.
- **Future Improvements**:
  - Incorporate matrix factorization (SVD - Singular Value Decomposition) to handle sparse matrix scaling.
  - Implement a hybrid recommendation model combining content-based features (genre, actor tags) with collaborative ratings.
