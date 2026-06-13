# Minimal KV Cache size estimator
def calculate_kv_cache_gb(layers: int, heads: int, head_dim: int, seq_len: int, batch_size: int, bytes_per_param: int = 2):
    # 2 (for Keys and Values)
    total_bytes = 2 * layers * heads * head_dim * seq_len * batch_size * bytes_per_param
    return total_bytes / (1024 ** 3) # Convert to GB

# Example for a Llama-like 8B model at 8k context, batch size 32
size_gb = calculate_kv_cache_gb(layers=32, heads=32, head_dim=128, seq_len=8192, batch_size=32)
print(f"KV Cache Size: {size_gb:.2f} GB")
