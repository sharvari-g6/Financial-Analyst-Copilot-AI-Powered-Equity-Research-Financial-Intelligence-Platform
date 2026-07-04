class Reranker:

    @staticmethod
    def rerank(

        documents,

        top_k=5

    ):

        ranked = sorted(

            documents,

            key=lambda x: x["score"],

            reverse=True

        )

        return ranked[:top_k]