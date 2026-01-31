from fastapi import FastAPI
# from app.api.ingest import router as ingest_router
from app.api.health import router as health_router

app = FastAPI(
    title="Multimodal Knowledge Base API",
    description="Backend for a multimodal developer knowledge base",
    version="0.1.0"
)

app.include_router(health_router, prefix="/health", tags=["Health"])
# app.include_router(ingest_router, prefix="/ingest", tags=["Ingestion"])