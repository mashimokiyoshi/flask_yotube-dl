FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y ffmpeg
RUN apt-get install python3 python3-pip -y
RUN pip3 install --upgrade pip

COPY . /home
WORKDIR /home

RUN pip3 install -r requirements.txt

RUN ls /home

ENV FLASK_APP app.py
RUN echo $FLASK_APP

RUN ls /home

CMD flask run -h 0.0.0.0 -p $PORT

