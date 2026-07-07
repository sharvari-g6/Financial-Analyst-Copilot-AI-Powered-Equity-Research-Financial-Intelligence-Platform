import pandas as pd

from prophet import Prophet

from backend.app.models.forecast_result import ForecastResult


class ProphetForecaster:

    def forecast(
        self,
        metric_name: str,
        years: list,
        values: list,
        periods: int = 3
    ):

        # Build dataframe for Prophet
        df = pd.DataFrame({

            "ds": pd.to_datetime(
                [f"{year}-12-31" for year in years]
            ),

            "y": values

        })

        # Train Prophet
        model = Prophet(

            yearly_seasonality=False,

            weekly_seasonality=False,

            daily_seasonality=False

        )

        model.fit(df)

        # Predict future years
        future = model.make_future_dataframe(

            periods=periods,

            freq="YS"

        )

        forecast = model.predict(future)

        future_values = forecast["yhat"].tail(periods).tolist()

        future_years = [

            years[-1] + i

            for i in range(1, periods + 1)

        ]

        return ForecastResult(

            metric=metric_name,

            historical_years=years,

            historical_values=values,

            forecast_years=future_years,

            forecast_values=[round(v, 2) for v in future_values]

        )