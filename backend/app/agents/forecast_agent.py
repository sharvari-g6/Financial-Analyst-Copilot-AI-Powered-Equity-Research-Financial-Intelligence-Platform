from backend.app.core.services import llm
from backend.app.prompts.forecast_prompt import ForecastPrompt
from backend.app.models.forecast_report import ForecastReport


class ForecastAgent:

    def analyze(
        self,
        company: str,
        forecasts: dict
    ):

        prompt = ForecastPrompt.get_prompt(company)

        forecast_text = ""

        for metric, forecast in forecasts.items():

            forecast_text += f"\n{metric}\n"

            forecast_text += "Historical:\n"

            for y, v in zip(
                forecast.historical_years,
                forecast.historical_values
            ):

                forecast_text += f"{y}: {v}\n"

            forecast_text += "\nForecast:\n"

            for y, v in zip(
                forecast.forecast_years,
                forecast.forecast_values
            ):

                forecast_text += f"{y}: {round(v,2)}\n"

            forecast_text += "\n"

        final_prompt = f"""
{prompt}

Forecast Data

{forecast_text}
"""

        answer = llm.generate(final_prompt)

        return ForecastReport(

            company=company,

            executive_summary=answer,

            revenue_forecast="",

            profitability_forecast="",

            cash_flow_forecast="",

            balance_sheet_forecast="",

            growth_drivers="",

            key_risks="",

            investment_implication="",

            confidence=""
        )