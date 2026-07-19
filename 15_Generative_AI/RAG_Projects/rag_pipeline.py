"""
Topic:
Generative AI - Retrieval-Augmented Generation (RAG) Pipeline

Importance:
LLMs have a knowledge cutoff date and cannot access private enterprise files.
RAG solves this by retrieving relevant context snippets from private documents
based on semantic queries, appending them into the LLM prompt to enable grounded,
accurate answers.

This file covers:
- Document Loading (mock text corpus reader)
- Text Splitting (chunking text with overlap)
- Creating Vector Embeddings (TF-IDF mapping)
- In-Memory Vector Store indexing
- Semantic Retrieval (finding relevant chunks)
- LLM Response Generation simulation with grounded context
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 1. Document Loading
# ==========================================
# Mock document loading step: list of text files contents
raw_documents = [
    """
    Project Apollo was the third United States human spaceflight program carried out by NASA. 
    It succeeded in landing the first humans on the Moon in 1969. The mission that achieved this 
    milestone was Apollo 11, crewed by Neil Armstrong, Buzz Aldrin, and Michael Collins. 
    Neil Armstrong was the commander and the first person to walk on the lunar surface.
    """,
    """
    The Python programming language was created by Guido van Rossum and released in 1991. 
    It design philosophy emphasizes code readability with its notable use of significant whitespace. 
    Its dynamic type system and automatic memory management support multiple programming paradigms.
    """
]

# ==========================================
# 2. Text Splitting (Chunking)
# ==========================================
# Chunking splits long documents into smaller segments to fit within LLM context sizes
# and provide precise semantic retrieval hooks.
def character_text_splitter(text, chunk_size=100, overlap=20):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        # Advance starting point by chunk_size minus overlap
        start += (chunk_size - overlap)
    return chunks

# ==========================================
# 3 & 4. Embeddings & Vector Database Index
# ==========================================
class SimpleRAGVectorStore:
    def __init__(self):
        self.chunks = []
        self.vectorizer = TfidfVectorizer()
        self.doc_vectors = None
        
    def index_documents(self, documents):
        # Step A: Split documents into chunks
        all_chunks = []
        for doc in documents:
            doc_chunks = character_text_splitter(doc, chunk_size=150, overlap=30)
            all_chunks.extend(doc_chunks)
        self.chunks = all_chunks
        
        # Step B: Fit and Transform chunks to TF-IDF vector embeddings
        self.doc_vectors = self.vectorizer.fit_transform(self.chunks)
        
    def retrieve(self, query, k=1):
        # Transform query to matching embedding coordinates
        query_vector = self.vectorizer.transform([query])
        
        # Calculate Cosine Similarity against all chunk vectors
        similarities = cosine_similarity(query_vector, self.doc_vectors).flatten()
        
        # Sort and return top K matching chunks
        top_indices = np.argsort(similarities)[::-1][:k]
        
        retrieved_chunks = []
        for idx in top_indices:
            retrieved_chunks.append({
                "chunk": self.chunks[idx],
                "score": similarities[idx]
            })
        return retrieved_chunks

# ==========================================
# 5. LLM Response Generation Simulation
# ==========================================
def run_rag_pipeline(query):
    # Step A: Load and index
    vector_store = SimpleRAGVectorStore()
    vector_store.index_documents(raw_documents)
    
    # Step B: Retrieve relevant context chunks
    retrieved = vector_store.retrieve(query, k=1)
    context = retrieved[0]["chunk"]
    score = retrieved[0]["score"]
    
    # Step C: Format Augmented Prompt
    augmented_prompt = f"""
System: Answer the user question strictly using the provided context. If the answer
cannot be found in the context, reply "I do not know".

Context:
"{context}"

User Question: {query}
Assistant Answer:"""
    
    # Step D: Simulated generation output
    # Check query content to simulate grounded LLM response
    response = ""
    if "apollo" in query.lower() or "moon" in query.lower():
        response = "Neil Armstrong, Buzz Aldrin, and Michael Collins landed on the Moon during the NASA Apollo 11 mission in 1969."
    elif "python" in query.lower() or "creator" in query.lower():
        response = "The Python programming language was created by Guido van Rossum and released in 1991."
    else:
        response = "I do not know."
        
    return response, context, score, augmented_prompt

# ==========================================
# 6. Execution & Test Runs
# ==========================================
if __name__ == "__main__":
    query_1 = "Who is the creator of the Python programming language?"
    
    print("=======================================")
    print(f"RAG Pipeline Execution for query: '{query_1}'")
    print("=======================================")
    
    answer_1, context_1, score_1, prompt_1 = run_rag_pipeline(query_1)
    
    print("--- 1. Retrieved Context Chunk: ---")
    print(f"Text Snippet: '{context_1}'")
    print(f"Cosine Match Score: {score_1:.4f}")
    
    print("\n--- 2. Grounded Augmented Prompt: ---")
    print(prompt_1)
    
    print(f"\n--- 3. Final Model Answer Output: ---")
    print(answer_1)
    print("=======================================")

"""
Key Takeaways:
- Text Splitting creates overlaps to ensure semantic keywords aren't sliced in half across chunks.
- Vector stores query similarity indexes to retrieve contextual snippets dynamically.
- RAG ground prompt completions strictly in retrieved contexts, preventing LLM hallucinations.

Interview Relevance:
- Explain the key components of a RAG pipeline. (1. Document Ingestion: Loading and parsing text files. 2. Chunking: Splitting text into smaller chunks. 3. Embedding: Vectorizing chunks. 4. Vector Store: Indexing embeddings. 5. Retrieval: Searching top K chunks closest to the user's query. 6. Generation: Augmenting the LLM prompt with retrieved context).
- Why do we need chunk overlap? (To prevent semantic information loss. If a crucial sentence is split exactly in half by the chunk boundary, its meaning is lost; overlap ensures sentences remain complete in at least one chunk).
- What is the difference between Dense Retrieval and Sparse Retrieval? (Sparse retrieval (like BM25/TF-IDF) looks for exact keyword occurrences; Dense retrieval (using transformer embeddings) looks for semantic meaning matching, even if different words are used).

AI/ML Relevance:
- Knowledge Grounding: Enterprise RAG implementations (using tools like LangChain, LlamaIndex, and ChromaDB) are standard for internal QA chat engines.
"""
