# Conceptual Semantic Cache
import numpy as np

cache = [] # List of tuples: (embedding_vector, text_response)

def get_cached_response(query_embedding, threshold=0.95):
    for cached_emb, response in cache:
        sim = np.dot(query_embedding, cached_emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(cached_emb))
        if sim > threshold:
            return response
    return None

def update_cache(query_embedding, response):
    cache.append((query_embedding, response))
