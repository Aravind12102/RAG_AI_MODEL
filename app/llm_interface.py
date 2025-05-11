import google.generativeai as genai
import os


genai_client = os.environ["G_API_KEY"]

def query_llm(context, question):
    context_str = "\n".join([doc.page_content for doc in context])
    prompt = f"Use the following context to answer the question:\n\n{context_str}\n\nQuestion: {question}"
    
    response = genai_client.models.generate_content(
        model="gemini-2.0-flash",  
        contents=prompt
    )
    return response.text
