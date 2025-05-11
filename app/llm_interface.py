import google.generativeai as genai


genai_client = genai.Client(api_key="AIzaSyAfO8S5sipCLNhMgt70HtpFDrpuI7nanfw")  # Or use os.environ["GOOGLE_API_KEY"]

def query_llm(context, question):
    context_str = "\n".join([doc.page_content for doc in context])
    prompt = f"Use the following context to answer the question:\n\n{context_str}\n\nQuestion: {question}"
    
    response = genai_client.models.generate_content(
        model="gemini-2.0-flash",  # You can also use "gemini-1.5-pro" if supported
        contents=prompt
    )
    return response.text
