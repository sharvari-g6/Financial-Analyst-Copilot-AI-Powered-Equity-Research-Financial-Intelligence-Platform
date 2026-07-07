from backend.app.graph.neo4j_client import Neo4jClient
from backend.app.graph.entity_extractor import EntityExtractor


class GraphBuilder:

    def __init__(self):

        self.db = Neo4jClient()

        self.extractor = EntityExtractor()

    def build(
        self,
        company: str
    ):

        print("\nExtracting entities...\n")

        entities = self.extractor.extract(company)

        print("Creating Company Node...")

        self.db.create_company(company)

        # =====================================================
        # Products
        # =====================================================

        print("Adding Products...")

        for product in entities.products:

            if not product.strip():
                continue

            self.db.create_product(product)

            self.db.link_company_product(
                company,
                product
            )

        # =====================================================
        # Risks
        # =====================================================

        print("Adding Risks...")

        for risk in entities.risks:

            if not risk.strip():
                continue

            self.db.create_risk(risk)

            self.db.link_company_risk(
                company,
                risk
            )

        # =====================================================
        # Technologies
        # =====================================================

        print("Adding Technologies...")

        for technology in entities.technologies:

            if not technology.strip():
                continue

            self.db.create_technology(technology)

            self.db.link_company_technology(
                company,
                technology
            )

        # =====================================================
        # Countries
        # =====================================================

        print("Adding Countries...")

        for country in entities.countries:

            if not country.strip():
                continue

            self.db.create_country(country)

            self.db.link_company_country(
                company,
                country
            )

        # =====================================================
        # Business Segments
        # =====================================================

        print("Adding Business Segments...")

        for segment in entities.business_segments:

            if not segment.strip():
                continue

            self.db.create_business_segment(segment)

            self.db.link_company_segment(
                company,
                segment
            )

        # =====================================================
        # People
        # =====================================================

        print("Adding People...")

        for person in entities.people:

            if not person.strip():
                continue

            self.db.create_person(person)

            self.db.link_company_person(
                company,
                person
            )

        print("\n" + "=" * 60)
        print("KNOWLEDGE GRAPH CREATED")
        print("=" * 60)

        print()

        print("Company :", company)

        print("Products :", len(entities.products))
        print("Risks :", len(entities.risks))
        print("Technologies :", len(entities.technologies))
        print("Countries :", len(entities.countries))
        print("Business Segments :", len(entities.business_segments))
        print("People :", len(entities.people))

        print("\nGraph successfully populated.\n")

        return entities