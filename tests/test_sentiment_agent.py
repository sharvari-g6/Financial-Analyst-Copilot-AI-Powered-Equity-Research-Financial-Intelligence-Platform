from backend.app.agents.sentiment_agent import SentimentAgent


def main():

    agent = SentimentAgent()

    report = agent.analyze_company("Apple")

    print("\n" + "=" * 80)
    print("COMPANY")
    print("=" * 80)

    print(report.company)

    print("\n" + "=" * 80)
    print("SENTIMENT REPORT")
    print("=" * 80)

    print(report.summary)

    print("\n" + "=" * 80)
    print("SOURCES")
    print("=" * 80)

    for source in report.sources:
        print(source)


if __name__ == "__main__":
    main()