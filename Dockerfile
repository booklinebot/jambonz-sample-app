FROM python:3.9-slim

# Install git
RUN apt-get update -y && apt-get install git -y

# Install Poetry
ENV POETRY_VERSION=1.1.12
RUN pip install "poetry==$POETRY_VERSION"

# Install Python dependencies
WORKDIR /usr/lib/app/
COPY poetry.lock pyproject.toml /usr/lib/app/
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# Add Python source files
COPY sample/ /usr/lib/app/

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
