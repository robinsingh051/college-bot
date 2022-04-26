FROM python:3.7-slim

RUN python -m pip install rasa==2.0

WORKDIR '/app'

COPY . .

RUN rasa train

USER 1001

CMD rasa run --enable-api --port $PORT