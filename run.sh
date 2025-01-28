#!/bin/bash
set -e;

# Navigate to the directory of the script
cd "$(dirname "$0")"

# Build the Docker image
docker build -t p79-runner .

# Run the container
docker run --rm p79-runner
