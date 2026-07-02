from backend.app.processing.pdf_parser import PDFParser
from backend.app.processing.chunker import DocumentChunker
from backend.app.processing.document_builder import DocumentBuilder
from backend.app.database.pinecone_db import PineconeDB


def main():

    # Step 1: Extract text from PDF
    parser = PDFParser()

    text = parser.extract_text(
        "data/annual_reports/sample_report.pdf"
    )

    # Step 2: Create chunks
    chunker = DocumentChunker()

    chunks = chunker.create_chunks(text)

    print(f"\nTotal Chunks: {len(chunks)}")

    # Step 3: Build documents with metadata
    documents = DocumentBuilder.build_documents(
        chunks=chunks,
        company="Apple",
        year=2025,
        document_type="Annual Report",
        source="10-K"
    )

    print(f"Documents Created: {len(documents)}")

    # Step 4: Upload to Pinecone
    pinecone = PineconeDB()

    uploaded = pinecone.upsert_vectors(documents)

    print(f"\nVectors Uploaded: {uploaded}")

    # Step 5: Verify Index Stats
    stats = pinecone.get_index_stats()

    print("\nUpdated Index Stats:\n")

    print(stats)


if __name__ == "__main__":
    main()