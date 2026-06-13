# Interview Questions
**Q: What is the KV Cache and why is it important?**
A: The KV cache stores the Key and Value matrices of previously processed tokens during generation. It prevents the model from recomputing the attention over the entire sequence for every new token, significantly speeding up autoregressive decoding.

**Q: Explain INT4 Quantization.**
A: Quantization reduces the precision of model weights from 16-bit floats to 4-bit integers. This drastically reduces VRAM requirements and memory bandwidth bottlenecks with minimal loss in generation quality.
