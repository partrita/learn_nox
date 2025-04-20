FROM python:3.12-slim

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container
COPY . /app

# Set working directory
WORKDIR /app

# Install dependencies
RUN uv sync --frozen --no-cache

# Run the FastAPI app
CMD ["/app/.venv/bin/fastapi", "run", "src/acebet/api.py", "--port", "80", "--host", "0.0.0.0"]
