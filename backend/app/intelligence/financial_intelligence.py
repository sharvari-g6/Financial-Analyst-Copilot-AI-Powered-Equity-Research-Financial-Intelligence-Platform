from backend.app.rag.retriever import Retriever
from backend.app.router.agent_router import AgentRouter
from backend.app.fusion.report_fusion import ReportFusion


class FinancialIntelligenceEngine:

    def __init__(self):

        self.retriever = Retriever()
        self.router = AgentRouter()
        self.fusion = ReportFusion()

    def analyze_company(
        self,
        company: str,
        top_k: int = 15
    ):

        print("\nRetrieving documents only once...\n")

        documents = self.retriever.retrieve(
            query=f"Complete financial analysis of {company}",
            top_k=top_k
        )

        context = "\n\n".join(
            doc["text"]
            for doc in documents
        )

        reports = self.router.run_all(
            company=company,
            context=context
        )

        final_report = self.fusion.fuse(

            company=company,

            reports=reports,

            sources=documents

        )

        return final_report