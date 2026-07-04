from dataclasses import dataclass


@dataclass
class RiskReport:

    company: str

    summary: str

    business_risks: str

    financial_risks: str

    operational_risks: str

    regulatory_risks: str

    supply_chain_risks: str

    market_risks: str

    future_outlook: str

    overall_rating: str

    confidence: str

    sources: list