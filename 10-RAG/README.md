# Retrieval-Augmented Generation (RAG)

## Core Components
- **Document Loaders:** Extracting text from PDFs, HTML, etc.
- **Chunking:** Splitting text into smaller pieces (e.g., 500 tokens with 50 token overlap) to fit context limits and improve search precision.
- **Embeddings:** Converting chunks into dense vectors.
- **Vector Database:** Storing and indexing vectors for fast similarity search (Chroma, FAISS).
- **Retrieval:** Fetching top-K most similar chunks to the user's query.
- **Generation:** Passing the retrieved chunks + the query to the LLM to form a grounded answer.

## Advanced Techniques
- **Reranking:** Using a specialized cross-encoder model to re-score retrieved documents for higher relevance.
- **HyDE:** Hypothetical Document Embeddings (generating a fake answer and embedding it for retrieval).
