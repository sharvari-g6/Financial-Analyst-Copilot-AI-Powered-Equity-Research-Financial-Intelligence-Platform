import json
import re


class FinancialParser:

    @staticmethod
    def parse(text: str):

        # ---------------------------------------
        # Remove markdown
        # ---------------------------------------

        text = text.replace("```json", "")
        text = text.replace("```", "")

        # ---------------------------------------
        # Extract JSON
        # ---------------------------------------

        match = re.search(r"\{[\s\S]*\}", text)

        if match is None:
            raise ValueError("No JSON object found.")

        json_text = match.group()

        # ---------------------------------------
        # Remove comments
        # ---------------------------------------

        # Remove // comments
        json_text = re.sub(r"//.*", "", json_text)

        # Remove /* ... */ comments
        json_text = re.sub(
            r"/\*.*?\*/",
            "",
            json_text,
            flags=re.DOTALL
        )

        # ---------------------------------------
        # Remove trailing commas
        # ---------------------------------------

        json_text = re.sub(r",\s*}", "}", json_text)
        json_text = re.sub(r",\s*]", "]", json_text)

        # ---------------------------------------
        # Replace invalid values
        # ---------------------------------------

        json_text = json_text.replace("N/A", "0")
        json_text = json_text.replace("null", "0")
        json_text = json_text.replace("None", "0")

        # Empty arrays like [, ,]
        json_text = re.sub(r"\[\s*,\s*,\s*\]", "[0,0,0]", json_text)

        # Missing values like [123,,456]
        json_text = re.sub(r",\s*,", ",0,", json_text)

        # Missing first value
        json_text = re.sub(r"\[\s*,", "[0,", json_text)

        # Missing last value
        json_text = re.sub(r",\s*\]", ",0]", json_text)

        # ---------------------------------------
        # Parse JSON
        # ---------------------------------------

        try:

            data = json.loads(json_text)

        except json.JSONDecodeError:

            print("\nFailed JSON:\n")
            print(json_text)
            raise

        # ---------------------------------------
        # Ensure required metrics exist
        # ---------------------------------------

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

            cleaned = []

            for value in data[metric][:3]:

                if isinstance(value, (int, float)):
                    cleaned.append(value)
                else:
                    cleaned.append(0)

            while len(cleaned) < 3:
                cleaned.append(0)

            data[metric] = cleaned

        return data