from backend.app.graph.graph_builder import GraphBuilder


def main():

    builder = GraphBuilder()

    # Optional: Clear old graph before rebuilding
    builder.db.clear_graph()

    entities = builder.build("Apple")

    print()
    print("=" * 80)
    print("GRAPH BUILD COMPLETE")
    print("=" * 80)

    print()

    print("Companies")
    print(["Apple"])

    print()

    print("Products")
    print(entities.products)

    print()

    print("Risks")
    print(entities.risks)

    print()

    print("Technologies")
    print(entities.technologies)

    print()

    print("Countries")
    print(entities.countries)

    print()

    print("Business Segments")
    print(entities.business_segments)

    print()

    print("People")
    print(entities.people)

    print()

    print("Total Nodes :", builder.db.node_count())

    builder.db.close()


if __name__ == "__main__":
    main()