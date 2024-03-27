import os
import csv

from constants import REPORT_DIRECTORY

def generate_report(db):
    # Load all docs in vector database
    doc_list = db.get()

    # Load ids list
    ids_list = doc_list["ids"]

    # Load metadata list of dictionaries
    meta_list = doc_list["metadatas"]

    # Load each item's list from metadata
    title_list = [item["title"] for item in meta_list]
    author_list = [item["author"] for item in meta_list]
    reliable_list = [item["reliable"] for item in meta_list]
    source_list = [item["source"] for item in meta_list]

    # Create a list of tuples (each tuple represents a row)
    rows = list(zip(title_list, author_list, reliable_list, source_list, ids_list))

    # Define the CSV file path
    csv_file = os.path.join(REPORT_DIRECTORY, "db_report.csv")

    # Write the data to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["title", "author", "reliable", "source", "ids"])  # Write header
        writer.writerows(rows)  # Write rows

def len_of_db(db):
    doc_list = db.get()
    ids_list = doc_list["ids"]
    print(f"There are {len(ids_list)} slices of documents in the database")

def remove_docs(db, target_title):
    doc_list = db.get()
    # Load ids list
    ids_list = doc_list["ids"]
    # Load metadata list of dictionaries
    meta_list = doc_list["metadatas"]
    # Load each item's list from metadata
    title_list = [item["title"] for item in meta_list]
    target_ids = []
    for i in range(len(title_list)):
        if target_title == title_list[i]:
            target_ids.append(ids_list[i])
    db.delete(target_ids)
    print(f"{len(target_ids)} slices of documents are removed from the vector database")
