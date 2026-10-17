from fastapi import FastAPI, HTTPException

from app import store
from app.config import settings
from app.schemas import HealthResponse, ItemCreate, ItemResponse

app = FastAPI(title=settings.app_name)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Return service status. Never raises."""
    return HealthResponse(status="ok", app=settings.app_name)


@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(body: ItemCreate) -> ItemResponse:
    """Create an item and return it with its assigned id."""
    return store.create_item(body)


@app.get("/items", response_model=list[ItemResponse])
def list_items() -> list[ItemResponse]:
    """Return all items."""
    return store.list_items()


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int) -> ItemResponse:
    """Return a single item by id. Raises 404 if it does not exist."""
    item = store.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    """Delete an item by id. Raises 404 if it does not exist."""
    if not store.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
