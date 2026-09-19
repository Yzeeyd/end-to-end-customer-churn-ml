FROM python:3.11-slim

COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:1.0.0 \
    /lambda-adapter /opt/extensions/lambda-adapter

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8000

CMD ["python", "-m", "uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]