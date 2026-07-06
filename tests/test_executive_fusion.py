from backend.app.fusion.executive_fusion import ExecutiveFusion


def main():

    fusion = ExecutiveFusion()

    financial_report = """
Apple demonstrated strong revenue growth with increasing operating income,
healthy cash flow and stable gross margins.
"""

    risk_report = """
Major risks include supply chain dependence, regulatory scrutiny,
cybersecurity threats and macroeconomic uncertainty.
"""

    valuation_report = """
Apple appears fundamentally strong with robust cash generation and
consistent profitability. Long-term outlook remains positive.
"""

    sentiment_report = """
Management maintains a positive outlook while acknowledging regulatory
and economic challenges. Product innovation remains a key growth driver.
"""

    print("\n" + "=" * 80)
    print("EXECUTIVE FUSION")
    print("=" * 80)

    result = fusion.generate(

        company="Apple",

        financial_report=financial_report,

        risk_report=risk_report,

        valuation_report=valuation_report,

        sentiment_report=sentiment_report

    )

    print(result)


if __name__ == "__main__":
    main()