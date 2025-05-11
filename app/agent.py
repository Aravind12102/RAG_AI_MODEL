from tools.calculator import calculate
from tools.dictionary import define
from app.retriever import retrieve
from app.llm_interface import query_llm

def route_query(query, vector_store):
    decision_log = []

    if any(word in query.lower() for word in ["calculate", "compute", "+", "-", "*", "/"]):
        decision_log.append("Routed to calculator")
        return decision_log, calculate(query)

    elif any(word in query.lower() for word in ["define", "meaning of"]):
        term = query.replace("define", "").strip()
        decision_log.append("Routed to dictionary")
        return decision_log, define(term)

    else:
        decision_log.append("Routed to RAG pipeline")
        docs = retrieve(query, vector_store)
        answer = query_llm(docs, query)
        return decision_log, answer
