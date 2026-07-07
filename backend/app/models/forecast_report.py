from dataclasses import dataclass


@dataclass
class ForecastReport:

    company: str

    executive_summary: str

    revenue_forecast: str

    profitability_forecast: str

    cash_flow_forecast: str

    balance_sheet_forecast: str

    growth_drivers: str

    key_risks: str

    investment_implication: str

    confidence: str