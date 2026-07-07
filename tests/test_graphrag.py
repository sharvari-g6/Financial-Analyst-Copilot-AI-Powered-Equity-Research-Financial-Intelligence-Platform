from backend.app.graphrag.graphrag_engine import GraphRAGEngine


def main():

    engine = GraphRAGEngine()

    company = "Apple"

    question = (
        "What are Apple's major products, "
        "business segments, technologies and risks?"
    )

    result = engine.ask(

        company=company,

        question=question

    )

    print()

    print("=" * 80)
    print("GRAPH RAG RESULT")
    print("=" * 80)

    print()

    print(result["answer"])


if __name__ == "__main__":
    main()