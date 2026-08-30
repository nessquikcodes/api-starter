from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Response body for GET /health."""

    status: str
    app: str
