# Modern Deep Learning & GPU Fundamentals

## From Transformers to Hardware
- **Mixture of Experts (MoE):** Using router networks to only activate a subset of parameters (experts) per token. Allows scaling to 8x7B parameters while only computing 14B parameters per forward pass (e.g., Mixtral).
- **GPU Architecture:** Understanding SMs (Streaming Multiprocessors), SRAM vs. HBM (High Bandwidth Memory).
- **FlashAttention:** Computing exact attention without materializing the massive N x N attention matrix in slow HBM; keeping operations in ultra-fast SRAM.

## Classic ML
- Random Forests and XGBoost remain the undefeated champions of tabular data. LLMs are for unstructured data.
