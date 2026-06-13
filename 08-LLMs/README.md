# Large Language Models (LLMs)

## How They Work
- **Autoregressive Generation:** Predicting the next token iteratively.
- **Context Window:** The maximum number of tokens a model can process at once (input + output).
- **KV Cache:** Caching previous Key and Value vectors during generation so they don't have to be recomputed for every new token.

## Optimization
- **Quantization:** Reducing weights from FP16 to INT8 or INT4 to save memory and speed up inference (e.g., GGUF, AWQ).
- **FlashAttention:** A hardware-aware attention algorithm that drastically speeds up computation and reduces memory usage.
