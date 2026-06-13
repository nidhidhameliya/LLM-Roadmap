import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleMoERouter(nn.Module):
    def __init__(self, d_model, num_experts, top_k):
        super().__init__()
        self.router = nn.Linear(d_model, num_experts, bias=False)
        self.top_k = top_k
        
    def forward(self, x):
        # x shape: [batch, seq_len, d_model]
        logits = self.router(x)
        probs = F.softmax(logits, dim=-1)
        top_k_probs, top_k_indices = torch.topk(probs, self.top_k, dim=-1)
        return top_k_probs, top_k_indices

router = SimpleMoERouter(d_model=512, num_experts=8, top_k=2)
x = torch.randn(1, 10, 512) # batch=1, seq=10, dim=512
probs, indices = router(x)
print("Routed Experts for first token:", indices[0, 0])
