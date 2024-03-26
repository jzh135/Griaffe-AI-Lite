#pip install sentence_transformers
import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from chromadb.config import Settings
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from constants import BEG_EN, DB_DIRECTORY, API_KEY

CHROMA_SETTINGS = Settings(
    anonymized_telemetry=False,
    is_persistent=True,
)

def get_openai_embeddings():
    return OpenAIEmbeddings(model="text-embedding-3-small", api_key = API_KEY)

def get_llm():
    return ChatOpenAI(model='gpt-3.5-turbo-0125', temperature = 0.2, openai_api_key = API_KEY)

def get_template():
    template = """Question: {question} 
    Answer: Let's think step by step."""
    return template

def get_db_en():
    embeddings = en_embeddings
    return Chroma(persist_directory=DB_DIRECTORY, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)

en_embeddings = get_openai_embeddings()
print("embedder is loaded")
db = get_db_en()