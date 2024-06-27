from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex

import os
from dotenv import load_dotenv

load_dotenv()

def main(dir):
    document = SimpleDirectoryReader(dir).load_data()
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    result = query_engine.query("What is generative AI?")
    print(result)

if __name__ == "__main__":
    main(dir="docs/")

