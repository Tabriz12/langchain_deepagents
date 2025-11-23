FROM python:3.12-slim

RUN apt-get update && apt-get install -y git

ENV POETRY_VERSION=2.2.1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

# only install dependencies here
COPY . /app
RUN poetry install


# CMD ["poetry", "run", "python", "-m", "langchain_deepagents.main"]


# docker build -t lc-deepagents:0.1 .
# docker run -it --rm -v $(pwd):/app lc-deepagents:0.1 poetry run python -m langchain_deepagents.main