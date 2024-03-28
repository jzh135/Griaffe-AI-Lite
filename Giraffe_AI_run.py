import os
from datetime import datetime

from model_loader import db
from constants import SOURCE_DIRECTORY, METADATA_INFO_GENERAL
from db_builder_tools import db_update, metadata_file_generator
from chatbot_tools import chatbot_qa_chain
from doc_retriever_tools import self_query_retriever
from db_checker import generate_report, len_of_db, remove_docs
welcome_message = """
🦒 Welcome to Giraffe AI Lite! 🦒
"""

goodbye_message = """
🦒 Farewell, dear friend! 🦒
"""
main_message = """
🦒 Main Menu 🦒
1. Document Retrieval
2. Talk to GG
3. Database Builder
4. Database Manager 
"""

def main_menu():
    while True:
        print(main_message)
        selection = input("Please enter your selection (1/2/3/d) or exit: ")
        if selection == '1':
            doc_retrive_menu()
        elif selection == '2':
            chatbot_menu()
        elif selection == '3':
            metadata_file_generator(SOURCE_DIRECTORY)
            user_message = input("\nTake your time to fill the metadata form!\nWhen you are ready, please enter 'yes' to continue: ")
            if user_message is not None:
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print('end', f"\n{current_time} > Embedder is loaded\n")
                db_update(db=db, source_directory=SOURCE_DIRECTORY)
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print('end', f"\n{current_time} > Database is updated\n")
        elif selection == "4":
            len_of_db(db)
            usr_report = input("Please enter 'report' to generate full report or 'remove' to remove a document: ")
            if usr_report == "report":
                generate_report(db)
                print("Report is generated")
            elif usr_report == "remove":
                target_doc = input("Please enter the title of the document to be removed: ")
                remove_docs(db, target_doc)
            else:
                print("Invalid input -- exit the loop")
        elif selection == "exit":
            print(goodbye_message)
            return None
        else:
            print("\n>>>Invlid input<<<\n")


def doc_retrive_menu():
    while True:
        query = input("\nEnter the query (or exit): ")
        if query == "exit":
            break
        filter = input("\nEnter the filter: ")
        usr_input = "query: " + query + " filter: " + filter
        # Get the answer from the chain
        retriever = self_query_retriever(METADATA_INFO_GENERAL)
        docs = retriever.get_relevant_documents(usr_input)
        print("\n> Giraffe 🦒:")
        for document in docs:
            print("\n> " + document.metadata["source"] + ":")
            print(document.page_content)
            print("--------------------------------------------------------------------------")

def chatbot_menu():
    while True:
        query = input("\nEnter the query (or exit): ")
        if query == "exit":
            break
        filter = input("\nEnter the filter: ")
        usr_input = "query: " + query + " filter: " + filter
        # Get the answer from the chain
        qa = chatbot_qa_chain()
        res = qa(usr_input)
        answer, docs = res["result"], res["source_documents"]

        # Print the result
        print("\n\n> Question:")
        print(usr_input)
        print("\n> Giraffe 🦒:")
        print(answer)
        # Print the source documents
        print("----------------------------------SOURCE DOCUMENTS---------------------------")
        for document in docs:
            print("\n> " + document.metadata["source"] + ":")
            print(document.page_content)
            print("--------------------------------------------------------------------------")
if __name__ == "__main__":
    print(welcome_message)
    main_menu()
