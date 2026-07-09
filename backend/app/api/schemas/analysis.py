from pydantic import BaseModel
from typing import Any


class AnalysisResponse(BaseModel):

    id: int

    company: str

    year: int

    upload_date: str

    financial_data: Any

    prophet_forecast: Any

    xgboost_forecast: Any

    forecast_report: Any

    intelligence_report: Any


class AnalysisListItem(BaseModel):

    id: int

    company: str

    year: int

    upload_date: str