from backend.app.forecasting.financial_extractor import FinancialExtractor

from backend.app.forecasting.prophet_forecaster import ProphetForecaster
from backend.app.forecasting.xgboost_forecaster import XGBoostForecaster

from backend.app.agents.forecast_agent import ForecastAgent

from backend.app.intelligence.financial_intelligence import (
    FinancialIntelligenceEngine,
)


class AnalysisPipeline:

    def __init__(self):

        self.extractor = FinancialExtractor()

        self.prophet = ProphetForecaster()

        self.xgboost = XGBoostForecaster()

        self.forecast_agent = ForecastAgent()

        self.intelligence = FinancialIntelligenceEngine()

    # =====================================================
    # MAIN PIPELINE
    # =====================================================

    def run(
        self,
        company: str
    ):

        print("\n" + "=" * 80)
        print("RUNNING ANALYSIS PIPELINE")
        print("=" * 80)

        # =====================================================
        # STEP 1
        # Extract Financial Statements
        # =====================================================

        print("\nExtracting financial statements...")

        financial_data = self.extractor.extract(company)

        # =====================================================
        # STEP 2
        # Prophet Forecast
        # =====================================================

        print("\nRunning Prophet Forecast...")

        prophet_forecasts = self._run_prophet(financial_data)

        # =====================================================
        # STEP 3
        # XGBoost Forecast
        # =====================================================

        print("\nRunning XGBoost Forecast...")

        xgboost_forecasts = self._run_xgboost(financial_data)

        # =====================================================
        # STEP 4
        # Forecast Report
        # =====================================================

        print("\nGenerating Forecast Report...")

        forecast_report = self.forecast_agent.analyze(

            company=company,

            forecasts=prophet_forecasts

        )

        # =====================================================
        # STEP 5
        # Multi-Agent Intelligence Report
        # =====================================================

        print("\nGenerating Intelligence Report...")

        intelligence_report = self.intelligence.analyze_company(

            company=company

        )

        print("\n" + "=" * 80)
        print("ANALYSIS PIPELINE COMPLETED")
        print("=" * 80)

        return {

            "financial_data": financial_data,

            "prophet_forecasts": prophet_forecasts,

            "xgboost_forecasts": xgboost_forecasts,

            "forecast_report": forecast_report,

            "intelligence_report": intelligence_report

        }

    # =====================================================
    # PROPHET
    # =====================================================

    def _run_prophet(
        self,
        data
    ):

        metrics = {

            "Revenue": data.revenue,

            "Operating Income": data.operating_income,

            "Net Income": data.net_income

        }

        forecasts = {}

        for metric, values in metrics.items():

            forecasts[metric] = self.prophet.forecast(

                metric_name=metric,

                years=data.years,

                values=values,

                periods=3

            )

        return forecasts

    # =====================================================
    # XGBOOST
    # =====================================================

    def _run_xgboost(
        self,
        data
    ):

        metrics = {

            "Revenue": data.revenue,

            "Operating Income": data.operating_income,

            "Net Income": data.net_income

        }

        forecasts = {}

        for metric, values in metrics.items():

            forecasts[metric] = self.xgboost.forecast(

                metric_name=metric,

                years=data.years,

                values=values,

                periods=3

            )

        return forecasts