from dataclasses import dataclass


@dataclass
class ForecastResult:

    metric: str

    historical_years: list

    historical_values: list

    forecast_years: list

    forecast_values: list