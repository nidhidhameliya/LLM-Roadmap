# AI System Design Q&A

**Q: How do you design an LLM system for high availability?**
A: Deploy behind a load balancer with multiple endpoints/providers (e.g., primary OpenAI, fallback Anthropic, tertiary local Azure endpoint). Implement circuit breakers and exponential backoff in the client wrapper.

**Q: How do you manage long-term memory for a conversational agent?**
A: Use a tiered approach: A rolling buffer for the immediate conversation context, and a Vector DB to store older interactions. When the user speaks, embed their message, retrieve the 3 most relevant past interactions from the Vector DB, and inject them into the system prompt.

**Q: Explain Semantic Caching.**
A: Caching API responses not by exact string match, but by the embedding similarity of the query. If a new query has a >0.98 cosine similarity to a cached query, return the cached LLM response to save latency and cost.

**Q: How do you handle model updates or deprecations in production?**
A: Implement prompt versioning and abstract the LLM client behind a common interface (like Langchain's BaseChatModel). Run shadow deployments (sending live traffic to the new model without returning it to the user) to evaluate responses before fully cutting over.
