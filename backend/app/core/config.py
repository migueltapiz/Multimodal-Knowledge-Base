from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Multimodal Knowledge Base"
    environment: str = "Developement"

    open_api_key: str

    chroma_persist_dir: str = "./chroma"
    chroma_collection: str = "knowledge_base"

    class Config:
        env_file = ".env"

Settings = Settings()