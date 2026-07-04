class CitationEngine:

    @staticmethod
    def build_citations(documents):

        citations = []

        for doc in documents:

            citations.append({

                "company": doc["company"],

                "year": doc["year"],

                "chunk_id": doc["chunk_id"],

                "similarity": round(doc["score"], 3)

            })

        return citations