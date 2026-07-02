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

    @staticmethod
    def build_documents(
        chunks: list[str],
        company: str,
        year: int,
        document_type: str,
        source: str
    ):

        documents = []

        from backend.app.processing.metadata_extractor import MetadataExtractor

        for chunk_id, chunk in enumerate(chunks):

            metadata = MetadataExtractor.create_metadata(
                company=company,
                year=year,
                document_type=document_type,
                source=source,
                chunk_id=chunk_id
            )

            documents.append(
                DocumentBuilder.build_document(
                    chunk,
                    metadata
                )
            )

        return documents