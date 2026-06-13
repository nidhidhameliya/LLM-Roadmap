import numpy as np

# Dot product / Cosine Similarity
v1 = np.array([1, 0, 1])
v2 = np.array([0, 1, 1])
dot = np.dot(v1, v2)
norm = np.linalg.norm(v1) * np.linalg.norm(v2)
cosine_sim = dot / norm
print(f"Cosine Similarity: {cosine_sim:.4f}")

# Softmax
logits = np.array([2.0, 1.0, 0.1])
exp_logits = np.exp(logits - np.max(logits)) # stability
probs = exp_logits / np.sum(exp_logits)
print(f"Softmax Probs: {probs}")
