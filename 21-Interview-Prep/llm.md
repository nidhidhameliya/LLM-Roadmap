# Large Language Models Q&A

**Q: Explain the difference between pre-training and fine-tuning.**
A: Pre-training is teaching the model the structure of language and general knowledge by predicting the next word on trillions of tokens of raw text. Fine-tuning adjusts the pre-trained model on a smaller, curated dataset to follow instructions or specialize in a domain.

**Q: What is FlashAttention?**
A: An algorithm that computes exact attention but minimizes memory reads/writes to the GPU's High Bandwidth Memory (HBM) by fusing operations and keeping data in the fast SRAM, significantly speeding up processing for long context windows.

**Q: Describe the RoPE (Rotary Positional Embedding) mechanism.**
A: Instead of adding a static positional vector to the embedding, RoPE rotates the token embeddings in the vector space. The angle of rotation depends on the token's absolute position, natively encoding relative distances between tokens, which improves extrapolation to longer sequences.

**Q: What is the difference between top-k and nucleus (top-p) sampling?**
A: Top-k restricts sampling to the `k` most likely next tokens. Top-p restricts sampling to the smallest set of tokens whose cumulative probability exceeds `p`. Top-p dynamically adjusts the pool size based on the model's confidence, whereas top-k is a fixed size.
