import torch
import torch.nn.functional as F

def scaled_dot_product_attention(q, k, v, mask=None):
    d_k = q.size(-1)
    # Q * K^T
    scores = torch.matmul(q, k.transpose(-2, -1)) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
        
    attention_weights = F.softmax(scores, dim=-1)
    output = torch.matmul(attention_weights, v)
    return output, attention_weights

# Example usage
seq_len, d_k = 3, 4
q = torch.randn(1, seq_len, d_k)
k = torch.randn(1, seq_len, d_k)
v = torch.randn(1, seq_len, d_k)

out, weights = scaled_dot_product_attention(q, k, v)
print("Output shape:", out.shape)
