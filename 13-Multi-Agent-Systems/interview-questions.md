# Interview Questions
**Q: Why use a Multi-Agent system instead of one single powerful agent?**
A: A single agent with too many tools and instructions suffers from "lost in the middle" context issues and prompt dilution. Multi-agent systems constrain the context and focus of each LLM call, leading to higher quality, specialized outputs.

**Q: What is a common failure mode of networked (conversational) multi-agent systems?**
A: Infinite loops or "hallucination echo chambers" where agents agree on incorrect information or endlessly politely thank each other. Strict orchestration or "manager" routing is required to prevent this.
