FROM python:3.10-alpine

WORKDIR /app

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["flask", "--app", "main", "run"]