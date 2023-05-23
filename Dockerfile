FROM python:3.8-buster AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim
WORKDIR '/app'

RUN pip install --no-cache-dir --upgrade pip
RUN pip install rasa==3.1
RUN pip install -U spacy==3.2.4
RUN python -m spacy download en_core_web_md

COPY . .

RUN rasa train

USER 1001

CMD rasa run --enable-api --port $PORT