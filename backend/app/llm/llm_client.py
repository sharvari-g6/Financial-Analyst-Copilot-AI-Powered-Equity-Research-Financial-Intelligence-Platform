from langchain_ollama import ChatOllama


class LLMClient:

    def __init__(self):

        self.llm = ChatOllama(

            model="llama3.1:8b",

            temperature=0.2

        )

    def generate(self, prompt: str):

        response = self.llm.invoke(prompt)

        return response.content