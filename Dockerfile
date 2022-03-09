FROM continuumio/anaconda3

WORKDIR /home

COPY requirements.txt requirements.txt

COPY Controler ./Controler/ 
COPY file_parser ./file_parser/
COPY Gypscie_Core ./Gypscie_Core/
COPY utils ./utils/

COPY worker.py ./
COPY Controler/controler.py ./
COPY Gypscie_Core/apy.py ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5057
EXPOSE 6057
EXPOSE 6379