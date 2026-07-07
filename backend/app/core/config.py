from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    # -----------------------------
    # Application
    # -----------------------------

    APP_NAME = os.getenv("APP_NAME")

    # -----------------------------
    # PostgreSQL
    # -----------------------------

    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    # -----------------------------
    # Pinecone
    # -----------------------------

    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

    # -----------------------------
    # Ollama
    # -----------------------------

    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2:latest"
    )

    # -----------------------------
    # Neo4j
    # -----------------------------

    NEO4J_URI = os.getenv("NEO4J_URI")

    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")

    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    NEO4J_DATABASE = os.getenv(
        "NEO4J_DATABASE",
        "neo4j"
    )


settings = Settings()