# Interview Questions
**Q: Why does "Chain of Thought" improve LLM performance on math problems?**
A: LLMs generate sequentially. CoT forces the model to externalize intermediate computational steps into the context window, allowing it to "read" its own logic before producing the final answer, rather than trying to compute everything in a single hidden forward pass.

**Q: What is the difference between Temperature and Top-P?**
A: Temperature scales the logits before softmax (higher = flatter distribution = more random). Top-P (nucleus sampling) restricts the token pool to the smallest set of tokens whose cumulative probability exceeds P. Both control randomness, but usually only one should be tuned at a time.
