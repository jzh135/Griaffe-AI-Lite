import os
#from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
#from langchain.chains import RetrievalQA
from langchain.chains.retrieval_qa.base import RetrievalQA

from model_loader import get_llm
from doc_retriever_tools import self_query_retriever
from constants import METADATA_INFO_GENERAL

def chatbot_qa_chain():
    # Prompt template
    template = """Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        {context}

        Question: {question}

        Helpful Answer:"""

    prompt = PromptTemplate.from_template(template)

    # Load LLM
    llm = get_llm()

    # Load retriever
    retriever = self_query_retriever(metadata_field_info = METADATA_INFO_GENERAL)

    # RetrievalQA
    qa = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever, 
        return_source_documents=True,
        verbose=True,
        chain_type_kwargs={
        "prompt": prompt}
        )
    # ChatBot UI
    return qa