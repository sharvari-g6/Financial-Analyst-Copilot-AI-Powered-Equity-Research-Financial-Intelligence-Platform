from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.routes.upload import router as upload_router
from backend.app.api.routes.health import router as health_router


app = FastAPI(

    title="Financial Analyst Copilot",

    version="1.0.0",

    description="AI-powered Financial Analyst using RAG, GraphRAG, Forecasting and Multi-Agent Systems"

)

# -----------------------------------
# CORS
# -----------------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

# -----------------------------------
# Routes
# -----------------------------------

app.include_router(

    health_router,

    tags=["Health"]

)

app.include_router(
    upload_router,
    tags=["Upload"]
)


@app.get("/")
def root():

    return {

        "application": "Financial Analyst Copilot",

        "version": "1.0.0",

        "status": "running"

    }