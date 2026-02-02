from fastapi import APIRouter, UploadFile, File, HTTPException
from app.ingestion.document_ingestor import ingest_document
import tempfile
import os

router = APIRouter()

@router.post("/document")
async def ingest_document_endpoint(file: UploadFile = File(...)):
    try:
        suffix = os.path.splitext(file.filename)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        ingest_document(
            file_path=tmp_path,
            original_filename=file.filename
        )

        return {
            "status": "document ingested",
            "filename": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if "tmp_path" in locals() and os.path.exists(tmp_path):
            os.remove(tmp_path)
