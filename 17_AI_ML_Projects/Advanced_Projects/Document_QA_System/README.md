# Advanced Project 2: Document Q&A System

## Project Objective
Develop a document question-answering system capable of parsing unstructured document manuals and extracting exact contextual matches to answer user inputs.

## Problem Statement
Information within manuals is hidden inside deep paragraphs. A QA system should parse documents, index sentence sections, and retrieve the exact target matching text segment to answer user requests directly.

## Technologies Used
- Python 3.10+
- Pandas & NumPy
- Scikit-learn (TF-IDF vector mapping, pairwise cosine similarity rankings)

## Architecture & Workflow
1. **Document Loading**: Ingest a structured document list (e.g. employee guide).
2. **Parsing & Indexing**: Tokenize paragraphs into individual sentence segments.
3. **Retrieval**: Compute similarity of query against sentences.
4. **Outputting**: Returns the highest matching sentence as the target answer.

## How to Run
Run the Document QA script from the repository root:
```bash
python 17_AI_ML_Projects/Advanced_Projects/Document_QA_System/qa_system.py
```

## Results & Future Improvements
- **Results**: Successfully parses text sentences and resolves relevant query matches.
- **Future Improvements**:
  - Implement PDF/Word document parser libraries (`PyPDF2` or `docx`).
  - Deploy semantic search metrics using pretrained embeddings.
