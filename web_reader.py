import llama_index

from llama_index.llms.openai import OpenAI
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex

import os
from dotenv import load_dotenv

load_dotenv()

def main(url):
    document = SimpleWebPageReader(html_to_text = True).load_data([url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    result = query_engine.query("What courses they provide?")
    print(result)

if __name__ == "__main__":
    main(url="https://www.pce.ac.in/")

