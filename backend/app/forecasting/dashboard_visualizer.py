
from backend.app.forecasting.prophet_forecaster import ProphetForecaster
from backend.app.forecasting.forecast_visualizer import ForecastVisualizer


class DashboardVisualizer:

    def __init__(self):

        self.forecaster = ProphetForecaster()
        self.visualizer = ForecastVisualizer()

    def generate_dashboard(self, data):

        charts = {}

        metrics = {

            "Revenue": data.revenue,

            "Operating Income": data.operating_income,

            "Net Income": data.net_income,

            "Operating Cash Flow": data.operating_cash_flow,

            "Total Assets": data.total_assets,

            "Total Liabilities": data.total_liabilities,

            "Shareholders Equity": data.shareholders_equity

        }

        for metric_name, values in metrics.items():

            # Skip metrics with missing values
            if (
                len(values) < 3
                or any(v is None for v in values)
            ):
                continue

            forecast = self.forecaster.forecast(

                metric_name=metric_name,

                years=data.years,

                values=values,

                periods=3

            )

            image = self.visualizer.plot(forecast)

            charts[metric_name] = image

        return charts