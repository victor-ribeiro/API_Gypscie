from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get('/hello')
def hello():
    """test endpoint"""
    return {'hello', 'world', datetime.now()}