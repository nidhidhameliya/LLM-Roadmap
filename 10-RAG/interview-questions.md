# Interview Questions
**Q: Why do we chunk documents before embedding them?**
A: Embedding whole documents dilutes the semantic meaning of specific details, making retrieval inaccurate. Chunking preserves localized semantics and ensures the retrieved text fits within the LLM's context window.

**Q: What is the purpose of a cross-encoder (Reranker) in advanced RAG?**
A: Standard bi-encoders (embeddings) are fast but compare vectors independently. A cross-encoder processes the query and document together through attention layers, yielding a much more accurate relevance score, albeit at a higher computational cost.
