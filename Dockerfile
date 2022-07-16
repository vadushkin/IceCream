FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /main
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8000