from app.embeddings.vector_store import vector_store

def embed_and_store(
    texts: list[str],
    metadatas: list[dict] | None = None
):
    if metadatas is None:
        metadatas = [{} for _ in texts]

    vector_store.add_texts(
        texts=texts,
        metadatas=metadatas
    )
