from fastapi import FastAPI

from app.config import settings
from app.schemas import HealthResponse, ItemResponse

app = FastAPI(title=settings.app_name)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Return service status. Never raises."""
    return HealthResponse(status="ok", app=settings.app_name)

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int) -> ItemResponse:
    """Return a single item by id."""
    return ItemResponse(id=item_id, name="widget")
