from backend.app.rag.retriever import Retriever
from backend.app.rag.citation_engine import CitationEngine


def main():

    retriever = Retriever()

    docs = retriever.retrieve(

        "What are Apple's business risks?"

    )

    citations = CitationEngine.build_citations(docs)

    print()

    print("Citations\n")

    for citation in citations:

        print(citation)


if __name__ == "__main__":
    main()