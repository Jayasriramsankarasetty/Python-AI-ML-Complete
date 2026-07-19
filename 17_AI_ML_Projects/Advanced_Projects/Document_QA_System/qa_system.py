"""
Topic:
Advanced Project - Document Q&A System

Importance:
This project demonstrates parsing paragraph-style text into sentence nodes,
indexing them using TF-IDF, and returning precise matching nodes.

This file covers:
- Ingesting raw manual paragraphs
- Splitting paragraphs into sentences
- Computing sentence vectors
- Retrieving matching answers using Cosine Similarity
"""

# ==========================================
# 1. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 2. Ingest & Parse Manual
# ==========================================
raw_manual = """
The company headquarters is located in San Francisco, California. 
Office working hours are from 9:00 AM to 5:00 PM, Monday through Friday. 
A complimentary lunch is provided for all staff members in the cafeteria at 12:30 PM. 
Parking passes can be requested directly from the facility coordinator in building B.
"""

# Split manual into clean list of sentences
sentences = [s.strip() for s in raw_manual.split("\n") if s.strip()]
# Expand any multi-sentence lines split by period
parsed_sentences = []
for line in sentences:
    parts = [p.strip() for p in line.split(".") if p.strip()]
    parsed_sentences.extend(parts)

# ==========================================
# 3. Vector Indexing & Search
# ==========================================
class DocumentQASystem:
    def __init__(self, document_nodes):
        self.nodes = document_nodes
        self.vectorizer = TfidfVectorizer()
        self.vectors = self.vectorizer.fit_transform(self.nodes)
        
    def query(self, user_question, k=1):
        query_vector = self.vectorizer.transform([user_question])
        similarities = cosine_similarity(query_vector, self.vectors).flatten()
        top_indices = np.argsort(similarities)[::-1][:k]
        
        matches = []
        for idx in top_indices:
            matches.append({
                "sentence": self.nodes[idx],
                "score": similarities[idx]
            })
        return matches

# ==========================================
# 4. Testing QA Runs
# ==========================================
if __name__ == "__main__":
    qa_engine = DocumentQASystem(parsed_sentences)
    
    question = "Where can I get a parking pass?"
    print("=======================================")
    print(f"Query: {question}")
    print("=======================================")
    
    results = qa_engine.query(question, k=1)
    best_match = results[0]
    
    print(f"Best Match Sentence: '{best_match['sentence']}.'")
    print(f"Similarity Score:     {best_match['score']:.4f}")
    print("=======================================")

"""
Key Takeaways:
- Document QA systems segment text files into granular sentence nodes.
- TF-IDF vectors map semantic intersection coefficients.
- Returning direct matching sentence nodes eliminates downstream LLM synthesis compute steps.

Interview Relevance:
- How do you parse unstructured PDF files for QA systems? (Use parsing libraries like PyPDF2 to extract raw strings, apply regex or NLTK's sentence tokenizers to split text into distinct semantic segments, and index those segments).

AI/ML Relevance:
- Search and retrieval: Used to build document lookup modules for customer support agents.
"""
