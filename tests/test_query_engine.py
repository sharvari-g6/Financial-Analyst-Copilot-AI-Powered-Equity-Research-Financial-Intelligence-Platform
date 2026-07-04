from backend.app.rag.query_engine import QueryEngine


def main():

    engine = QueryEngine()

    response = engine.ask(
        "What are Apple's biggest business risks?"
    )

    print("\n" + "=" * 80)
    print("QUESTION")
    print("=" * 80)
    print(response["question"])

    print("\n" + "=" * 80)
    print("AI ANSWER")
    print("=" * 80)
    print(response["answer"])

    print("\n" + "=" * 80)
    print("SOURCES")
    print("=" * 80)

    for source in response["sources"]:
        print(source)


if __name__ == "__main__":
    main()