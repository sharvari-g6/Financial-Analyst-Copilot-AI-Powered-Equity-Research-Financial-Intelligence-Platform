from fastapi import APIRouter

from backend.app.api.schemas.chat import (
    ChatRequest,
    ChatResponse
)

from backend.app.api.services.chat_service import ChatService


router = APIRouter()

service = ChatService()


@router.post(
    "/chat",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):

    result = service.ask(

        question=request.question

    )

    return result