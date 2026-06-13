from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load & Chunk (Simulated text)
text = "RAG combines retrieval and generation. It reduces hallucinations."
splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
chunks = splitter.create_documents([text])

for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk.page_content}")

# Note: Full RAG requires embedding models and a vector DB (e.g., Chroma).
# See mini-project for full implementation expectations.
