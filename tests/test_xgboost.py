from backend.app.forecasting.financial_extractor import FinancialExtractor

from backend.app.forecasting.xgboost_forecaster import XGBoostForecaster


def main():

    extractor = FinancialExtractor()

    data = extractor.extract("Apple")

    forecaster = XGBoostForecaster()

    result = forecaster.forecast(

        metric_name="Revenue",

        years=data.years,

        values=data.revenue,

        periods=3

    )

    print()

    print("=" * 80)

    print("XGBOOST REVENUE FORECAST")

    print("=" * 80)

    print()

    print("Historical Data")

    print()

    for year, value in zip(

        result.historical_years,

        result.historical_values

    ):

        print(year, ":", f"{value:,}")

    print()

    print("Forecast")

    print()

    for year, value in zip(

        result.forecast_years,

        result.forecast_values

    ):

        print(year, ":", f"{value:,.2f}")


if __name__ == "__main__":

    main()