from app.embeddings.vector_store import vector_store

def embed_and_store(texts: list[str], metadata: dict):
    metadatas = [{**metadata} for _ in texts]

    vector_store.add_texts(
        texts=texts,
        metadatas=metadatas
    )