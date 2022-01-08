FROM python:3.8-alpine

RUN adduser -D myproj

WORKDIR /home/myproj

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY api_server.py ./
COPY worker.py ./

RUN chown -R myproj:myproj ./

USER myproj

# CMD uvicorn api_server:app --host 0.0.0.0 --port 5057