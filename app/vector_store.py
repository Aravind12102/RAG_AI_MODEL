import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.environ["API_KEY"]  # Explicitly reference env var
)

def build_vector_store(docs):
    texts = [doc.page_content for doc in docs]  # Extract plain text
    return FAISS.from_texts(texts, embedding)

def save_vector_store(store, path="vector_store_index"):
    store.save_local(path)

def load_vector_store(path="vector_store_index"):
    return FAISS.load_local(path, embeddings=embedding)

