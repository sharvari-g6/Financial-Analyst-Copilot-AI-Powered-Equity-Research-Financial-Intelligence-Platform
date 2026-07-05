from backend.app.agents.financial_agent import FinancialAgent
from backend.app.agents.risk_agent import RiskAgent
from backend.app.agents.valuation_agent import ValuationAgent
from backend.app.agents.sentiment_agent import SentimentAgent


class AgentRouter:

    def __init__(self):

        self.financial = FinancialAgent()
        self.risk = RiskAgent()
        self.valuation = ValuationAgent()
        self.sentiment = SentimentAgent()

    # --------------------------------------------------
    # Existing Query Router
    # --------------------------------------------------

    def route(
        self,
        company: str,
        query: str
    ):

        query = query.lower()

        reports = {}

        # ------------------------
        # Financial
        # ------------------------

        if any(word in query for word in [
            "financial",
            "revenue",
            "profit",
            "income",
            "cash",
            "balance",
            "statement"
        ]):

            reports["financial"] = (
                self.financial.analyze_company(company)
            )

        # ------------------------
        # Risk
        # ------------------------

        if any(word in query for word in [
            "risk",
            "threat",
            "danger",
            "issue"
        ]):

            reports["risk"] = (
                self.risk.analyze_company(company)
            )

        # ------------------------
        # Valuation
        # ------------------------

        if any(word in query for word in [
            "valuation",
            "invest",
            "buy",
            "sell",
            "hold",
            "stock"
        ]):

            reports["valuation"] = (
                self.valuation.analyze_company(company)
            )

        # ------------------------
        # Sentiment
        # ------------------------

        if any(word in query for word in [
            "sentiment",
            "management",
            "tone",
            "future",
            "guidance"
        ]):

            reports["sentiment"] = (
                self.sentiment.analyze_company(company)
            )

        # ------------------------
        # Complete Analysis
        # ------------------------

        if (
            "analyze" in query
            or "analysis" in query
            or "complete" in query
        ):

            reports = self.run_all(company)

        return reports

    # --------------------------------------------------
    # NEW: Shared Context Mode (Phase 6.1)
    # --------------------------------------------------

    def run_all(
        self,
        company: str,
        context: str = None
    ):

        return {

            "financial": self.financial.analyze_company(
                company,
                context=context
            ),

            "risk": self.risk.analyze_company(
                company,
                context=context
            ),

            "valuation": self.valuation.analyze_company(
                company,
                context=context
            ),

            "sentiment": self.sentiment.analyze_company(
                company,
                context=context
            )

        }