from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Response body for GET /health."""

    status: str
    app: str
    
class ItemResponse(BaseModel):
    """Response body for GET /items/{item_id}."""

    id: int
    name: str
