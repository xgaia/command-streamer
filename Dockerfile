FROM python:3.9-alpine
MAINTAINER "Xavier Garnier"

COPY . /app
WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

RUN pip install flask gunicorn
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
