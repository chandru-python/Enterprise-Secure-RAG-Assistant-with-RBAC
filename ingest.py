import os
import json
import pandas as pd

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# ============================================
# EMBEDDING MODEL
# ============================================

print("\nLOADING EMBEDDING MODEL...\n")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("EMBEDDING MODEL LOADED SUCCESSFULLY\n")

# ============================================
# DATASET PATH
# ============================================

BASE_PATH = "datasets"

documents = []

# ============================================
# LOAD DATASETS
# ============================================

print("===================================")
print("LOADING DATASETS")
print("===================================\n")

# CHECK DATASET FOLDER
if not os.path.exists(BASE_PATH):

    print(f"ERROR : '{BASE_PATH}' folder not found")
    exit()

# LOOP THROUGH DATASET FOLDERS
for folder in os.listdir(BASE_PATH):

    folder_path = os.path.join(BASE_PATH, folder)

    # SKIP NON-FOLDERS
    if not os.path.isdir(folder_path):
        continue

    print(f"\nPROCESSING FOLDER : {folder}")

    # LOOP THROUGH FILES
    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        text = ""

        try:

            # ============================================
            # TXT FILES
            # ============================================

            if file.endswith(".txt"):

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    text = f.read()

            # ============================================
            # CSV FILES
            # ============================================

            elif file.endswith(".csv"):

                df = pd.read_csv(file_path)

                text = df.to_string(index=False)

            # ============================================
            # JSON FILES
            # ============================================

            elif file.endswith(".json"):

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    data = json.load(f)

                    text = json.dumps(
                        data,
                        indent=2
                    )

            else:
                continue

            # SKIP EMPTY FILES
            if text.strip() == "":

                print(f"EMPTY FILE SKIPPED : {file}")
                continue

            # ============================================
            # CREATE DOCUMENT
            # ============================================

            doc = Document(
                page_content=text,
                metadata={
                    "source": file,
                    "department": folder,
                    "path": file_path
                }
            )

            documents.append(doc)

            print(f"LOADED : {file}")

        except Exception as e:

            print(f"\nERROR READING FILE : {file}")
            print(e)

# ============================================
# DOCUMENT SUMMARY
# ============================================

print("\n===================================")
print(f"TOTAL DOCUMENTS LOADED : {len(documents)}")
print("===================================\n")

# CHECK DOCUMENTS
if len(documents) == 0:

    print("NO DOCUMENTS FOUND")
    exit()

# ============================================
# TEXT SPLITTING
# ============================================

print("CREATING TEXT CHUNKS...\n")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("===================================")
print(f"TOTAL CHUNKS CREATED : {len(chunks)}")
print("===================================\n")

# ============================================
# CREATE VECTOR DATABASE
# ============================================

print("CREATING FAISS VECTOR DATABASE...\n")

try:

    vectorstore = FAISS.from_documents(
        chunks,
        embedding_model
    )

    # CREATE VECTOR STORE DIRECTORY
    os.makedirs(
        "vector_store",
        exist_ok=True
    )

    # SAVE VECTOR DATABASE
    vectorstore.save_local(
        "vector_store"
    )

    print("===================================")
    print("FAISS VECTOR DATABASE CREATED")
    print("===================================\n")

except Exception as e:

    print("\nERROR CREATING VECTOR DATABASE")
    print(e)
