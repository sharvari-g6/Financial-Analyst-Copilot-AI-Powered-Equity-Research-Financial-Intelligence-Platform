from neo4j import GraphDatabase

from backend.app.core.config import settings


class Neo4jClient:

    def __init__(self):

        print("Connecting to Neo4j...")

        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(
                settings.NEO4J_USERNAME,
                settings.NEO4J_PASSWORD
            )
        )

        self.database = settings.NEO4J_DATABASE

    # ==========================================================
    # Generic Query Runner
    # ==========================================================

    def run(self, query: str, **params):

        with self.driver.session(
            database=self.database
        ) as session:

            result = session.run(
                query,
                **params
            )

            return [record.data() for record in result]

    # ==========================================================
    # Close
    # ==========================================================

    def close(self):

        self.driver.close()

    # ==========================================================
    # Company
    # ==========================================================

    def create_company(self, company: str):

        query = """
        MERGE (c:Company {name:$company})
        """

        self.run(
            query,
            company=company
        )

    # ==========================================================
    # Product
    # ==========================================================

    def create_product(self, product: str):

        query = """
        MERGE (p:Product {name:$product})
        """

        self.run(
            query,
            product=product
        )

    # ==========================================================
    # Risk
    # ==========================================================

    def create_risk(self, risk: str):

        query = """
        MERGE (r:Risk {name:$risk})
        """

        self.run(
            query,
            risk=risk
        )

    # ==========================================================
    # Technology
    # ==========================================================

    def create_technology(self, technology: str):

        query = """
        MERGE (t:Technology {name:$technology})
        """

        self.run(
            query,
            technology=technology
        )

    # ==========================================================
    # Country
    # ==========================================================

    def create_country(self, country: str):

        query = """
        MERGE (c:Country {name:$country})
        """

        self.run(
            query,
            country=country
        )

    # ==========================================================
    # Business Segment
    # ==========================================================

    def create_business_segment(self, segment: str):

        query = """
        MERGE (s:BusinessSegment {name:$segment})
        """

        self.run(
            query,
            segment=segment
        )

    # ==========================================================
    # Person
    # ==========================================================

    def create_person(self, person: str):

        query = """
        MERGE (p:Person {name:$person})
        """

        self.run(
            query,
            person=person
        )

    # ==========================================================
    # Relationships
    # ==========================================================

    def link_company_product(
        self,
        company,
        product
    ):

        query = """
        MATCH (c:Company {name:$company})
        MATCH (p:Product {name:$product})
        MERGE (c)-[:PRODUCES]->(p)
        """

        self.run(
            query,
            company=company,
            product=product
        )

    def link_company_risk(
        self,
        company,
        risk
    ):

        query = """
        MATCH (c:Company {name:$company})
        MATCH (r:Risk {name:$risk})
        MERGE (c)-[:FACES_RISK]->(r)
        """

        self.run(
            query,
            company=company,
            risk=risk
        )

    def link_company_technology(
        self,
        company,
        technology
    ):

        query = """
        MATCH (c:Company {name:$company})
        MATCH (t:Technology {name:$technology})
        MERGE (c)-[:USES_TECHNOLOGY]->(t)
        """

        self.run(
            query,
            company=company,
            technology=technology
        )

    def link_company_country(
        self,
        company,
        country
    ):

        query = """
        MATCH (c:Company {name:$company})
        MATCH (co:Country {name:$country})
        MERGE (c)-[:OPERATES_IN]->(co)
        """

        self.run(
            query,
            company=company,
            country=country
        )

    def link_company_segment(
        self,
        company,
        segment
    ):

        query = """
        MATCH (c:Company {name:$company})
        MATCH (s:BusinessSegment {name:$segment})
        MERGE (c)-[:HAS_SEGMENT]->(s)
        """

        self.run(
            query,
            company=company,
            segment=segment
        )

    def link_company_person(
        self,
        company,
        person
    ):

        query = """
        MATCH (c:Company {name:$company})
        MATCH (p:Person {name:$person})
        MERGE (c)-[:HAS_CEO]->(p)
        """

        self.run(
            query,
            company=company,
            person=person
        )

    # ==========================================================
    # Utility Functions
    # ==========================================================

    def get_companies(self):

        query = """
        MATCH (c:Company)
        RETURN c.name AS company
        ORDER BY company
        """

        result = self.run(query)

        return [
            record["company"]
            for record in result
        ]

    def clear_graph(self):

        query = """
        MATCH (n)
        DETACH DELETE n
        """

        self.run(query)

    def node_count(self):

        query = """
        MATCH (n)
        RETURN COUNT(n) AS total
        """

        result = self.run(query)

        return result[0]["total"]