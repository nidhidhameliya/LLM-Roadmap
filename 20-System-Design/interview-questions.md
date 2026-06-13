# System Design Interview Questions

**Q: Design an AI code assistant (like GitHub Copilot).**
A: Use an IDE plugin sending debounced keystrokes via WebSockets to an API gateway. The backend retrieves the surrounding code context (Fill-In-The-Middle), applies lightweight syntax parsing, and sends the prompt to a highly optimized, low-latency, specialized code model (e.g., StarCoder) deployed on multi-GPU instances using vLLM for high throughput.

**Q: How do you handle high traffic spikes in an LLM app?**
A: 1) Semantic Caching (Redis/VectorDB) to serve repeated queries instantly. 2) Asynchronous queues (Celery/RabbitMQ) to accept requests and process them as capacity allows. 3) Fallback routing to secondary API providers if the primary is rate-limited. 4) Auto-scaling inference nodes (if self-hosted).

**Q: Design a personalized news feed using LLMs.**
A: Run an overnight batch job using a smaller LLM to tag/summarize thousands of incoming articles. Store embeddings in a Vector DB. Store user preference embeddings. When the user opens the app, perform a fast vector similarity search between the user profile embedding and the day's article embeddings.
