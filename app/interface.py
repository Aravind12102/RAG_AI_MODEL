import streamlit as st
from agent import route_query
from vector_store import load_vector_store

st.title("Multi-Agent Q&A Assistant")
query = st.text_input("Enter your question:")

if query:
    vector_store = load_vector_store()
    log, answer = route_query(query, vector_store)
    st.write("**Decision Log:**", log)
    st.write("**Answer:**", answer)
