from dataclasses import dataclass


@dataclass
class SentimentReport:

    company: str

    summary: str

    management_tone: str

    future_guidance: str

    positive_signals: str

    negative_signals: str

    risk_language: str

    growth_expectations: str

    investor_sentiment: str

    confidence: str

    sources: list