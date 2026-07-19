"""
Topic:
Advanced Project - RAG Assistant from Scratch

Importance:
Retrieval-Augmented Generation is the standard system architecture for private database QA.
Building this pipeline from scratch proves your conceptual clarity of chunking,
embedding, database query retrieval, and context augmentation steps.

This file covers:
- Loading private documentation corpus
- Implementing recursive character splitting (chunking)
- Computing embeddings using TfidfVectorizer
- Query retrieval based on Cosine Similarity
- Compiling the augmented prompt payload
"""

# ==========================================
# 1. Import Libraries
# ==========================================
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 2. Ingest & Chunk Documents
# ==========================================
kb_documents = [
    "Project Orion is a secure spacecraft initiative designed for deep solar journeys, scheduled for pilot test launch in 2028. It uses hybrid fusion thrusters.",
    "Company holiday policy: Employees receive 25 days of paid annual leave. Vacation requests must be logged in the HR portal 2 weeks in advance."
]

def split_text_to_chunks(text, size=100, overlap=20):
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += (size - overlap)
    return chunks

# ==========================================
# 3. Simple Vector Indexer
# ==========================================
class RAGAppEngine:
    def __init__(self):
        self.chunks = []
        self.vectorizer = TfidfVectorizer()
        self.vectors = None
        
    def build_index(self, docs):
        # Chunk
        for doc in docs:
            self.chunks.extend(split_text_to_chunks(doc, size=80, overlap=15))
        # Vectorize
        self.vectors = self.vectorizer.fit_transform(self.chunks)
        
    def search(self, query, k=1):
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.vectors).flatten()
        best_idx = np.argmax(similarities)
        return self.chunks[best_idx], similarities[best_idx]

# ==========================================
# 4. Run RAG Pipeline
# ==========================================
def run_assistant():
    engine = RAGAppEngine()
    engine.build_index(kb_documents)
    
    query = "When is the launch date of Project Orion?"
    context, score = engine.search(query)
    
    # Context Grounded Prompt
    prompt = f"""
Instructions: Answer the question using the context. If not found, say "I do not know".

Context:
"{context}"

Question: {query}
Answer:"""

    # Simulated generation
    response = ""
    if "orion" in query.lower() and "launch" in query.lower():
        response = "Project Orion is scheduled for a pilot test launch in 2028."
    else:
        response = "I do not know."
        
    print("=======================================")
    print("RAG Assistant Project Pipeline Run:")
    print("=======================================")
    print(f"Query:                 {query}")
    print(f"Retrieved Score:       {score:.4f}")
    print(f"Retrieved Context:     '{context}'")
    print(f"Grounded Model Answer: {response}")
    print("=======================================")

if __name__ == "__main__":
    run_assistant()

"""
Key Takeaways:
- Chunking breaks files into readable spans to feed into model input limits.
- Overlaps preserve contextual flow across boundary splits.
- In-context learning uses retrieved text as factual context to anchor predictions.

Interview Relevance:
- Explain what 'Grounding' means in RAG. (Grounding is the process of forcing the LLM to base its answers strictly on the retrieved context documents, preventing it from generating fabricated answers from its pre-trained weights).

AI/ML Relevance:
- Search applications: The standard design template used in corporate document search chatbots.
"""
