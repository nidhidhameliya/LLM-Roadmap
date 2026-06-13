# AI System Design

This section focuses on designing large-scale, production-ready AI applications.
See `interview-questions.md` for specific scenarios.

## Core Considerations
- **Latency vs. Throughput:** Do you need real-time streaming (latency) or batch processing millions of rows overnight (throughput)?
- **Cost:** GPT-4 is expensive. Can you route easy queries to a cheaper model (e.g., Haiku) and hard queries to GPT-4?
- **Data Privacy:** Can you send user data to OpenAI, or do you need a local model hosted on an internal AWS VPC?
- **Reliability:** LLM APIs fail. You need exponential backoff, retry logic, and fallback models.
