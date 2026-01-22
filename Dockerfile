FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim
WORKDIR /app

# Install dependencies (doing this as a separate copy steps improves caching)
COPY pyproject.toml uv.lock .
RUN uv sync --locked --all-groups

# Copy over remaining code, tests, and configurations
COPY . .

# Perform type checking and linting at build time
RUN uv run --locked ty check
RUN uv run --locked ruff check

ENTRYPOINT ["/bin/bash", "-c", "uv run -m unittest"]
