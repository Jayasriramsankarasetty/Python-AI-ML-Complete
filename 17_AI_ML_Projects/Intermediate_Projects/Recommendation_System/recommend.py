"""
Topic:
Intermediate Project - Collaborative Filtering Recommendation System using Cosine Similarity

Importance:
Recommendation systems drive click-through rates across tech platforms.
Understanding how to manipulate user-item matrices and calculate item-item cosine matches
is a high-frequency system design interview requirement.

This file covers:
- Setting up a User-Item rating matrix
- Calculating pairwise Cosine Similarity across items (movies)
- Creating a recommendation retrieval function
- Testing query recommendations
"""

# ==========================================
# 1. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 2. Setup User-Item Matrix
# ==========================================
# Users ratings (1 to 5) for 5 movies
# NaN indicates the user hasn't watched/rated the movie
ratings_data = {
    "User_A": [5.0, 4.0, 1.0, np.nan, 1.0],
    "User_B": [4.0, 5.0, np.nan, 2.0, 1.0],
    "User_C": [1.0, np.nan, 5.0, 4.0, 4.0],
    "User_D": [2.0, 1.0, 4.0, 5.0, np.nan],
    "User_E": [np.nan, 1.0, 4.0, 4.0, 5.0]
}

movies = ["Toy_Story", "The_Lion_King", "The_Matrix", "Inception", "Interstellar"]

# Create DataFrame (Index = Movies, Columns = Users)
df_ratings = pd.DataFrame(ratings_data, index=movies)

print("=======================================")
print("Original User-Item Ratings Matrix:")
print("=======================================")
print(df_ratings)

# ==========================================
# 3. Preprocessing (Handling missing values)
# ==========================================
# Subtract row mean (mean centering) and fill NaNs with 0.0
# This normalizes rating behaviors (some users rate strictly, others leniently)
df_centered = df_ratings.sub(df_ratings.mean(axis=1), axis=0).fillna(0.0)

# ==========================================
# 4. Compute Similarity Matrix
# ==========================================
# Calculate cosine similarity between rows (movies)
similarity_matrix = cosine_similarity(df_centered)
df_similarity = pd.DataFrame(similarity_matrix, index=movies, columns=movies)

print("\n=======================================")
print("Item-to-Item Cosine Similarity Matrix:")
print("=======================================")
print(df_similarity.round(4))
print("=======================================")

# ==========================================
# 5. Retrieve Recommendations
# ==========================================
def get_similar_items(movie_name, k=2):
    """
    Retrieve top K movies similar to the given query movie.
    """
    if movie_name not in df_similarity.index:
        return f"Movie '{movie_name}' not found in catalog."
        
    # Get similarity series for the query movie
    similar_scores = df_similarity[movie_name].drop(movie_name)
    # Sort descending
    top_matches = similar_scores.sort_values(ascending=False).head(k)
    return top_matches

if __name__ == "__main__":
    query_movie = "Toy_Story"
    print(f"\nGenerating Top 2 recommendations for users who watched '{query_movie}':")
    recs = get_similar_items(query_movie, k=2)
    print(recs)
    print("=======================================")

"""
Key Takeaways:
- Item-Item Collaborative Filtering suggests products similar to what a user rated highly in the past.
- Mean centering normalizes baseline user biases across rating scales.
- Cosine similarity evaluates spatial angle alignments across user rating columns.

Interview Relevance:
- Explain Collaborative Filtering vs Content-Based filtering. (Collaborative filtering makes recommendations based on user rating behaviors and historical matrices; Content-Based filtering makes recommendations based on features of the items themselves, like genre, tags, or actors).
- What is the Cold Start problem? (A scenario where a recommendation system fails to recommend items to new users or suggest new items because there is no historical rating data available yet. Resolved using content-based fallbacks or popularity ranks).

AI/ML Relevance:
- E-commerce Suggestion engines: The fundamental mathematical backbone behind Amazon-style product recommendation widgets.
"""
