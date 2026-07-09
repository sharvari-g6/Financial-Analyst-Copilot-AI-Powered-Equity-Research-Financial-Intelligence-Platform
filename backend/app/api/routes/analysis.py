from fastapi import APIRouter
from fastapi import HTTPException

from backend.app.api.services.analysis_service import AnalysisService

router = APIRouter()

service = AnalysisService()


# =====================================================
# Get All Analyses
# =====================================================

@router.get("/analysis")
def get_all_analyses():

    return service.get_all()


# =====================================================
# Get Analysis by Company & Year
# =====================================================

@router.get("/analysis/{company}/{year}")
def get_analysis(
    company: str,
    year: int
):

    analysis = service.get_analysis(
        company,
        year
    )

    if analysis is None:

        raise HTTPException(
            status_code=404,
            detail="Analysis not found."
        )

    return analysis


# =====================================================
# Delete Analysis
# =====================================================

@router.delete("/analysis/{analysis_id}")
def delete_analysis(
    analysis_id: int
):

    success = service.delete(
        analysis_id
    )

    if not success:

        raise HTTPException(
            status_code=404,
            detail="Analysis not found."
        )

    return {

        "status": "success",

        "message": "Analysis deleted successfully."

    }