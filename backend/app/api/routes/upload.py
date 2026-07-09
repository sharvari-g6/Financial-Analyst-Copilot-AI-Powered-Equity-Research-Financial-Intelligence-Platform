from fastapi import APIRouter, UploadFile, File, Form

from backend.app.api.schemas.upload import UploadResponse
from backend.app.api.services.upload_service import UploadService


router = APIRouter()

service = UploadService()


@router.post(
    "/upload",
    response_model=UploadResponse
)
async def upload_document(

    file: UploadFile = File(...),

    company: str = Form(...),

    year: int = Form(...)

):

    result = service.process_upload(

        file=file,

        company=company,

        year=year

    )

    return result