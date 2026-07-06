from backend.app.models.intelligence_report import IntelligenceReport
from backend.app.fusion.executive_fusion import ExecutiveFusion


class ReportFusion:

    def __init__(self):

        self.executive = ExecutiveFusion()

    def fuse(
        self,
        company: str,
        reports: dict,
        sources: list
    ):

        final_summary = self.executive.generate(

            company=company,

            financial_report=reports["financial"].summary,

            risk_report=reports["risk"].summary,

            valuation_report=reports["valuation"].summary,

            sentiment_report=reports["sentiment"].summary

        )

        return IntelligenceReport(

            company=company,

            executive_summary=final_summary,

            financial_analysis=reports["financial"].summary,

            risk_analysis=reports["risk"].summary,

            valuation_analysis=reports["valuation"].summary,

            sentiment_analysis=reports["sentiment"].summary,

            investment_thesis="",

            recommendation="",

            confidence="",

            sources=sources

        )