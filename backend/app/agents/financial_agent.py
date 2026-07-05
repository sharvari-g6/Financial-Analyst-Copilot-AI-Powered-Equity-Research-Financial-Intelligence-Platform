from backend.app.core.services import query_engine
from backend.app.prompts.financial_prompt import FinancialPrompt
from backend.app.models.financial_report import FinancialReport


class FinancialAgent:

    def __init__(self):

        self.query_engine = query_engine

    def analyze_company(
        self,
        company: str,
        context: str = None
    ):

        prompt = FinancialPrompt.get_prompt(company)

        question = f"Analyze the financial performance of {company}."

        # ----------------------------------
        # Shared Context Mode
        # ----------------------------------

        if context is not None:

            result = self.query_engine.ask_from_context(

                question=question,

                context=context,

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

                sources=[]

            )

            return report

        # ----------------------------------
        # Normal RAG Mode
        # ----------------------------------

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