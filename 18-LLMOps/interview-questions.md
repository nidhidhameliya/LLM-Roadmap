# Interview Questions
**Q: What is "LLM-as-a-judge"?**
A: Using a powerful model (like GPT-4) to evaluate the outputs of another model (like a smaller 8B model) based on specific criteria like relevance or helpfulness, scaling evaluation without human labelers.

**Q: How do you prevent Prompt Injection?**
A: Use separate system and user messages, delimit user input with distinct characters (e.g., `"""`), and employ input guardrails (classifiers trained to detect injection attempts) before processing.
