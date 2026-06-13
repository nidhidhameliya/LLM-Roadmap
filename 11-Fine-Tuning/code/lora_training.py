from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM
import torch

# Dummy configuration for demonstration
model_id = "gpt2" # Use a small model to avoid downloads
model = AutoModelForCausalLM.from_pretrained(model_id)

config = LoraConfig(
    r=8, 
    lora_alpha=32, 
    target_modules=["c_attn"], # GPT-2 specific attention module name
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

peft_model = get_peft_model(model, config)
peft_model.print_trainable_parameters()
# Output: trainable params: X || all params: Y || trainable%: Z
