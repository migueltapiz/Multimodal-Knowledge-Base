from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def healt_check():
    return {"status": "ok"}