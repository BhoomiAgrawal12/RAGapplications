from llama_index.core import SimpleDirectoryReader
import sys
from exceptions import customexception
from logger import logging
import os 
def load_data(uploaded_file):
    try:
        logging.info("data loading started...")
        if uploaded_file is not None:
            save_path = os.path.join("text", uploaded_file.name) 
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            logging.info(f"File {uploaded_file.name} saved successfully.")

        loader = SimpleDirectoryReader("text")
        documents=loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)



    