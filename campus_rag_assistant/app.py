import os
import uuid
import numpy as np
import chromadb

from PyPDF2 import PdfReader

from sentence_transformers import SentenceTransformer

# Load Embedding Model
print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
client = chromadb.PersistentClient(path="./vectordb")

collection = client.get_or_create_collection(name="campus_documents")

# PDF Text Extraction
def extract_pdf_text(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text

# Chunking
def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


# Load Documents
documents_path = "documents"
all_chunks = []

print("\nProcessing PDFs...\n")
for filename in os.listdir(documents_path):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(documents_path, filename)
        print(f"Reading: {filename}")
        text = extract_pdf_text(pdf_path)
        chunks = chunk_text(text)

        for chunk in chunks:
            all_chunks.append({ "text": chunk, "source": filename})

print(f"\nTotal chunks created: {len(all_chunks)}")

# Store Embeddings
print("\nGenerating embeddings...")

for chunk in all_chunks:
    embedding = model.encode(chunk["text"])
    collection.add(
        documents=[chunk["text"]],
        embeddings=[embedding.tolist()],
        ids=[str(uuid.uuid4())],
        metadatas=[{
            "source": chunk["source"]
        }]
    )

print("\nEmbeddings stored.")


# RAG Question Function
def ask_question(question):
    print("\n" + "=" * 60)
    print(f"Question: {question}")
    
    # Generate query embedding
    query_embedding = model.encode(question)

    # Retrieve relevant chunks
    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=5
    )

    docs = results["documents"][0]

    metadata = results["metadatas"][0]

    print("\nRetrieved Chunks:\n")

    # Re-ranking
    reranked = []
    for doc, meta in zip(docs, metadata):
        doc_embedding = model.encode(doc)
        similarity = np.dot(
            query_embedding,
            doc_embedding
        ) / (
            np.linalg.norm(query_embedding)
            * np.linalg.norm(doc_embedding)
        )

        reranked.append({
            "doc": doc,
            "score": similarity,
            "source": meta["source"]
        })

    reranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # Final Answer
    best = reranked[0]

    print(f"Source: {best['source']}")
    print(f"Similarity Score: {best['score']:.4f}")

    print("\nAnswer:\n")
    print(best["doc"])

# Test Questions
ask_question("What is the late assignment policy?")
ask_question("Who should I contact for transcript issuance?")
ask_question("What are the hostel rules?")