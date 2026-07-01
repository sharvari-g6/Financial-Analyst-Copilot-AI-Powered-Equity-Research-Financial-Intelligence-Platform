from neo4j import GraphDatabase
from backend.app.core.config import settings

driver = GraphDatabase.driver(
    settings.NEO4J_URI,
    auth=(
        settings.NEO4J_USERNAME,
        settings.NEO4J_PASSWORD
    )
)

def get_driver():
    return driver