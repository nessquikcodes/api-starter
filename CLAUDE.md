# Project guide

FastAPI backend. Python 3.12. Tests with pytest, lint and format with ruff.

Run before opening a PR:

    ruff check . && ruff format --check . && pytest -q

## Review rules

When reviewing a PR, flag any of the following. Be specific: name the file and line.

1. **Every new or changed route has a test.** A route in `app/` needs a matching test in `tests/` that calls it through `TestClient` and checks status code and response body. No test, no merge.

2. **No bare or silent excepts.** `except:` and `except Exception:` are only allowed if they log or re-raise. Catch the specific exception you expect. (ruff enforces E722 and BLE001.)

3. **Public functions have docstrings.** One sentence is enough. Say what it returns and what it raises. (ruff enforces D103.)

4. **Request and response bodies are Pydantic models.** Route signatures must not accept or return raw `dict`. Put models in `app/schemas.py`.

5. **No secrets or environment-specific values in code.** Read config from environment variables through `app/config.py`. Flag any hardcoded URL, key, password, or port.

## Style

- Prefer small functions. If a route handler is over ~30 lines, suggest splitting it.
- Don't suggest adding type hints where they already exist, and don't nitpick formatting; ruff owns that.
- If the PR looks correct and follows the rules, say so briefly. Don't invent problems.
