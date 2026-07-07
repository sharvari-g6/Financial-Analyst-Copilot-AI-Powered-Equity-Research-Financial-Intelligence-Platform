import json
import re


class FinancialParser:

    @staticmethod
    def parse(text: str):

        # Remove markdown fences
        text = text.replace("```json", "")
        text = text.replace("```", "")

        # Extract JSON block
        match = re.search(r"\{[\s\S]*\}", text)

        if match is None:
            raise ValueError("No JSON object found.")

        json_text = match.group()

        # Remove trailing commas
        json_text = re.sub(r",\s*}", "}", json_text)
        json_text = re.sub(r",\s*]", "]", json_text)

        # Replace invalid values
        json_text = json_text.replace("N/A", "0")
        json_text = json_text.replace("null", "0")
        json_text = json_text.replace("None", "0")

        try:
            data = json.loads(json_text)

        except json.JSONDecodeError:

            print("\nFailed JSON:\n")
            print(json_text)
            raise

        metrics = [
            "revenue",
            "operating_income",
            "net_income",
            "operating_cash_flow",
            "total_assets",
            "total_liabilities",
            "shareholders_equity"
        ]

        for metric in metrics:

            if metric not in data:
                data[metric] = [0, 0, 0]

            while len(data[metric]) < 3:
                data[metric].append(0)

        return data