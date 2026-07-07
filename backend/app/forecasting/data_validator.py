class DataValidator:

    @staticmethod
    def normalize(values, expected_length=3):
        """
        Ensures:
        1. Exactly expected_length values
        2. Chronological order (oldest -> newest)
        """

        if values is None:
            values = []

        values = list(values)

        # Keep only the latest expected_length values
        if len(values) > expected_length:
            values = values[:expected_length]

        # Pad missing values with 0
        while len(values) < expected_length:
            values.append(0)

        # Financial statements are usually newest -> oldest.
        # Reverse them so they become oldest -> newest.
        values.reverse()

        return values