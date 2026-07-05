from backend.app.core.singleton import Singleton
from backend.app.processing.embedding_generator import EmbeddingGenerator


class PineconeDB:

    def __init__(self):

        self.index = Singleton.pinecone_index()

        self.embedder = EmbeddingGenerator()

    def upsert_vectors(self, documents):

        texts = [doc["text"] for doc in documents]

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

        query_embedding = self.embedder.generate_embedding(query)

        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )

        return results