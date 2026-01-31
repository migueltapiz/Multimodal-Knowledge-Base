import os

# 🔥 Desactiva telemetría de Chroma/PostHog de forma definitiva
os.environ["POSTHOG_DISABLED"] = "1"
os.environ["ANONYMIZED_TELEMETRY"] = "False"

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from app.core.config import Settings

embeddings = OpenAIEmbeddings(
    api_key=Settings.openai_api_key
)

vector_store = Chroma(
    collection_name=Settings.chroma_collection,
    embedding_function=embeddings,
    persist_directory=Settings.chroma_persist_dir
)
