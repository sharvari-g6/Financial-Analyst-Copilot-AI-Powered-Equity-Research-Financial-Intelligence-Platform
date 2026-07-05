from backend.app.core.services import query_engine
from backend.app.prompts.risk_prompt import RiskPrompt
from backend.app.models.risk_report import RiskReport


class RiskAgent:

    def __init__(self):

        self.query_engine = query_engine

    def analyze_company(
        self,
        company: str
    ):

        prompt = RiskPrompt.get_prompt(company)

        question = f"What are the major business and financial risks faced by {company}?"

        result = self.query_engine.ask(

            question=question,

            system_prompt=prompt

        )

        report = RiskReport(

            company=company,

            summary=result["answer"],

            business_risks="",

            financial_risks="",

            operational_risks="",

            regulatory_risks="",

            supply_chain_risks="",

            market_risks="",

            future_outlook="",

            overall_rating="",

            confidence="",

            sources=result["sources"]

        )

        return report