from backend.app.graph.graph_query import GraphQuery


class GraphRetriever:

    def __init__(self):

        self.graph = GraphQuery()

    def retrieve(
        self,
        company: str
    ):

        return {

            "company": company,

            "products": [
                row["product"]
                for row in self.graph.get_products(company)
            ],

            "risks": [
                row["risk"]
                for row in self.graph.get_risks(company)
            ],

            "technologies": [
                row["technology"]
                for row in self.graph.get_technologies(company)
            ],

            "segments": [
                row["segment"]
                for row in self.graph.get_segments(company)
            ],

            "countries": [
                row["country"]
                for row in self.graph.get_countries(company)
            ],

            "competitors": [
                row["competitor"]
                for row in self.graph.get_competitors(company)
            ]

        }