from sqlalchemy.orm import Session

from backend.app.models.analysis_result import AnalysisResult


class AnalysisRepository:

    # ============================================
    # Save Analysis
    # ============================================

    def save_analysis(

        self,

        db: Session,

        company: str,

        year: int,

        financial_data,

        prophet_forecast,

        xgboost_forecast,

        forecast_report,

        intelligence_report

    ):

        analysis = AnalysisResult(

            company=company,

            year=year,

            financial_data=financial_data,

            prophet_forecast=prophet_forecast,

            xgboost_forecast=xgboost_forecast,

            forecast_report=forecast_report,

            intelligence_report=intelligence_report

        )

        db.add(analysis)

        db.commit()

        db.refresh(analysis)

        return analysis

    # ============================================
    # Get Analysis
    # ============================================

    def get_analysis(

        self,

        db: Session,

        company: str,

        year: int

    ):

        return (

            db.query(AnalysisResult)

            .filter(

                AnalysisResult.company == company,

                AnalysisResult.year == year

            )

            .first()

        )

    # ============================================
    # Get All Analyses
    # ============================================

    def get_all(

        self,

        db: Session

    ):

        return (

            db.query(AnalysisResult)

            .order_by(

                AnalysisResult.upload_date.desc()

            )

            .all()

        )

    # ============================================
    # Delete
    # ============================================

    def delete(

        self,

        db: Session,

        analysis_id: int

    ):

        analysis = (

            db.query(AnalysisResult)

            .filter(

                AnalysisResult.id == analysis_id

            )

            .first()

        )

        if analysis:

            db.delete(analysis)

            db.commit()

            return True

        return False