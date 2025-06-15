FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /bot

RUN pip install --upgrade pip wheel 'poetry==2.1.3'

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

COPY . .

RUN poetry install --no-root

CMD ["poetry", "run", "python3", "main.py"]
