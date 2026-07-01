class MetadataExtractor:

    @staticmethod
    def create_metadata(
        company: str,
        year: int,
        document_type: str,
        source: str,
        chunk_id: int
    ):

        return {
            "company": company,
            "year": year,
            "document_type": document_type,
            "source": source,
            "chunk_id": chunk_id
        }