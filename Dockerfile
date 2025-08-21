FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --only=main --no-root --no-interaction --no-ansi

COPY ./app /app/app
COPY ./tests /app/tests

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
