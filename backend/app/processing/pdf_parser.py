import fitz


class PDFParser:

    @staticmethod
    def extract_text(pdf_path: str) -> str:

        document = fitz.open(pdf_path)

        full_text = ""

        for page in document:

            page_text = page.get_text()

            full_text += page_text + "\n"

        document.close()

        return full_text