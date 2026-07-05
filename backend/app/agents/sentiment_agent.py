from backend.app.core.services import query_engine
from backend.app.prompts.sentiment_prompt import SentimentPrompt
from backend.app.models.sentiment_report import SentimentReport


class SentimentAgent:

    def __init__(self):

        self.query_engine = query_engine

    def analyze_company(
        self,
        company: str,
        context: str = None
    ):

        prompt = SentimentPrompt.get_prompt(company)

        question = f"What is the management sentiment of {company}?"

        # ----------------------------------
        # Shared Context Mode
        # ----------------------------------

        if context is not None:

            result = self.query_engine.ask_from_context(

                question=question,

                context=context,

                system_prompt=prompt

            )

            report = SentimentReport(

                company=company,

                summary=result["answer"],

                management_tone="",

                future_guidance="",

                positive_signals="",

                negative_signals="",

                risk_language="",

                growth_expectations="",

                investor_sentiment="",

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

        report = SentimentReport(

            company=company,

            summary=result["answer"],

            management_tone="",

            future_guidance="",

            positive_signals="",

            negative_signals="",

            risk_language="",

            growth_expectations="",

            investor_sentiment="",

            confidence="",

            sources=result["sources"]

        )

        return report