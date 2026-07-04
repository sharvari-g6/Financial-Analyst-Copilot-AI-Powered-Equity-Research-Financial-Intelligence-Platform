from backend.app.rag.query_engine import QueryEngine
from backend.app.prompts.financial_prompt import FinancialPrompt
from backend.app.models.financial_report import FinancialReport


class FinancialAgent:

    def __init__(self):

        self.query_engine = QueryEngine()

    def analyze_company(
        self,
        company: str
    ):

        prompt = FinancialPrompt.get_prompt(company)

        question = f"Analyze the financial performance of {company}."

        result = self.query_engine.ask(

            question=question,

            system_prompt=prompt

        )

        report = FinancialReport(

            company=company,

            summary=result["answer"],

            revenue="",

            profitability="",

            cash_flow="",

            balance_sheet="",

            strengths="",

            weaknesses="",

            overall_health="",

            confidence="",

            sources=result["sources"]

        )

        return report