from backend.app.processing.pdf_parser import PDFParser
from backend.app.processing.chunker import DocumentChunker
from backend.app.processing.embedding_generator import EmbeddingGenerator


pdf_path = "data/annual_reports/sample_report.pdf"

text = PDFParser.extract_text(pdf_path)

chunker = DocumentChunker()

chunks = chunker.create_chunks(text)

embedder = EmbeddingGenerator()

embedding = embedder.generate_embedding(
    chunks[0]
)

print(f"Embedding Dimension: {len(embedding)}")

print("\nFirst 10 Values:")

print(embedding[:10])

embeddings = embedder.generate_embeddings(
    chunks[:5]
)

print(f"\nGenerated {len(embeddings)} embeddings")