from app.ingest import load_and_chunk_documents
from app.vector_store import build_vector_store, save_vector_store

if __name__ == "__main__":
    print("Loading and chunking documents...")
    docs = load_and_chunk_documents(folder="data")  # Use correct folder name if needed
    print(f"Total chunks created: {len(docs)}")
    
    if len(docs) == 0:
        print("No documents were found or processed. Please check the 'data' folder.")
    else:
        print("Building vector store...")
        store = build_vector_store(docs)
        print("Saving vector store...")
        save_vector_store(store)
        print("✅ Vector store built and saved successfully.")
