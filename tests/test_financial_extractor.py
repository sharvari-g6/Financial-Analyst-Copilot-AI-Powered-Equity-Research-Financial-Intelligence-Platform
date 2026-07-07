from backend.app.forecasting.financial_extractor import FinancialExtractor


def main():

    extractor = FinancialExtractor()

    data = extractor.extract("Apple")

    print()

    print("="*80)

    print("FINANCIAL TIME SERIES")

    print("="*80)

    print()

    print(data)


if __name__=="__main__":

    main()