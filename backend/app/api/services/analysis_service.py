from backend.app.database.postgres import SessionLocal
from backend.app.repositories.analysis_repository import AnalysisRepository


class AnalysisService:

    def __init__(self):

        self.repo = AnalysisRepository()

    # ============================================
    # Get Single Analysis
    # ============================================

    def get_analysis(
        self,
        company: str,
        year: int
    ):

        db = SessionLocal()

        try:

            analysis = self.repo.get_analysis(

                db,

                company,

                year

            )

            if analysis is None:

                return None

            return {

                "id": analysis.id,

                "company": analysis.company,

                "year": analysis.year,

                "upload_date": str(analysis.upload_date),

                "financial_data": analysis.financial_data,

                "prophet_forecast": analysis.prophet_forecast,

                "xgboost_forecast": analysis.xgboost_forecast,

                "forecast_report": analysis.forecast_report,

                "intelligence_report": analysis.intelligence_report

            }

        finally:

            db.close()

    # ============================================
    # List Analyses
    # ============================================

    def get_all(self):

        db = SessionLocal()

        try:

            analyses = self.repo.get_all(db)

            return [

                {

                    "id": item.id,

                    "company": item.company,

                    "year": item.year,

                    "upload_date": str(item.upload_date)

                }

                for item in analyses

            ]

        finally:

            db.close()

    # ============================================
    # Delete
    # ============================================

    def delete(
        self,
        analysis_id: int
    ):

        db = SessionLocal()

        try:

            return self.repo.delete(

                db,

                analysis_id

            )

        finally:

            db.close()