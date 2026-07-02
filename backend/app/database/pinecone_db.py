from pinecone import Pinecone

from backend.app.core.config import settings
from backend.app.processing.embedding_generator import EmbeddingGenerator


class PineconeDB:

    def __init__(self):

        self.pc = Pinecone(
            api_key=settings.PINECONE_API_KEY
        )

        self.index = self.pc.Index(
            settings.PINECONE_INDEX_NAME
        )

        self.embedder = EmbeddingGenerator()

    def upsert_vectors(self, documents):

        # Extract all texts
        texts = [doc["text"] for doc in documents]

        # Generate embeddings in batch
        embeddings = self.embedder.generate_embeddings(texts)

        vectors = []

        for doc, embedding in zip(documents, embeddings):

            vector = {

                "id": (
                    f'{doc["metadata"]["company"]}_'
                    f'{doc["metadata"]["year"]}_'
                    f'chunk_{doc["metadata"]["chunk_id"]}'
                ),

                "values": embedding,

                "metadata": {

                    "company": doc["metadata"]["company"],
                    "year": doc["metadata"]["year"],
                    "document_type": doc["metadata"]["document_type"],
                    "source": doc["metadata"]["source"],
                    "chunk_id": doc["metadata"]["chunk_id"],
                    "text": doc["text"]

                }

            }

            vectors.append(vector)

        self.index.upsert(vectors=vectors)

        return len(vectors)

    def get_index_stats(self):

        return self.index.describe_index_stats()
    

    def search_vectors(
        self,
        query: str,
        top_k: int = 5
    ):

        # Generate embedding for the user's query
        query_embedding = self.embedder.generate_embedding(query)

        # Search Pinecone
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )

        return results