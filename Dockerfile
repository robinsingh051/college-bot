FROM python:3.8-buster AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

RUN pip install rasa==3.1
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download en_core_web_md-3.2.0

COPY ./actions /app/actions

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml

EXPOSE 5005
CMD ["--help"]