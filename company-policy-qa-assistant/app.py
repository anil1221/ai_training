from sentence_transformers import SentenceTransformer
import chromadb
import numpy as np

# Loading embedding model
print("Loading model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Load policies
with open("policies.txt", "r") as file:
    text = file.read()

# Chunking
chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]

# print("\nPolicy Chunks:\n")

# for chunk in chunks:
#     print(chunk)
#     print()

# Generating embeddings
print("Generating embeddings...")

embeddings = model.encode(chunks)

# Create ChromaDB client
client = chromadb.Client()

collection = client.create_collection(
    name="company_policies"
)

# Store embeddings
for index, chunk in enumerate(chunks):

    collection.add(
        documents=[chunk],
        embeddings=[embeddings[index].tolist()],
        ids=[str(index)]
    )

print("\nEmbeddings stored successfully")


def ask_question(question):
    print("\n" + "=" * 50)
    print(f"Question: {question}")

    # Query embedding
    query_embedding = model.encode(question)

    # Similarity search
    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=3
    )

    retrieved_docs = results["documents"][0]

    # print("\nRetrieved Results:\n")
    # for doc in retrieved_docs:
    #     print(doc)
    #     print()

    # Re-ranking optimization
    reranked_results = []

    for doc in retrieved_docs:

        doc_embedding = model.encode(doc)

        similarity = np.dot(
            query_embedding,
            doc_embedding
        ) / (
            np.linalg.norm(query_embedding)
            * np.linalg.norm(doc_embedding)
        )

        reranked_results.append(
            (doc, similarity)
        )

    reranked_results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    # print("Re-ranked Results:\n")
    # for doc, score in reranked_results:

    #     print(
    #         f"Similarity Score: "
    #         f"{score:.4f}"
    #     )

    #     print(doc)
    #     print()

    # Final answer
    best_answer = reranked_results[0][0]

    # print("Final Answer:\n")
    print(f"Answer: {best_answer}")


# Test questions
ask_question("Can employees work remotely?")

ask_question("Do we need MFA?")

ask_question("Can I install personal software?")