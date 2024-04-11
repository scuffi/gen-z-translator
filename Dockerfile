FROM tiangolo/uvicorn-gunicorn:python3.11
WORKDIR /app/
COPY /translator /app/
COPY requirements.txt /app/
RUN pip install -U pip && pip install -r requirements.txt

WORKDIR /app

CMD ["uvicorn", "app.asgi:api", "--host", "0.0.0.0", "--port", "3000", "--reload"]
