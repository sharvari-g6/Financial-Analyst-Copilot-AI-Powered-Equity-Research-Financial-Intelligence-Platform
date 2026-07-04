from backend.app.database.pinecone_db import PineconeDB


class Retriever:

    def __init__(self):

        self.vector_db = PineconeDB()

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        results = self.vector_db.search_vectors(
            query=query,
            top_k=top_k
        )

        documents = []

        if hasattr(results, "matches"):

            for match in results.matches:

                documents.append({

                    "score": match.score,

                    "text": match.metadata["text"],

                    "company": match.metadata["company"],

                    "year": match.metadata["year"],

                    "chunk_id": match.metadata["chunk_id"]

                })

        return documents