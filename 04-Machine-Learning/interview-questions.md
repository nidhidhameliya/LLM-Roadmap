# Interview Questions
**Q: Explain how MoE (Mixture of Experts) reduces inference latency.**
A: MoE decouples total parameter count from compute cost. A model might have 47B total parameters, but a routing layer ensures each token only activates 2 of the 8 experts (e.g., 12B active parameters). This drastically reduces the FLOPs required per token generation.

**Q: What is the Memory Wall in Deep Learning?**
A: GPUs can compute math (FLOPs) much faster than they can read data from memory (HBM bandwidth). LLM generation is largely memory-bandwidth bound (reading weights for every token), not compute-bound. This is why AWQ/GPTQ quantization (reading 4-bits instead of 16-bits) speeds up generation.
