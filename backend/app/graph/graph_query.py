from backend.app.graph.neo4j_client import Neo4jClient


class GraphQuery:

    def __init__(self):

        self.db = Neo4jClient()

    # -----------------------------
    # Company
    # -----------------------------
    def get_company(self, company):

        query = """
        MATCH (c:Company {name:$company})
        RETURN c.name AS company
        """

        return self.db.run(query, company=company)

    # -----------------------------
    # Products
    # -----------------------------
    def get_products(self, company):

        query = """
        MATCH (c:Company {name:$company})-[:PRODUCES]->(p:Product)
        RETURN p.name AS product
        ORDER BY product
        """

        return self.db.run(query, company=company)

    # -----------------------------
    # Risks
    # -----------------------------
    def get_risks(self, company):

        query = """
        MATCH (c:Company {name:$company})-[:FACES_RISK]->(r:Risk)
        RETURN r.name AS risk
        ORDER BY risk
        """

        return self.db.run(query, company=company)

    # -----------------------------
    # Technologies
    # -----------------------------
    def get_technologies(self, company):

        query = """
        MATCH (c:Company {name:$company})-[:USES_TECHNOLOGY]->(t:Technology)
        RETURN t.name AS technology
        ORDER BY technology
        """

        return self.db.run(query, company=company)

    # -----------------------------
    # Segments
    # -----------------------------
    def get_segments(self, company):

        query = """
        MATCH (c:Company {name:$company})-[:HAS_SEGMENT]->(s:BusinessSegment)
        RETURN s.name AS segment
        ORDER BY segment
        """

        return self.db.run(query, company=company)

    # -----------------------------
    # Countries
    # -----------------------------
    def get_countries(self, company):

        query = """
        MATCH (c:Company {name:$company})-[:OPERATES_IN]->(co:Country)
        RETURN co.name AS country
        ORDER BY country
        """

        return self.db.run(query, company=company)

    # -----------------------------
    # Competitors
    # -----------------------------
    def get_competitors(self, company):

        query = """
        MATCH (c:Company {name:$company})-[:COMPETES_WITH]->(co:Company)
        RETURN co.name AS competitor
        ORDER BY competitor
        """

        return self.db.run(query, company=company)