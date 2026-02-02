from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.rag.query_engine import query_knowledge_base

router = APIRouter()

class QueryRequest(BaseModel):
    question: str
    k: int = 4

@router.post("/answer")
async def query_knowledge_base_endpoint(payload: QueryRequest):
    try:
        result = query_knowledge_base(
            question=payload.question,
            k=payload.k
        )
        
        return {
            "status": "query processed",
            "answer": result["answer"],
            "sources": result["sources"]
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )