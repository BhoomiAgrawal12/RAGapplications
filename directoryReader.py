# from llama_index.readers.web import SimpleWebPageReader
import google.generativeai as genai
import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_webpage_text(url: str) -> str:
    documents = SimpleDirectoryReader(url).load_data()
    if documents:
        return documents[0].text  
    return "No content extracted from the webpage."

def query_gemini(content: str, query: str) -> str:
    model = genai.GenerativeModel("gemini-pro") 
    
    prompt = f"Here is the webpage content:\n\n{content}\n\nQuestion: {query}"
    
    response = model.generate_content(prompt)
    
    return response.text if hasattr(response, "text") else "No response received."

def main(url: str):
    webpage_text = get_webpage_text(url)
    response = query_gemini(webpage_text, "summarise the text")
    print(response)

if __name__ == "__main__":
    file_path = "/media/bhoomi/New Volume/CodesLinux/QueansRAG"
    main(url=file_path)