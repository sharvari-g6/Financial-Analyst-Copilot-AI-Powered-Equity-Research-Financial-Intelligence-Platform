from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from backend.app.database.base import Base


class AnalysisResult(Base):

    __tablename__ = "analysis_results"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    company = Column(
        String,
        nullable=False
    )

    year = Column(
        Integer,
        nullable=False
    )

    upload_date = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    financial_data = Column(JSONB)

    prophet_forecast = Column(JSONB)

    xgboost_forecast = Column(JSONB)

    forecast_report = Column(JSONB)

    intelligence_report = Column(JSONB)