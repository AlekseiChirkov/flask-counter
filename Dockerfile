FROM python:3.8-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["flask", "--app", "main", "run"]