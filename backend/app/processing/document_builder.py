class DocumentBuilder:

    @staticmethod
    def build_document(
        text: str,
        metadata: dict
    ):

        return {
            "text": text,
            "metadata": metadata
        }