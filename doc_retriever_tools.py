#pip install lark

import os
#from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever

from model_loader import get_llm, db
from constants import METADATA_INFO_GENERAL

DB_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data_base')

## Self Query Retriever
def self_query_retriever(metadata_field_info = METADATA_INFO_GENERAL):
    document_content_description = "Content of the document"
    # Load LLM
    llm = get_llm()
    # Setup retriever
    retriever = SelfQueryRetriever.from_llm(
        llm = llm,
        vectorstore = db,
        document_contents = document_content_description,
        metadata_field_info = metadata_field_info,
        verbose=True,
        search_kwargs={"k": 4}
    )
    return retriever

## Test code
"""
retriever = self_query_retriever(METADATA_INFO_GENERAL)
result = retriever.get_relevant_documents("give me information about biden in unreliable sources")
print(result)
"""
