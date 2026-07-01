from fastapi import FastAPI

from backend.app.api.routes.health import router as health_router

app = FastAPI(
    title="Financial Analyst Copilot"
)

app.include_router(health_router)

@app.get("/")
def root():

    return {
        "message": "Financial Analyst Copilot API Running"
    }