import os
import shutil

from backend.app.processing.pdf_parser import PDFParser
from backend.app.processing.chunker import DocumentChunker
from backend.app.processing.document_builder import DocumentBuilder

from backend.app.database.pinecone_db import PineconeDB
from backend.app.database.postgres import SessionLocal

from backend.app.graph.graph_builder import GraphBuilder

from backend.app.analysis.pipeline import AnalysisPipeline

from backend.app.repositories.analysis_repository import AnalysisRepository
from backend.app.utils.json_converter import to_json_serializable


class UploadService:

    def __init__(self):

        self.chunker = DocumentChunker()

        self.vector_db = PineconeDB()

        self.graph_builder = GraphBuilder()

        self.pipeline = AnalysisPipeline()

        self.analysis_repo = AnalysisRepository()

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

        documents = DocumentBuilder.build_documents(

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
        # Run Complete Analysis
        # ---------------------------------------

        print("Running Analysis Pipeline...")

        analysis = self.pipeline.run(company)

        # ---------------------------------------
        # Save Analysis to PostgreSQL
        # ---------------------------------------

        db = SessionLocal()

        try:

            self.analysis_repo.save_analysis(

                db=db,

                company=company,

                year=year,

                financial_data=to_json_serializable(
                    analysis["financial_data"]
                ),

                prophet_forecast=to_json_serializable(
                    analysis["prophet_forecasts"]
                ),

                xgboost_forecast=to_json_serializable(
                    analysis["xgboost_forecasts"]
                ),

                forecast_report=to_json_serializable(
                    analysis["forecast_report"]
                ),

                intelligence_report=to_json_serializable(
                    analysis["intelligence_report"]
                )

            )

        finally:

            db.close()

        # ---------------------------------------
        # Response
        # ---------------------------------------

        return {

            "status": "success",

            "company": company,

            "year": year,

            "chunks": vector_count,

            "message": "Document processed successfully and analysis saved."

        }