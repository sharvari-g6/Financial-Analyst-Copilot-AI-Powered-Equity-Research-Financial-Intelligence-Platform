import json

from backend.app.core.services import query_engine

from backend.app.models.graph_entities import GraphEntities


class EntityExtractor:

    def extract(
        self,
        company: str
    ):

        question = (
            f"Extract all important entities from the annual report of {company}."
        )

        prompt = """
You are an expert Financial Knowledge Graph Builder.

Read the retrieved annual report carefully.

Extract ALL entities that appear in the report.

Include entities even if they appear only once.

Return ONLY valid JSON.

Do not explain anything.

Rules:

- companies:
    Public companies, subsidiaries, partners.

- people:
    CEO, CFO, directors, executives.

- products:
    iPhone, Mac, iPad, Apple Watch, Vision Pro,
    software, services, devices.

- countries:
    Every country or region mentioned.

- risks:
    Every business risk, financial risk,
    cybersecurity risk, regulatory risk,
    supply chain risk.

- technologies:
    AI, Machine Learning,
    Apple Intelligence,
    Cloud,
    Semiconductors,
    etc.

- competitors:
    Companies competing with Apple.

- business_segments:
    Products,
    Services,
    Wearables,
    Hardware,
    Software,
    etc.

Return ONLY JSON.

{
    "companies":[],
    "people":[],
    "products":[],
    "countries":[],
    "risks":[],
    "technologies":[],
    "competitors":[],
    "business_segments":[]
}
"""

        result = query_engine.ask(

            question=question,

            system_prompt=prompt,

            top_k=10

        )

        text = result["answer"]

        start = text.find("{")

        end = text.rfind("}")

        json_text = text[start:end+1]

        data = json.loads(json_text)

        return GraphEntities(

            companies=data.get("companies", []),

            people=data.get("people", []),

            products=data.get("products", []),

            countries=data.get("countries", []),

            risks=data.get("risks", []),

            technologies=data.get("technologies", []),

            competitors=data.get("competitors", []),

            business_segments=data.get("business_segments", [])

        )