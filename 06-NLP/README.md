# Modern NLP & Tokenization

## Tokenization Mechanics
- **BPE (Byte-Pair Encoding):** The standard for LLMs (OpenAI's `tiktoken`). Operates on raw bytes, allowing it to represent *any* character, eliminating `<UNK>` (out-of-vocabulary) tokens.
- **Glitch Tokens / SolidGoldMagikarp:** Tokens that were highly frequent in scraped internet data but never appeared in training prompts, causing models to hallucinate wildly when encountered.
- **Token Efficiency:** Non-English languages often require 3-4x more tokens to represent the same meaning as English, drastically increasing API costs and latency.

## Embeddings
- Modern embeddings (like text-embedding-3-large) natively support **Matryoshka Representation Learning**, allowing you to truncate the vector size (e.g., from 3072 to 256) while retaining 90% of the performance.
