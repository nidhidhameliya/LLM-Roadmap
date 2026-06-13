# RAG Interview Q&A

**Q: What are the main challenges of scaling RAG to millions of documents?**
A: Ensuring high recall (finding the right chunks), dealing with conflicting information in the database, minimizing vector search latency, and keeping the vector database synchronized with the source documents (CRUD operations on chunks).

**Q: What is the "Lost in the Middle" phenomenon?**
A: LLMs tend to pay more attention to information at the very beginning and very end of their context window. If crucial retrieved context is placed in the middle of a long prompt, the model might ignore it.

**Q: How does HyDE (Hypothetical Document Embeddings) improve retrieval?**
A: A user query (e.g., "How do I reset my password?") might not lexically match the answer in the DB. HyDE asks an LLM to generate a hypothetical answer first, embeds that answer, and uses it to search the DB, often resulting in closer semantic matches to the actual documentation.

**Q: What is chunk overlap and why is it used?**
A: It's duplicating a small number of tokens at the boundary of adjacent chunks. It prevents cutting a sentence or core concept in half, ensuring that context isn't lost at the chunk borders.
