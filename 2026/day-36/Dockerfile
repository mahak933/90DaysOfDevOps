FROM python:3.11-slim

RUN groupadd -r project && useradd -r -g project mahak


WORKDIR /app

COPY requirements.txt .

RUN pip install  -r requirements.txt

COPY . .

COPY app.py .

RUN chown -R mahak:project /app

USER mahak

EXPOSE 5000

CMD ["python", "app.py"]
