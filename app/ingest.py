import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
import fitz  
from docx import Document  

def extract_text_from_file(filepath):
    if filepath.endswith(".txt"):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    elif filepath.endswith(".pdf"):
        doc = fitz.open(filepath)
        return "\n".join([page.get_text() for page in doc])
    elif filepath.endswith(".docx"):
        doc = Document(filepath)
        return "\n".join([para.text for para in doc.paragraphs])
    return None

def load_and_chunk_documents(folder='data'):
    os.makedirs(folder, exist_ok=True)  
    all_texts = []

    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        text = extract_text_from_file(full_path)
        if text:
            all_texts.append(text)

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.create_documents(all_texts)




