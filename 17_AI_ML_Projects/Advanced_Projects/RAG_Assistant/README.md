# Advanced Project 1: Retrieval-Augmented Generation (RAG) Assistant

## Project Objective
Develop a local Retrieval-Augmented Generation (RAG) assistant that indexes unstructured knowledge files and retrieves relevant segments to answer user questions truthfully without hallucinating.

## Problem Statement
Standard pre-trained LLMs lack access to private, real-time files (like employee manuals or custom software logs). Grounding their queries inside an index lookup database ensures fact-based, context-grounded answers.

## Technologies Used
- Python 3.10+
- Pandas & NumPy
- Scikit-learn (TfidfVectorizer for mock embedding generation, cosine similarities retrieval)

## Architecture & Workflow
1. **Document Loading**: Ingest a text file corpus containing project guidelines.
2. **Text Chunking**: Split long text blocks into smaller overlapping chunks (size=150, overlap=30).
3. **Vector Database Indexing**: Compute TF-IDF embedding vectors for all chunks and store them in an in-memory vector library.
4. **Retrieval**: Compute the cosine similarity score between the user query vector and indexed document vectors, returning the top K matches.
5. **Generation**: Combine the retrieved context with the user query inside an augmented prompt template to simulate grounded response generation.

## How to Run
Run the RAG assistant script from the repository root:
```bash
python 17_AI_ML_Projects/Advanced_Projects/RAG_Assistant/rag_app.py
```

## Results & Future Improvements
- **Results**: Successfully retrieves relevant document context and returns precise answers without hallucination.
- **Future Improvements**:
  - Integrate live open-source embeddings models (like HuggingFace `sentence-transformers`) and a local vector database (like Chroma or FAISS).
  - Create a web-based user interface using Streamlit.
