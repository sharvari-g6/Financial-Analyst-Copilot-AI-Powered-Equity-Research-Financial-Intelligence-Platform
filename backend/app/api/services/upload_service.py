import os
import shutil

from backend.app.processing.pdf_parser import PDFParser
from backend.app.processing.chunker import DocumentChunker
from backend.app.processing.document_builder import DocumentBuilder
from backend.app.database.pinecone_db import PineconeDB
from backend.app.graph.graph_builder import GraphBuilder


class UploadService:

    def __init__(self):

        self.chunker = DocumentChunker()

        self.vector_db = PineconeDB()

        self.graph_builder = GraphBuilder()

    def process_upload(
        self,
        file,
        company: str,
        year: int
    ):

        # ---------------------------------------
        # Save uploaded PDF
        # ---------------------------------------

        upload_dir = "uploaded_reports"

        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(
            upload_dir,
            file.filename
        )

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        # ---------------------------------------
        # Extract Text
        # ---------------------------------------

        print("\nExtracting PDF text...")

        text = PDFParser.extract_text(file_path)

        # ---------------------------------------
        # Chunking
        # ---------------------------------------

        print("Creating chunks...")

        chunks = self.chunker.create_chunks(text)

        # ---------------------------------------
        # Build Documents
        # ---------------------------------------

        print("Building document objects...")

        builder = DocumentBuilder()

        documents = builder.build_documents(

            chunks=chunks,

            company=company,

            year=year,

            document_type="Annual Report",

            source=file.filename

        )

        # ---------------------------------------
        # Upload to Pinecone
        # ---------------------------------------

        print("Uploading vectors...")

        vector_count = self.vector_db.upsert_vectors(
            documents
        )

        # ---------------------------------------
        # Build Knowledge Graph
        # ---------------------------------------

        print("Building Knowledge Graph...")

        self.graph_builder.build(company)

        # ---------------------------------------
        # Response
        # ---------------------------------------

        return {

            "status": "success",

            "company": company,

            "chunks": vector_count,

            "message": "Document processed successfully."

        }