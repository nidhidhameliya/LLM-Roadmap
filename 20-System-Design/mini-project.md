# Mini-Project: Semantic Cache
**Brief:** Implement a caching layer to reduce LLM API costs.
**Requirements:** When a user asks a question, embed the query. Check a Vector DB for an existing embedded query with >0.95 similarity. If found, return the cached answer. If not, call the LLM and cache the new query/answer pair.
