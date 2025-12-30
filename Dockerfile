FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim
WORKDIR /app

# Install dependencies (doing this as a separate copy steps improves caching)
COPY pyproject.toml .
RUN uv sync

# Copy over remaining code, tests, and configurations
COPY . .

ENTRYPOINT ["/bin/bash", "-c", "uv run -m unittest"]
