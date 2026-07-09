from pydantic import BaseModel


class UploadResponse(BaseModel):

    status: str

    company: str

    chunks: int

    message: str