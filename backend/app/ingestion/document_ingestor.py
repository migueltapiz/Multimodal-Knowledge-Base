from langchain_community.document_loaders import TextLoader
from app.utils.chunking import chunk_text
from app.embeddings.embedder import embed_and_store
from app.core.logging import logger

def ingest_document(file_path: str):
    loader = TextLoader(file_path)
    docs = loader.load()

    chunks = chunk_text(docs[0].page_content)

    logger.info(f"Ingesting document: {file_path}")

    embed_and_store(
        chunks,
        metadata={
            "source": "document",
            "filename": file_path
        }
    )
