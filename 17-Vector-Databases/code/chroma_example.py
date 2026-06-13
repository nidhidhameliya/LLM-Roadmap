import chromadb

# Initialize local in-memory DB
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

# Add docs (Chroma handles embedding via default sentence-transformers)
collection.add(
    documents=["This is a document about AI.", "This is a document about cats."],
    metadatas=[{"topic": "tech"}, {"topic": "pets"}],
    ids=["id1", "id2"]
)

# Search
results = collection.query(
    query_texts=["Tell me about artificial intelligence"],
    n_results=1
)
print("Search Results:", results['documents'])
