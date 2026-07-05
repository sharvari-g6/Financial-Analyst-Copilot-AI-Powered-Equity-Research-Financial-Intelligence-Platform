from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import ollama

from backend.app.core.config import settings


class Singleton:

    _embedding_model = None

    _pinecone = None
    _index = None

    _ollama_client = None

    @classmethod
    def embedding_model(cls):

        if cls._embedding_model is None:

            print("Loading Embedding Model...")

            cls._embedding_model = SentenceTransformer(
                "BAAI/bge-small-en-v1.5"
            )

        return cls._embedding_model

    @classmethod
    def pinecone_index(cls):

        if cls._index is None:

            print("Connecting to Pinecone...")

            if cls._pinecone is None:

                cls._pinecone = Pinecone(
                    api_key=settings.PINECONE_API_KEY
                )

            cls._index = cls._pinecone.Index(
                settings.PINECONE_INDEX_NAME
            )

        return cls._index

    @classmethod
    def ollama_client(cls):

        if cls._ollama_client is None:

            print("Initializing Ollama Client...")

            cls._ollama_client = ollama.Client()

        return cls._ollama_client