from langchain_community.vectorstores import Chroma
from app.core.config import Settings
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    api_key=Settings.openai_api_key
)

vector_store = Chroma(
    collection_name=Settings.chroma_collection,
    embeddings=embeddings,
    persis_directory=Settings.chroma_persist_dir
)