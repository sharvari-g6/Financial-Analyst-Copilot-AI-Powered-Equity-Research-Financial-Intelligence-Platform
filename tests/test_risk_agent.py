from backend.app.agents.risk_agent import RiskAgent


def main():

    agent = RiskAgent()

    report = agent.analyze_company("Apple")

    print("\n" + "=" * 80)
    print("COMPANY")
    print("=" * 80)

    print(report.company)

    print("\n" + "=" * 80)
    print("RISK REPORT")
    print("=" * 80)

    print(report.summary)

    print("\n" + "=" * 80)
    print("SOURCES")
    print("=" * 80)

    for source in report.sources:
        print(source)


if __name__ == "__main__":
    main()