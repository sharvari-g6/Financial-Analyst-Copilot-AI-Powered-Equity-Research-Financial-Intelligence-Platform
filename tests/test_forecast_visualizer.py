from backend.app.forecasting.financial_extractor import FinancialExtractor
from backend.app.forecasting.prophet_forecaster import ProphetForecaster
from backend.app.forecasting.forecast_visualizer import ForecastVisualizer


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

    visualizer = ForecastVisualizer()

    image = visualizer.plot(result)

    print()

    print("=" * 80)

    print("FORECAST CHART GENERATED")

    print("=" * 80)

    print()

    print(image)


if __name__ == "__main__":
    main()