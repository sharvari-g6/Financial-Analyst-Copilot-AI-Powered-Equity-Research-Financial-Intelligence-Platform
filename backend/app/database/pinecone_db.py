from pinecone import Pinecone

from backend.app.core.config import settings


class PineconeDB:
    """
    Handles all interactions with the Pinecone vector database.
    """

    def __init__(self):
        """
        Initialize Pinecone client and connect to the index.
        """

        self.pc = Pinecone(
            api_key=settings.PINECONE_API_KEY
        )

        self.index = self.pc.Index(
            settings.PINECONE_INDEX_NAME
        )

    def get_index(self):
        """
        Return the Pinecone index object.
        """

        return self.index

    def get_index_stats(self):
        """
        Return statistics of the Pinecone index.
        """

        return self.index.describe_index_stats()