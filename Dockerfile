FROM python:3.7-slim

RUN apt-get update \
 && apt-get install -y wget firefox-esr \
 && rm -rf /var/lib/apt/lists/* \
 && wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz \
 && tar -xvzf geckodriver-v0.29.1-linux64.tar.gz \
 && rm geckodriver-v0.29.1-linux64.tar.gz \
 && chmod +x geckodriver \
 && mv geckodriver /usr/local/bin/ \
 && apt remove -y wget

WORKDIR /root/TweetScraper/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
