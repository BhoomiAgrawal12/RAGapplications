import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai
from exceptions import customexception
from logger import logging

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def load_model():
    try:
        model=Gemini(model="models/gemini-1.5-pro-latest",api_key=GEMINI_API_KEY)
        return model
    except Exception as e:
        raise customexception(e,sys)
        