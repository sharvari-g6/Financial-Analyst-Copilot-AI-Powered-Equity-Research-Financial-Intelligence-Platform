from backend.app.graph.neo4j_client import Neo4jClient


def main():

    client = Neo4jClient()

    # Clear old graph
    client.clear_graph()

    # Create companies
    client.create_company("Apple")

    client.create_company("Microsoft")

    client.create_company("Google")

    print()

    print("=" * 80)
    print("COMPANIES")
    print("=" * 80)
    print()

    companies = client.get_companies()

    for company in companies:
        print(company)

    print()

    print("=" * 80)
    print("NODE COUNT")
    print("=" * 80)
    print()

    print(client.node_count())

    client.close()


if __name__ == "__main__":
    main()