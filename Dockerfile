# Use official Python 3.14 image
FROM python:3.14-slim

# Set work directory
WORKDIR /app

# Install required Python packages
RUN pip install --no-cache-dir bandit pytest

# Copy all project files
COPY . /app

# Create reports directories
RUN mkdir -p reports/bandit_reports reports/trivy_reports

# Default command: run unit tests
CMD ["python", "-m", "unittest", "discover"]
