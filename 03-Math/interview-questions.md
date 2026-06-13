# Interview Questions
**Q: How does RoPE (Rotary Positional Embedding) differ from Absolute Positional Encoding?**
A: Absolute encoding (like in the original Transformer) adds a static positional vector. RoPE applies a rotation matrix to the token embeddings based on their position. This naturally encodes the relative distance between tokens mathematically via dot products, improving length extrapolation.

**Q: Why do we care so much about KV Cache size during inference?**
A: Autoregressive generation processes one token at a time. Without KV cache, we must recompute attention over all previous tokens. Storing the Keys and Values in VRAM allows fast O(1) attention updates, but at massive scale, the KV cache can consume more VRAM than the model weights themselves, bottlenecking concurrent batch sizes.
