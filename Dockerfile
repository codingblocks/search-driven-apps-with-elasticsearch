FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY flask /app
WORKDIR /app
RUN pip install flask
RUN pip install requests
ENTRYPOINT ["python"]
CMD ["app.py"]