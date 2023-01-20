FROM python:3.8-slim

WORKDIR /app

COPY src ./src
COPY pyproject.toml .
COPY poetry.lock .

RUN pip install poetry
RUN poetry install --no-dev

COPY nltk_data_init.py .

RUN poetry run python nltk_data_init.py

EXPOSE 8080

CMD ["poetry", "run", "python", "-m", "src.main"]
