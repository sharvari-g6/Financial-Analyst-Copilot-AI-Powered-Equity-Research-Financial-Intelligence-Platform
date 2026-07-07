from backend.app.graph.entity_extractor import EntityExtractor


def main():

    extractor = EntityExtractor()

    entities = extractor.extract("Apple")

    print()

    print("=" * 80)
    print("GRAPH ENTITIES")
    print("=" * 80)

    print()

    print("Companies")

    print(entities.companies)

    print()

    print("People")

    print(entities.people)

    print()

    print("Products")

    print(entities.products)

    print()

    print("Countries")

    print(entities.countries)

    print()

    print("Risks")

    print(entities.risks)

    print()

    print("Technologies")

    print(entities.technologies)

    print()

    print("Competitors")

    print(entities.competitors)

    print()

    print("Business Segments")

    print(entities.business_segments)


if __name__ == "__main__":
    main()