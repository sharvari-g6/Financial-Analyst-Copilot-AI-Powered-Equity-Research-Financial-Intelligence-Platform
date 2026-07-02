from backend.app.database.pinecone_db import PineconeDB


def main():

    db = PineconeDB()

    query = "Why did Apple's revenue increase?"

    print(f"\nQuery: {query}\n")

    results = db.search_vectors(
        query=query,
        top_k=5
    )

    print("Raw Response:")
    print(results)
    print()

    if not results.matches:
        print("No matches found!")
        return

    print(f"Total Matches: {len(results.matches)}\n")

    for i, match in enumerate(results.matches, start=1):

        print("=" * 80)

        print(f"Match {i}")
        print(f"Score : {match.score:.4f}")

        print("\nMetadata:")

        for key, value in match.metadata.items():

            if key != "text":
                print(f"{key}: {value}")

        print("\nRetrieved Text:\n")

        print(match.metadata["text"][:700])

        print("\n")


if __name__ == "__main__":
    main()