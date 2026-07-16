"""
Load 5 markdown notes from previous days into ChromaDB.
Requires: pip install langchain langchain-community langchain-huggingface langchain-chroma chromadb sentence-transformers
No API key needed — uses a local embedding model.
Run from inside the day-15/ folder so the relative paths below resolve.
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# 5 notes files from previous days
NOTE_FILES = [
    "../day-01/research-notes.md",
    "../day-06/cot-notes.md",
    "../day-09/research-notes.md",
    "../day-12/function-calling-notes.md",
    "../day-13/context-notes.md",
]

def load_and_chunk(paths):
    docs = []
    for path in paths:
        loader = TextLoader(path)
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)


if __name__ == "__main__":
    chunks = load_and_chunk(NOTE_FILES)
    print(f"Loaded {len(chunks)} chunks from {len(NOTE_FILES)} files")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db",
    )
    print("Stored chunks in ChromaDB at ./chroma_db")
