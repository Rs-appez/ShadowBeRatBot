FROM python:3.10-slim

ENV TZ="Europe/Brussels"

RUN apt-get update \
    && apt-get install -y ffmpeg \
    && apt-get install -y nmap \
    && apt-get install -y openvpn

WORKDIR /shadowBeRatBot

COPY requirements.txt /shadowBeRatBot/
RUN pip install -r requirements.txt
COPY . /shadowBeRatBot/

CMD python main.py