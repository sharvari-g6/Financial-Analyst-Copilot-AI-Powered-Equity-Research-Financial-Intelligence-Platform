from backend.app.forecasting.financial_extractor import FinancialExtractor
from backend.app.forecasting.prophet_forecaster import ProphetForecaster


def main():

    extractor = FinancialExtractor()

    data = extractor.extract("Apple")

    forecaster = ProphetForecaster()

    result = forecaster.forecast(
        metric_name="Revenue",
        years=data.years,
        values=data.revenue,
        periods=3
    )

    print()
    print("=" * 80)
    print("REVENUE FORECAST")
    print("=" * 80)

    print("\nHistorical Data\n")

    for year, value in zip(
        result.historical_years,
        result.historical_values
    ):
        print(f"{year} : {value:,}")

    print("\nForecast\n")

    for year, value in zip(
        result.forecast_years,
        result.forecast_values
    ):
        print(f"{year} : {value:,.2f}")

    print("\n")
    print("=" * 80)


if __name__ == "__main__":
    main()