def retrieve(query, vector_store, k=3):
    return vector_store.similarity_search(query, k=k)
