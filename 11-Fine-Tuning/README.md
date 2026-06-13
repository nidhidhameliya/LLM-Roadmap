# Fine-Tuning

## Concepts
- **Full Fine-Tuning:** Updating all model weights (expensive, requires huge VRAM).
- **PEFT (Parameter-Efficient Fine-Tuning):** Updating only a small subset of parameters.
- **LoRA (Low-Rank Adaptation):** Injecting trainable low-rank matrices into transformer layers while freezing the original weights. Drastically reduces memory usage.
- **QLoRA:** LoRA combined with a quantized (4-bit) base model, allowing fine-tuning of large models on consumer GPUs.
- **RLHF & DPO:** Aligning models with human preferences. DPO (Direct Preference Optimization) is a simpler, mathematically equivalent alternative to RLHF that doesn't require a separate reward model.
