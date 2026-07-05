from backend.app.core.services import query_engine
from backend.app.prompts.valuation_prompt import ValuationPrompt
from backend.app.models.valuation_report import ValuationReport


class ValuationAgent:

    def __init__(self):

        self.query_engine = query_engine

    def analyze_company(
        self,
        company: str
    ):

        prompt = ValuationPrompt.get_prompt(company)

        question = (
            f"Evaluate the investment attractiveness and valuation "
            f"of {company} based on the available financial documents."
        )

        result = self.query_engine.ask(

            question=question,

            system_prompt=prompt

        )

        report = ValuationReport(

            company=company,

            summary=result["answer"],

            revenue_outlook="",

            profitability_outlook="",

            cash_flow_strength="",

            competitive_position="",

            growth_opportunities="",

            valuation_opinion="",

            investment_thesis="",

            confidence="",

            sources=result["sources"]

        )

        return report