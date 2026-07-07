from xgboost import XGBRegressor

import numpy as np

from backend.app.models.forecast_result import ForecastResult


class XGBoostForecaster:

    def forecast(
        self,
        metric_name: str,
        years: list,
        values: list,
        periods: int = 3
    ):

        # --------------------------
        # Remove missing values
        # --------------------------

        clean = [

            (y, v)

            for y, v in zip(years, values)

            if isinstance(v, (int, float))

        ]

        years = [x[0] for x in clean]

        values = [x[1] for x in clean]

        # --------------------------
        # Training data
        # --------------------------

        X = np.array(years).reshape(-1, 1)

        y = np.array(values)

        model = XGBRegressor(

            n_estimators=200,

            learning_rate=0.1,

            max_depth=3,

            random_state=42

        )

        model.fit(X, y)

        # --------------------------
        # Future years
        # --------------------------

        future_years = [

            years[-1] + i

            for i in range(1, periods + 1)

        ]

        future_X = np.array(future_years).reshape(-1, 1)

        predictions = model.predict(future_X)

        return ForecastResult(

            metric=metric_name,

            historical_years=years,

            historical_values=values,

            forecast_years=future_years,

            forecast_values=[

                round(x, 2)

                for x in predictions

            ]

        )