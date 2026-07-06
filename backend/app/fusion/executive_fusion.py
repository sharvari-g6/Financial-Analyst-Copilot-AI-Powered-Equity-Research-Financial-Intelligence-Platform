from backend.app.core.services import query_engine


class ExecutiveFusion:

    def generate(
        self,
        company: str,
        financial_report: str,
        risk_report: str,
        valuation_report: str,
        sentiment_report: str
    ):

        prompt = f"""
You are a Senior Equity Research Analyst.

You have received four independent reports about {company}.

==========================
FINANCIAL ANALYSIS
==========================

{financial_report}

==========================
RISK ANALYSIS
==========================

{risk_report}

==========================
VALUATION ANALYSIS
==========================

{valuation_report}

==========================
SENTIMENT ANALYSIS
==========================

{sentiment_report}

---------------------------------------------------

Create ONE final professional Equity Research Report.

Return ONLY the following sections.

Executive Summary

(2-3 paragraphs summarizing the company.)

-------------------------------------

Investment Thesis

(Why should an investor consider this company?)

-------------------------------------

Recommendation

Choose ONLY ONE:

BUY

HOLD

SELL

Explain your reasoning.

-------------------------------------

Confidence

Give a confidence score between 0 and 100%.

Mention why.
"""

        return query_engine.llm.generate(prompt)