from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "gpt2" # Using GPT-2 as a small placeholder
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cpu")

prompt = "The future of AI is"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
outputs = model.generate(
    **inputs,
    max_new_tokens=20,
    temperature=0.7,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
