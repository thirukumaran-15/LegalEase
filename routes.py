from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()
generator = GeminiDocumentGenerator()

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    effective_date: str

@router.post("/generate")
def generate_document(request: DocumentRequest):
    try:
        text = generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            effective_date=request.effective_date,
        )
        return {"document": text}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
