from backend.app.agents.valuation_agent import ValuationAgent


def main():

    agent = ValuationAgent()

    report = agent.analyze_company("Apple")

    print("\n" + "=" * 80)
    print("COMPANY")
    print("=" * 80)

    print(report.company)

    print("\n" + "=" * 80)
    print("VALUATION REPORT")
    print("=" * 80)

    print(report.summary)

    print("\n" + "=" * 80)
    print("SOURCES")
    print("=" * 80)

    for source in report.sources:

        print(source)


if __name__ == "__main__":
    main()