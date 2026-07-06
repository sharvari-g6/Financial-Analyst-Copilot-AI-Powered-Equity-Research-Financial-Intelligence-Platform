from backend.app.intelligence.financial_intelligence import (
    FinancialIntelligenceEngine
)


def main():

    print("\nInitializing Financial Intelligence Engine...\n")

    engine = FinancialIntelligenceEngine()

    report = engine.analyze_company("Apple")

    print("\n")
    print("=" * 80)
    print("COMPANY")
    print("=" * 80)

    print(report.company)

    print("\n")
    print("=" * 80)
    print("EXECUTIVE SUMMARY")
    print("=" * 80)

    print(report.executive_summary)

    print("\n")
    print("=" * 80)
    print("FINANCIAL ANALYSIS")
    print("=" * 80)

    print(report.financial_analysis)

    print("\n")
    print("=" * 80)
    print("RISK ANALYSIS")
    print("=" * 80)

    print(report.risk_analysis)

    print("\n")
    print("=" * 80)
    print("VALUATION ANALYSIS")
    print("=" * 80)

    print(report.valuation_analysis)

    print("\n")
    print("=" * 80)
    print("SENTIMENT ANALYSIS")
    print("=" * 80)

    print(report.sentiment_analysis)

    print("\n")
    print("=" * 80)
    print("INVESTMENT THESIS")
    print("=" * 80)

    print(report.investment_thesis)

    print("\n")
    print("=" * 80)
    print("RECOMMENDATION")
    print("=" * 80)

    print(report.recommendation)

    print("\n")
    print("=" * 80)
    print("CONFIDENCE")
    print("=" * 80)

    print(report.confidence)

    print("\n")
    print("=" * 80)
    print("SOURCES")
    print("=" * 80)

    print(f"Total Sources: {len(report.sources)}")

    for source in report.sources:

        print(source)


if __name__ == "__main__":
    main()