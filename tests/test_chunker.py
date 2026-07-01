from backend.app.processing.pdf_parser import PDFParser
from backend.app.processing.chunker import DocumentChunker


pdf_path = "data/annual_reports/sample_report.pdf"

text = PDFParser.extract_text(pdf_path)

chunker = DocumentChunker()

chunks = chunker.create_chunks(text)

print(f"\nTotal Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])

print("\nChunk Length:")
print(len(chunks[0]))

chunk_lengths = [len(chunk) for chunk in chunks]

print(f"\nTotal Chunks: {len(chunks)}")
print(f"Average Length: {sum(chunk_lengths)/len(chunk_lengths):.2f}")
print(f"Min Length: {min(chunk_lengths)}")
print(f"Max Length: {max(chunk_lengths)}")