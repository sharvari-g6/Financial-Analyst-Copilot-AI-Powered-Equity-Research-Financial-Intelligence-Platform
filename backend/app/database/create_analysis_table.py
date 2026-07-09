from backend.app.database.postgres import engine

from backend.app.database.base import Base

# Import models so SQLAlchemy registers them
from backend.app.models.analysis_result import AnalysisResult


def create_tables():

    Base.metadata.create_all(bind=engine)

    print("Analysis table created successfully.")


if __name__ == "__main__":

    create_tables()