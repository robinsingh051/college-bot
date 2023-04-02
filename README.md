# College Admission Chatbot

## Purpose
The purpose of this project is to implement an intelligent voice assistant to answer common queries that parents and students may have while taking admission. The chatbot provides appropriate responses to failures and queries. 

## Features
- Built using Rasa chatbot framework
- Utilizes Vosk API for offline speech recognition
- Utilizes Pyttsx3 for text to speech conversion
- Uses Spacy for natural language processing
- Can be run locally
- Easy to customize and add new queries

## Run Locally
1. Clone the project
  git clone https://github.com/robinsingh051/college-bot

2. Go to the project directory
  cd college-bot

3. Install dependencies
```bash
    pip install rasa==3.1
    pip install spacy
    pip install requests
    pip install vosk
    pip install pyttsx3
    python -m spacy download en_core_web_lg
```
open terminal in this directory and run the following command to start rasa server
```bash
  rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
```

open another terminal to run voice assistant
```bash
    python v.py
```

## Tech Stack
<p align="left">
  <img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" alt="python" width="40" height="40"/>
  <img src="https://www.vectorlogo.zone/logos/rasahq/rasahq-icon.svg" alt="rasa" width="40" height="40"/>
  <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/>
</p>
 
## Team Members
- [Robin Singh](https://github.com/robinsingh051)
- [Sanjana Pradhan](https://github.com/Sanjana27-11)

