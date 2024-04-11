FROM python:3.11

WORKDIR /app

COPY /translator /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
