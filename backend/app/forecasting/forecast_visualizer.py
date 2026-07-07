import os

import matplotlib.pyplot as plt

from backend.app.models.forecast_result import ForecastResult


class ForecastVisualizer:

    def plot(
        self,
        forecast: ForecastResult,
        save_folder: str = "forecast_outputs"
    ):

        os.makedirs(save_folder, exist_ok=True)

        plt.figure(figsize=(9, 5))

        # Historical Data
        plt.plot(
            forecast.historical_years,
            forecast.historical_values,
            marker="o",
            linewidth=2,
            label="Historical"
        )

        # Forecast Data
        plt.plot(
            forecast.forecast_years,
            forecast.forecast_values,
            marker="o",
            linestyle="--",
            linewidth=2,
            label="Forecast"
        )

        plt.title(f"{forecast.metric} Forecast")

        plt.xlabel("Year")

        plt.ylabel(forecast.metric)

        plt.grid(True)

        plt.legend()

        output_path = os.path.join(
            save_folder,
            f"{forecast.metric.lower().replace(' ', '_')}_forecast.png"
        )

        plt.savefig(
            output_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        return output_path