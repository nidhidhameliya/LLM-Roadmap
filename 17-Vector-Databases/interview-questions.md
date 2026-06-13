# Interview Questions
**Q: What is HNSW (Hierarchical Navigable Small World)?**
A: A popular ANN algorithm that builds a multi-layered graph of vectors. Searches start at the top (coarse) layer and navigate down to the bottom (fine) layer to quickly find the nearest neighbors without comparing against every single vector.

**Q: Why not just use Postgres or Elasticsearch for embeddings?**
A: Traditional DBs are optimized for exact keyword matches (B-Trees). While Postgres with `pgvector` is now viable, dedicated Vector DBs (Chroma, Pinecone) are often faster, easier to scale for billion-vector workloads, and have purpose-built indexing algorithms.
