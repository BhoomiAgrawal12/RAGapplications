#code for openai
# import llama_index
# from llama_index.core import VectorStoreIndex
# from dotenv import load_dotenv
# import os
# from llama_index.readers.web import SimpleWebPageReader

# load_dotenv()
# def main(url: str)->None:
#     document=SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
#     index=VectorStoreIndex.from_documents(documents=document)
#     query_engine=index.as_query_engine()
#     response=query_engine.query("What is the web page about?")
#     print(response)

# if __name__=="__main__":
#     main(url="https://www.amazon.in/")


#code for gemini
from llama_index.readers.web import SimpleWebPageReader
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_webpage_text(url: str) -> str:
    documents = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
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
    response = query_gemini(webpage_text, "What is the web page about?")
    print(response)

if __name__ == "__main__":
    main(url="https://www.amazon.in/")