FROM python:3.9-slim

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password \
    MONGO_URL=mongodb://admin:password@mongodb:27017

RUN mkdir -p /home/app

COPY requirements.txt /home/app/
COPY app.py /home/app/
COPY index.html /home/app/

# COPY ./app /home/app

WORKDIR /home/app

RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]
