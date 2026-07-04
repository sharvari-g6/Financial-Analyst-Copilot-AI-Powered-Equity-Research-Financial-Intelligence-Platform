from backend.app.rag.retriever import Retriever


def main():

    retriever = Retriever()

    docs = retriever.retrieve(

        query="What are Apple's major business risks?",

        top_k=3

    )

    print()

    print(f"Retrieved {len(docs)} documents\n")

    for i, doc in enumerate(docs, start=1):

        print("=" * 70)

        print(f"Result {i}")

        print(f"Similarity Score : {doc['score']:.3f}")

        print(f"Chunk ID         : {doc['chunk_id']}")

        print()

        print(doc["text"][:500])

        print()


if __name__ == "__main__":
    main()