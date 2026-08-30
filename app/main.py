from fastapi import FastAPI

from app.config import settings
from app.schemas import HealthResponse

app = FastAPI(title=settings.app_name)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Return service status. Never raises."""
    return HealthResponse(status="ok", app=settings.app_name)

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Return a single item by id."""
    return {"id": item_id, "name": "widget"}
