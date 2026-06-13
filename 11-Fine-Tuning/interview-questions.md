# Interview Questions
**Q: How does LoRA save memory compared to full fine-tuning?**
A: LoRA freezes the original multi-billion parameter matrices and only trains small, low-rank decomposition matrices ($A \times B$). This reduces the number of trainable parameters by 99%, drastically cutting optimizer state and gradient memory requirements.

**Q: When should you use RAG vs Fine-Tuning?**
A: Use RAG for adding new, dynamic knowledge or accessing proprietary data. Use Fine-Tuning for teaching the model a specific style, tone, format, or highly specialized domain behavior.
