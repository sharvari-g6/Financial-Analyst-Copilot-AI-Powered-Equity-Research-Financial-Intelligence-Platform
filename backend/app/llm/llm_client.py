from backend.app.core.singleton import Singleton


class LLMClient:

    def __init__(self):

        self.client = Singleton.ollama_client()

        self.model = "llama3.1:8b"

    def generate(self, prompt: str):

        response = self.client.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response["message"]["content"]