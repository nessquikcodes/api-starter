from fastapi import FastAPI

from app.config import settings
from app.schemas import HealthResponse

app = FastAPI(title=settings.app_name)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Return service status. Never raises."""
    return HealthResponse(status="ok", app=settings.app_name)
