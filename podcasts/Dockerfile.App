FROM python:2.7-slim

WORKDIR /app

COPY app /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "app.py"]