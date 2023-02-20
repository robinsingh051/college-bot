FROM python:3.8

RUN python -m pip install rasa==3.1

WORKDIR '/app'

COPY . .

RUN rasa train

USER 1001

CMD rasa run --enable-api --port $PORT