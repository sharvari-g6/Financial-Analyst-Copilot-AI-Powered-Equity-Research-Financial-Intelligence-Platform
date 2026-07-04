from backend.app.rag.retriever import Retriever
from backend.app.rag.reranker import Reranker


def main():

    retriever = Retriever()

    docs = retriever.retrieve(

        "Apple business risks",

        top_k=10

    )

    ranked = Reranker.rerank(

        docs,

        top_k=5

    )

    print()

    print("Top Ranked Results\n")

    for doc in ranked:

        print(doc["score"])


if __name__ == "__main__":
    main()