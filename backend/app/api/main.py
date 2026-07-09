from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes.health import router as health_router
from backend.app.api.routes.upload import router as upload_router
from backend.app.api.routes.chat import router as chat_router
from backend.app.api.routes.analysis import router as analysis_router


app = FastAPI(

    title="Financial Analyst Copilot",

    version="1.0.0",

    description=(
        "AI-powered Financial Analyst using "
        "RAG, GraphRAG, Forecasting and Multi-Agent Systems"
    )

)

# =====================================================
# CORS
# =====================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

# =====================================================
# API Routes
# =====================================================

app.include_router(

    health_router,

    prefix="/api",

    tags=["Health"]

)

print("Health loaded")

app.include_router(

    upload_router,

    prefix="/api",

    tags=["Upload"]

)

print("Upload loaded")

app.include_router(

    chat_router,

    prefix="/api",

    tags=["Chat"]

)

print("Chat loaded")

app.include_router(

    analysis_router,

    prefix="/api",

    tags=["Analysis"]

)

print("Analysis loaded")

# =====================================================
# Root
# =====================================================

@app.get("/")
def root():

    return {

        "application": "Financial Analyst Copilot",

        "version": "1.0.0",

        "status": "running"

    }