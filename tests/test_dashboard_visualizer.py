from backend.app.forecasting.financial_extractor import FinancialExtractor
from backend.app.forecasting.dashboard_visualizer import DashboardVisualizer


def main():

    extractor = FinancialExtractor()

    data = extractor.extract("Apple")

    dashboard = DashboardVisualizer()

    charts = dashboard.generate_dashboard(data)

    print()

    print("=" * 80)
    print("GENERATED CHARTS")
    print("=" * 80)

    print()

    for metric, image in charts.items():

        print(metric)

        print(image)

        print()


if __name__ == "__main__":
    main()