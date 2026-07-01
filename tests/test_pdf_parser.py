from backend.app.processing.pdf_parser import PDFParser


pdf_path = "data/annual_reports/sample_report.pdf"

text = PDFParser.extract_text(pdf_path)

print(text[:2000])

print(f"\nTotal Characters: {len(text):,}")