FROM python:3.8

RUN apt-get update
RUN apt-get upgrade -y
 
RUN apt-get install git -y
RUN mkdir /home/fibonacci
COPY . /home/fibonacci
WORKDIR /home/fibonacci
RUN pip3 install -r requirements.txt