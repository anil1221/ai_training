import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient( path="./vectordb")

collection = client.get_or_create_collection(name="knowledge_base")

# Load Knowledge Base
with open("knowledge_base/python_basics.txt", "r") as file:
    text = file.read()

chunks = text.split("\n")
for index, chunk in enumerate(chunks):
    if chunk.strip():
        embedding = model.encode(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[embedding.tolist()],
            ids=[str(index)]
        )

# Search Tool
def vector_search_tool(query: str):
    query_embedding = model.encode(query)
    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=2
    )

    return results["documents"][0]