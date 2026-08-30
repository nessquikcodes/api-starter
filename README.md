# api-starter

FastAPI backend with ruff/pytest CI and a Claude PR-review agent.

    pip install -e ".[dev]"
    ruff check . && ruff format --check . && pytest -q
    uvicorn app.main:app --reload
