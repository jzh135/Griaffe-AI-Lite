import os
import shutil
import json

from langchain.docstore.document import Document
from langchain_community.document_loaders import TextLoader
from langchain.document_loaders.pdf import PyMuPDFLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from datetime import datetime

from model_loader import db
from constants import SOURCE_DIRECTORY, METADATA_DIRECTORY, ARCHIVE_SOURCE_DIRECTORY

TEMP_METADATA_PATH = os.path.join(SOURCE_DIRECTORY, "documents_metadata.json")

def db_update_single(file_path,db):
    ## Get database list of ids and metadata
    db_dic = db.get()
    ids_list = db_dic["ids"]
    meta_list = db_dic["metadatas"]
    ## Load and split new document
    # Get file extension and file name
    file_extension = os.path.splitext(file_path)[1]
    # Select document loader
    loader = loader_selection(file_extension=file_extension, file_path=file_path)
    if loader is None:
        return None
    else:
        pages = loader.load()
    # Initialize new_doc
    new_doc = [Document]
    new_doc[0].page_content = ""
    new_doc[0].metadata = pages[0].metadata
    #print(loaded_metadata[file_path])
    loaded_metadata = metadata_loader(TEMP_METADATA_PATH)
    new_doc[0].metadata = loaded_metadata[file_path]
    # Merge all pages to one page
    for page in pages:
            new_doc[0].page_content = new_doc[0].page_content + page.page_content
    # Split document
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
    new_doc_slices = text_splitter.split_documents(new_doc)
    ## Check if the new document file name is existed in the database and remove the duplicate old document vectors
    i = 0
    for slice_meta_data in meta_list:
        print("-------------------")
        print(file_path)
        print(slice_meta_data['source'])
        print("--------------------")
        if slice_meta_data['source'] in file_path:
            ids = ids_list[i]
            print(f"Existed document slice with ids = {ids} from file {file_path} is removed from the database")
            db.delete(ids)
        i = i+1
    print(new_doc_slices)
    ## Add new document slices to database
    print(f"{len(new_doc_slices)} slices are loaded successfully")
    db.add_documents(new_doc_slices)
    print(f"New document {file_path} is added to the database")
    return None
    

def db_update(db,source_directory):
    for root, _, files in os.walk(source_directory):
        for file_name in files:
            #file_extension = os.path.splitext(file_name)[1]
            source_file_path = os.path.join(root, file_name)
            # Remove duplicate files and get new document slices
            db_update_single(file_path=source_file_path, db=db)
    """
    # Move source file to the archive folder
    for root, _, files in os.walk(source_directory):
        for file_name in files:
            source_file_path = os.path.join(root, file_name)
            archive_source_file =  os.path.join(ARCHIVE_SOURCE_DIRECTORY, file_name)
            # Delete the old file in archive folder
            if os.path.exists(archive_source_file):
                os.remove(archive_source_file)
                print(f"{file_name} in {ARCHIVE_SOURCE_DIRECTORY} was successfully deleted.")
            else:
                print(f"{file_name} does not exist in {ARCHIVE_SOURCE_DIRECTORY}.")
            # Add new file to archive folder
            shutil.move(source_file_path, ARCHIVE_SOURCE_DIRECTORY)
    """      
    return None

def loader_selection(file_extension, file_path):
    if file_extension == ".txt":
        loader = TextLoader(file_path,encoding='utf-8') # If not specific encoding, it will have rise UnicodeDecodeError
    elif file_extension == ".pdf":
        print("loading")
        loader = PyMuPDFLoader(file_path)
    else:
        print(f"{file_path} is not supported")
        loader = None
    return loader

def metadata_file_generator(source_directory):
    metadata_dict = {}
    for root, _, files in os.walk(source_directory):
        for file in files:
            #file_path = os.path.join(root, file)
            metadata = metadata_init(file)
            metadata_dict.update(metadata)
    # Save the metadata dictionary to a JSON file
    with open(TEMP_METADATA_PATH, "w") as json_file:
        json.dump(metadata_dict, json_file, indent=4)
    print(f"Metadata for all files in {source_directory} has been saved to documents_metadata.json")
    return None

def metadata_init(file_path):
    general = {
        os.path.join(SOURCE_DIRECTORY, file_path): {
            "title": os.path.splitext(file_path)[0],
            "author": "",
            "chapter": "",
            "reliable":True,
            "source":file_path
        }
    }
    return general 

def metadata_loader(file_path):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

 ## Test code
"""
if __name__ == "__main__":
    metadata_file_generator(SOURCE_DIRECTORY)
    db_update(db=db, source_directory=SOURCE_DIRECTORY)
    #template = metadata_init("iVPI-ACO2-HwSAV.docx")
    #print(template)
    metadata_file_generator(SOURCE_DIRECTORY)
    metadata_dict = metadata_loader(TEMP_METADATA_PATH)
    if metadata_dict:
        print("Metadata loaded successfully:")
"""