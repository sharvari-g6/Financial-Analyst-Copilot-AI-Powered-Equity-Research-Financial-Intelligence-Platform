from backend.app.intelligence.financial_intelligence import FinancialIntelligenceEngine


def main():

    engine = FinancialIntelligenceEngine()

    report = engine.analyze_company("Apple")

    print("\n" + "=" * 80)
    print("COMPANY")
    print("=" * 80)
    print(report["company"])

    print("\n" + "=" * 80)
    print("REPORTS GENERATED")
    print("=" * 80)

    for name in report["reports"]:
        print(name)

    print("\n" + "=" * 80)
    print("DOCUMENTS RETRIEVED")
    print("=" * 80)

    print(len(report["sources"]))


if __name__ == "__main__":
    main()