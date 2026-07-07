from backend.app.forecasting.financial_extractor import FinancialExtractor
from backend.app.forecasting.prophet_forecaster import ProphetForecaster
from backend.app.agents.forecast_agent import ForecastAgent


def main():

    extractor = FinancialExtractor()

    data = extractor.extract("Apple")

    forecaster = ProphetForecaster()

    forecasts = {}

    metrics = {

        "Revenue": data.revenue,

        "Operating Income": data.operating_income,

        "Net Income": data.net_income

    }

    for metric, values in metrics.items():

        forecasts[metric] = forecaster.forecast(

            metric_name=metric,

            years=data.years,

            values=values,

            periods=3

        )

    agent = ForecastAgent()

    report = agent.analyze(

        company="Apple",

        forecasts=forecasts

    )

    print()

    print("=" * 80)
    print("FORECAST REPORT")
    print("=" * 80)

    print()

    print(report.executive_summary)


if __name__ == "__main__":
    main()