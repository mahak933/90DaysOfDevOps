
FROM python:3.12-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000

CMD ["python", "hello.py"]

