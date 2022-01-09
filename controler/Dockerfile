FROM continuumio/anaconda3
WORKDIR /home

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY *.py ./
COPY utils ./
RUN ls utils

COPY workflow ./
RUN workflow