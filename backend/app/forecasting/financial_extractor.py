from backend.app.core.services import query_engine
from backend.app.forecasting.financial_parser import FinancialParser
from backend.app.forecasting.data_validator import DataValidator
from backend.app.models.financial_timeseries import FinancialTimeSeries


class FinancialExtractor:

    def extract(
        self,
        company: str
    ):

        question = (
            f"Extract the historical financial metrics of {company} "
            "for the last three years."
        )

        prompt = """
You are a Financial Data Extraction Expert.

Use ONLY the provided financial statements.

Extract ONLY these metrics.

Return ONLY valid JSON.

Do NOT explain anything.

Return the numbers in the order they appear in the financial statement.

Format:

{
    "revenue":[year1,year2,year3],
    "operating_income":[...],
    "net_income":[...],
    "operating_cash_flow":[...],
    "total_assets":[...],
    "total_liabilities":[...],
    "shareholders_equity":[...]
}
"""

        result = query_engine.ask(

            question=question,

            system_prompt=prompt,

            top_k=10

        )
        print("\n" + "="*80)
        print("RAW LLM OUTPUT")
        print("="*80)
        print(result["answer"])
        print("="*80 + "\n")

        # Parse JSON returned by the LLM
        data = FinancialParser.parse(result["answer"])

        # Normalize all metrics
        revenue = DataValidator.normalize(
            data.get("revenue", [])
        )

        operating_income = DataValidator.normalize(
            data.get("operating_income", [])
        )

        net_income = DataValidator.normalize(
            data.get("net_income", [])
        )

        operating_cash_flow = DataValidator.normalize(
            data.get("operating_cash_flow", [])
        )

        total_assets = DataValidator.normalize(
            data.get("total_assets", [])
        )

        total_liabilities = DataValidator.normalize(
            data.get("total_liabilities", [])
        )

        shareholders_equity = DataValidator.normalize(
            data.get("shareholders_equity", [])
        )

        return FinancialTimeSeries(

            company=company,

            years=[2023, 2024, 2025],

            revenue=revenue,

            operating_income=operating_income,

            net_income=net_income,

            operating_cash_flow=operating_cash_flow,

            free_cash_flow=[0, 0, 0],

            total_assets=total_assets,

            total_liabilities=total_liabilities,

            shareholders_equity=shareholders_equity

        )