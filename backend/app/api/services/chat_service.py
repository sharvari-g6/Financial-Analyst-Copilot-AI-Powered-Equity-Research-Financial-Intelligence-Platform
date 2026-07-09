from backend.app.core.services import query_engine


class ChatService:

    def ask(
        self,
        question: str
    ):

        result = query_engine.ask(

            question=question,

            top_k=10

        )

        return {

            "answer": result["answer"]

        }