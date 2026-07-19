"""
Topic:
Generative AI - Text Embeddings & Cosine Similarity

Importance:
Embeddings translate natural language tokens into dense numerical vectors
where semantic distance corresponds to meaning. They are the core technology
behind semantic search, recommendation engines, and retrieval steps in RAG pipelines.

This file covers:
- Concept: Mapping text to high-dimensional space, cosine similarity formula
- Creating vector representations of text using scikit-learn TF-IDF Vectorizer
- Calculating Cosine Similarity scores between query and document vectors
- Simple interpretation of semantic match outputs
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 1. Concept Explanation & Mathematical formulas
# ==========================================
# An Embedding is a representation of text as a list of numbers (a vector).
# Words or sentences with similar meanings are projected closer together in the vector space.
# Formula: Cosine Similarity measures the angle between two vectors A and B:
#   Cosine Similarity = (A • B) / (||A|| * ||B||)
#     - Result = 1.0: Vectors point in identical directions (highly similar).
#     - Result = 0.0: Vectors are orthogonal (no similarity).
#     - Result = -1.0: Vectors point in opposite directions.

# ==========================================
# 2. Text Vectorization & Cosine Similarity Setup
# ==========================================
def calculate_sentence_similarity():
    # Documents corpus (knowledge base)
    documents = [
        "Python is a versatile programming language for machine learning.",
        "Deep learning models require GPUs or specialized hardware to train.",
        "SQL databases store records in relational tables using rows and columns.",
        "Data science involves statistical analysis, cleaning, and visualizations."
    ]
    
    # Query query
    query = "What hardware do I need to train a neural network?"
    
    print("=======================================")
    print("Document Corpus:")
    print("=======================================")
    for idx, doc in enumerate(documents):
        print(f"Doc {idx}: {doc}")
    print(f"\nQuery: '{query}'")
    print("=======================================")
    
    # Vectorize text using TF-IDF (Term Frequency-Inverse Document Frequency)
    # This maps text into bag-of-words vector coordinates scaled by token occurrences.
    vectorizer = TfidfVectorizer()
    
    # Fit vectorizer on all documents + query
    all_texts = documents + [query]
    vectorizer.fit(all_texts)
    
    # Transform documents and query to vectors
    doc_vectors = vectorizer.transform(documents)
    query_vector = vectorizer.transform([query])
    
    # Compute Cosine Similarity between the query vector and all document vectors
    similarities = cosine_similarity(query_vector, doc_vectors).flatten()
    
    # ==========================================
    # 3. Simple Interpretation
    # ==========================================
    results = pd.DataFrame({
        "Document": documents,
        "Similarity_Score": similarities
    }).sort_values(by="Similarity_Score", ascending=False)
    
    print("\n=======================================")
    print("Cosine Similarity Search Results:")
    print("=======================================")
    print(results)
    print("=======================================")
    
    best_match = results.iloc[0]
    print(f"\nBest Matching Document: '{best_match['Document']}'")
    print(f"Cosine Similarity:      {best_match['Similarity_Score']:.4f}")
    print("Interpretation: The query specifically asks about 'hardware' and 'train', aligning closely")
    print("with Doc 1 ('Deep learning models require GPUs or specialized hardware to train').")
    print("=======================================")

if __name__ == "__main__":
    calculate_sentence_similarity()

"""
Key Takeaways:
- Embeddings translate textual semantic meanings into numeric vectors.
- Cosine similarity measures the angle between vectors to evaluate semantic matching, independent of text lengths.
- In production, deep learning models (like OpenAI's text-embedding-3-small) output dense vectors (e.g. 1536 dimensions) for semantic lookup.

Interview Relevance:
- Why is Cosine Similarity preferred over Euclidean Distance for text embeddings? (Euclidean distance is sensitive to vector length, meaning longer documents will be placed far away simply due to word counts. Cosine similarity only measures the angle direction, making it length-invariant).
- How do Transformer embeddings differ from Word2Vec embeddings? (Word2Vec assigns a static vector to each word regardless of context; Transformers like BERT generate contextual embeddings, where the word 'bank' has different vectors in 'river bank' vs 'money bank').
- What does the dimensionality of an embedding represent? (The number of float coordinates in the vector, representing latent semantic feature concepts learned by the model).

AI/ML Relevance:
- Retrieval step: Forms the query search indexing core of all RAG (Retrieval-Augmented Generation) systems.
"""
