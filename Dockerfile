FROM python:3.12-slim
WORKDIR /app

# Install dependencies (do not forget to update requirements.txt if you install new packages)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy over code and tests (adapt if you have a different structure)
COPY hash/ hash/
COPY tests/ tests/

# Copy the test runner script
COPY run_tests.sh .
RUN chmod +x run_tests.sh

ENTRYPOINT ["./run_tests.sh"]
