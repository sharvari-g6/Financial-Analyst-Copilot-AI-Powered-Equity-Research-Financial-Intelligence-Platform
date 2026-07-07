from backend.app.graph.graph_query import GraphQuery


def print_result(title, rows, key):

    print()
    print("=" * 80)
    print(title)
    print("=" * 80)

    if not rows:
        print("No results.")
        return

    for row in rows:
        print("-", row[key])


def main():

    graph = GraphQuery()

    company = "Apple"

    print_result(
        "PRODUCTS",
        graph.get_products(company),
        "product"
    )

    print_result(
        "RISKS",
        graph.get_risks(company),
        "risk"
    )

    print_result(
        "TECHNOLOGIES",
        graph.get_technologies(company),
        "technology"
    )

    print_result(
        "BUSINESS SEGMENTS",
        graph.get_segments(company),
        "segment"
    )

    print_result(
        "COUNTRIES",
        graph.get_countries(company),
        "country"
    )


if __name__ == "__main__":
    main()