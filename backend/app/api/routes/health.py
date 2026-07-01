from fastapi import APIRouter
from sqlalchemy import text

from backend.app.database.postgres import engine
from backend.app.database.neo4j_db import driver
from backend.app.database.pinecone_db import pc

router = APIRouter()

@router.get("/health")
def health_check():

    status = {}

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        status["postgres"] = "connected"

    except Exception as e:
        status["postgres"] = f"error: {str(e)}"

    try:
        driver.verify_connectivity()
        status["neo4j"] = "connected"

    except Exception as e:
        status["neo4j"] = f"error: {str(e)}"

    try:
        pc.list_indexes()
        status["pinecone"] = "connected"

    except Exception as e:
        status["pinecone"] = f"error: {str(e)}"

    return status