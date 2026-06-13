# Math for LLM Engineers

## Core Linear Algebra
- **Matrix Multiplication (MatMul):** The bottleneck of LLM inference.
- **Dot Product & Cosine Similarity:** The mathematical basis for RAG retrieval and embedding proximity.

## Advanced LLM Math
- **KV Cache Size Calculation:** `2 * number_of_layers * number_of_heads * head_dimension * sequence_length * batch_size * bytes_per_parameter`. Crucial for vLLM sizing.
- **RoPE (Rotary Positional Embeddings):** Rotating embedding vectors in complex space to preserve relative distance between tokens natively, allowing infinite context window extrapolation.
