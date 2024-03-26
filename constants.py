import os
from langchain.chains.query_constructor.base import AttributeInfo

# Import OpenAI API Key from a file
def read_api_key_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            api_key = file.read().strip()  # Read the content and remove leading/trailing spaces
            return api_key
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Document Directory
SOURCE_DIRECTORY = os.path.join(os.path.dirname(__file__), 'source')
ARCHIVE_DIRECTORY = os.path.join(os.path.dirname(__file__), 'archive')
METADATA_DIRECTORY = os.path.join(ARCHIVE_DIRECTORY, 'metadata')
ARCHIVE_SOURCE_DIRECTORY = os.path.join(ARCHIVE_DIRECTORY, 'source files')

# Audio Directory
AUDIO_ROOT = os.path.join(os.path.dirname(__file__), 'audio_docs')
AUDIO_SOURCE = os.path.join(AUDIO_ROOT, 'audio_source')
TRANSCRIPTION = os.path.join(AUDIO_ROOT, 'transcription')

# Database Directory
DB_DIRECTORY = os.path.join(os.path.dirname(__file__), 'db_en')

# OpenAI API Key 
API_KEY_FILE = os.path.join(os.path.dirname(__file__), 'openAI_API.txt')
API_KEY = read_api_key_from_file(API_KEY_FILE)

# Report Directory
REPORT_DIRECTORY = os.path.join(os.path.dirname(__file__), 'report')

# Check if essential directories exist
for folder_path in [SOURCE_DIRECTORY, ARCHIVE_DIRECTORY, METADATA_DIRECTORY, ARCHIVE_SOURCE_DIRECTORY, AUDIO_ROOT, AUDIO_SOURCE, TRANSCRIPTION, DB_DIRECTORY, REPORT_DIRECTORY]:
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    else:
        pass

# Metadata Info
METADATA_INFO_GENERAL = [
        AttributeInfo(
            name="title",
            description="Book name or artical title",
            type="string",
        ),
        AttributeInfo(
            name="author",
            description="auther of this book or article",
            type="string",
        ),
        AttributeInfo(
            name="chapter",
            description="Document type (or property), such as [Safety Report] or [Design Description]",
            type="string",
        ),
        AttributeInfo(
            name="reliable", 
            description="Reliability of the information source: True = reliable, False = unreliable", 
            type="bool"
        ),
        AttributeInfo(
            name="source", 
            description="full name with extension of this book or article", 
            type="string"
        )
    ]
