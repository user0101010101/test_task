FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r /app/requirements.txt

COPY . .

CMD ["python3", "/app/src/start.py"]

EXPOSE 10000
