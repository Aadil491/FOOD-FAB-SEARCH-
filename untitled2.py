
!pip install -U langchain-community
!pip install langchain_text_splitters
!pip install langchain-huggingface
!pip install chromadb
!pip install langchain_google_genai
!pip install protobuf
!pip install sentence-transformers

import urllib
import warnings
from pathlib import Path as p
from pprint import pprint

import pandas as pd
from langchain import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
#from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveJsonSplitter

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

import google.generativeai as genai
import os
warnings.filterwarnings("ignore")

from IPython.display import display
from IPython.display import Markdown
import textwrap
import os

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY=" give your api key"
genai.configure(api_key=GOOGLE_API_KEY)



model1 = genai.GenerativeModel(model_name = "gemini-2.0-flash-exp")



response = model1.generate_content("What are the usecases of LLMs?")


to_markdown(response.text)

available_models = genai.list_models()
for model in available_models:
    print(model)

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-002",  # Use the correct model name
    google_api_key=GOOGLE_API_KEY,
    temperature=0.6,
    convert_system_message_to_human=True
)

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

import json

def load_json_file(file_path):
  """Loads a JSON file and returns its content as a Python dictionary.

  Args:
    file_path: The path to the JSON file.

  Returns:
    A Python dictionary representing the JSON data, or None if an error occurs.
  """
  try:
    with open(file_path, 'r') as f:
      data = json.load(f)
    return data
  except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    return None
  except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in {file_path}")
    return None

# Example usage:
file_path = '/content/menu_incoming_json_log.json' # Replace with your file path
data = load_json_file(file_path)

import json
pages = RecursiveJsonSplitter(max_chunk_size =1500)
#documents = pages.split_text(json.dumps(data))
document = pages.split_text(data)
len(document)
print(document[0])

from langchain.docstore.document import Document

texts = [Document(page_content=d) for d in document]

texts = list(map(lambda x: x.page_content.replace("\n", " "), texts))

"""**Creating Vector Index:** A vector index is created from the texts using Chroma and embeddings."""

vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k":5})

template = """
You are an expert virtual assistant with a friendly and professional tone. Use the provided information to answer the question thoughtfully and accurately. If the answer is not available, please say so honestly. Conclude every response with a positive note.

Here is the context:
{context}

Question: {question}

Detailed and Helpful Answer:
"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)# Run chain

"""**Initializing QA Chain:** The QA chain is set up with the model and vector index."""

qa_chain = RetrievalQA.from_chain_type(
    model,
    retriever=vector_index,
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

question = "give variety of jain thali food"
result = qa_chain({"query": question})
Markdown(result["result"])

