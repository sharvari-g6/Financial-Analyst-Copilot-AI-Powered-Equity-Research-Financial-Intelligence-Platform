from backend.app.processing.pdf_parser import PDFParser
from backend.app.processing.chunker import DocumentChunker
from backend.app.processing.metadata_extractor import MetadataExtractor
from backend.app.processing.document_builder import DocumentBuilder


pdf_path = "data/annual_reports/sample_report.pdf"

text = PDFParser.extract_text(pdf_path)

chunker = DocumentChunker()

chunks = chunker.create_chunks(text)

documents = []

for idx, chunk in enumerate(chunks):

    metadata = MetadataExtractor.create_metadata(
        company="Apple",
        year=2025,
        document_type="Annual Report",
        source="10-K",
        chunk_id=idx
    )

    document = DocumentBuilder.build_document(
        text=chunk,
        metadata=metadata
    )

    documents.append(document)

print(f"Total Documents: {len(documents)}")

print("\nSample Document:\n")

print(documents[0])