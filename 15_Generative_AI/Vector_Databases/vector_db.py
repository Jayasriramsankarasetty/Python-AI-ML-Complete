"""
Topic:
Generative AI - In-Memory Vector Database from Scratch

Importance:
Vector Databases (like Pinecone, Milvus, Chroma) index high-dimensional embeddings
for sub-millisecond retrieval. Understanding the mechanisms of inserting, indexing, and querying
documents using vector calculations (e.g. Cosine Similarity) is key for system designs.

This file covers:
- Concept: Vector DB storage, metadata, and vector indexing
- Implementing a simple in-memory Vector Database class
- Storing document texts, vector arrays, and metadata payloads
- Implementing search querying with similarity scores ranking
- Testing insertion and querying using NumPy operations
"""

import numpy as np

# ==========================================
# 1. Concept Explanation & Architecture
# ==========================================
# Traditional databases index text using keywords (inverted index, BM25).
# Vector Databases store and index high-dimensional numeric arrays (embeddings).
# Key Components:
#   - Storage: Holds document raw content, vector coordinates, and metadata payload (JSON dict).
#   - Similarity Metric: Cosine Similarity, L2 Euclidean Distance, or Dot Product.
#   - Indexing: Algorithms (like HNSW - Hierarchical Navigable Small World, IVF - Inverted File Index)
#     that cluster vectors for fast approximate nearest neighbor (ANN) searches, avoiding O(N) comparisons.

# ==========================================
# 2. Simple Vector Database Implementation
# ==========================================
class SimpleVectorDB:
    def __init__(self):
        # Database rows
        self.storage = []
        
    def insert(self, text, vector, metadata=None):
        """
        Insert a document record into our database.
        """
        # Ensure vector is a numpy array
        vector_arr = np.array(vector, dtype=float)
        record = {
            "text": text,
            "vector": vector_arr,
            "metadata": metadata or {}
        }
        self.storage.append(record)
        
    def query(self, query_vector, k=2, filter_meta=None):
        """
        Retrieve top K documents closest to the query vector.
        """
        query_arr = np.array(query_vector, dtype=float)
        
        matches = []
        for record in self.storage:
            # Metadata filter check (if requested)
            if filter_meta:
                skip = False
                for key, val in filter_meta.items():
                    if record["metadata"].get(key) != val:
                        skip = True
                        break
                if skip:
                    continue
            
            # Compute Cosine Similarity manually using numpy
            vec = record["vector"]
            # dot product / (norm_q * norm_v)
            dot_product = np.dot(query_arr, vec)
            norm_q = np.linalg.norm(query_arr)
            norm_v = np.linalg.norm(vec)
            
            # Avoid division by zero
            similarity = dot_product / (norm_q * norm_v) if (norm_q > 0 and norm_v > 0) else 0.0
            
            matches.append({
                "text": record["text"],
                "metadata": record["metadata"],
                "score": similarity
            })
            
        # Sort matches by score descending
        matches.sort(key=lambda x: x["score"], reverse=True)
        return matches[:k]

# ==========================================
# 3. Execution & Testing
# ==========================================
if __name__ == "__main__":
    db = SimpleVectorDB()
    
    # We define mock 3-dimensional embeddings representing semantic categories:
    # Dimension 1: Technology, Dimension 2: Food, Dimension 3: Finance
    doc_1_emb = [0.9, 0.1, 0.0]  # Tech document
    doc_2_emb = [0.1, 0.8, 0.1]  # Food document
    doc_3_emb = [0.2, 0.0, 0.9]  # Finance document
    doc_4_emb = [0.8, 0.2, 0.1]  # Tech document
    
    db.insert("Learn Python and cloud deployment models.", doc_1_emb, {"category": "tech"})
    db.insert("Cooking delicious pasta with garlic and basil.", doc_2_emb, {"category": "food"})
    db.insert("Investment portfolios, stock markets, and mutual funds.", doc_3_emb, {"category": "finance"})
    db.insert("Software engineering best practices in coding.", doc_4_emb, {"category": "tech"})
    
    # Query: A technology-related concept
    query_emb = [0.85, 0.15, 0.0]
    
    print("=======================================")
    print(f"Querying Top 2 nearest documents for vector: {query_emb}")
    print("=======================================")
    
    results = db.query(query_emb, k=2)
    for idx, res in enumerate(results):
        print(f"Match {idx+1} | Score: {res['score']:.4f} | Category: {res['metadata']['category']}")
        print(f"  Text: {res['text']}\n")
        
    print("=======================================")
    print("Querying with Metadata Filter Category = 'tech':")
    print("=======================================")
    filtered_results = db.query(query_emb, k=2, filter_meta={"category": "tech"})
    for idx, res in enumerate(filtered_results):
         print(f"Match {idx+1} | Score: {res['score']:.4f} | Text: {res['text']}")
    print("=======================================")

"""
Key Takeaways:
- Vector databases store high-dimensional embeddings paired with metadata payloads.
- Cosine distance calculations compute spatial similarity directions between queries and stored records.
- Metadata filtering lets engines restrict search spaces based on categorical keys prior to or after similarity computation.

Interview Relevance:
- How does a Vector Database query millions of vectors under 10ms? (By using Approximate Nearest Neighbor (ANN) index graphs like HNSW. Instead of comparing the query vector against every record (O(N) search), HNSW navigates clustered multi-layered graphs to find nearest neighbors in logarithmic logarithmic time).
- Explain Pre-filtering vs Post-filtering in Vector DBs. (Pre-filtering applies metadata filters before searching vectors, ensuring only valid documents are checked. Post-filtering searches vectors first, then throws away results that fail metadata checks, which can result in returning fewer than K matches).
- What is the difference between Cosine Similarity and Dot Product? (Dot product only measures vector projection directions and lengths; Cosine similarity normalizes vector lengths, measuring only the angle between them).

AI/ML Relevance:
- RAG Storage: Essential index component to locate correct context documents from massive files databases for LLM prompt augmentation.
"""
