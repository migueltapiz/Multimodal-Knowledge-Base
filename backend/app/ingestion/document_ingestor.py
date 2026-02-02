import os
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredMarkdownLoader,
)
from app.utils.chunking import chunk_text
from app.embeddings.embedder import embed_and_store
from app.core.logging import logger


def get_loader(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        return TextLoader(file_path, encoding="utf-8")

    if ext == ".pdf":
        return PyPDFLoader(file_path)

    if ext in [".docx", ".doc"]:
        return UnstructuredWordDocumentLoader(file_path)

    if ext in [".md", ".markdown"]:
        return UnstructuredMarkdownLoader(file_path)

    raise ValueError(f"Unsupported file type: {ext}")


def ingest_document(file_path: str, original_filename: str):
    logger.info(f"Ingesting document: {original_filename}")

    loader = get_loader(file_path)
    docs = loader.load()

    all_chunks = []

    for doc_index, doc in enumerate(docs):
        chunks = chunk_text(doc.page_content)

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "text": chunk,
                "metadata": {
                    "source": "document",
                    "filename": original_filename,
                    "page": doc.metadata.get("page", doc_index),
                    "chunk": i
                }
            })
    
    texts = [chunk["text"] for chunk in all_chunks]
    metadatas = [chunk["metadata"] for chunk in all_chunks]

    embed_and_store(texts, metadatas)

    logger.info(
        f"Document ingested: {original_filename} "
        f"({len(all_chunks)} chunks)"
    )
