import tiktoken

def calculate_cost(prompt: str, model: str = "gpt-4o"):
    # Load the correct encoding for the model
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(prompt)
    num_tokens = len(tokens)
    
    # Example pricing (fictional placeholder prices)
    cost_per_1k = 0.005 
    total_cost = (num_tokens / 1000) * cost_per_1k
    
    print(f"Tokens: {num_tokens}")
    print(f"Cost: ${total_cost:.5f}")
    return total_cost

calculate_cost("Implement a robust Red-Black tree in Rust.")
