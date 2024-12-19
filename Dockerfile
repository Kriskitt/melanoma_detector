FROM python:3.10.6-buster

COPY melanoma_detector melanoma_detector
COPY requirements.txt /requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


WORKDIR /melanoma_detector/api

CMD uvicorn api:app --host 0.0.0.0 --port $PORT
