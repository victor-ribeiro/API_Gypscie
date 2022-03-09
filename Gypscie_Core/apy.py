from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pickle import dumps, dump
from pydantic import BaseModel
from redis import Redis
from typing import Dict
from rq import Queue, Worker
import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(root)
import zlib

from worker import MLWorker
from Controler.workflow import task_model
redis_con = Redis(host='redis', port=6379, db=1)
q = Queue('gypscie_queue', connection=redis_con)

app = FastAPI()

class MLTask(BaseModel):
    name: str
    kind: str
    operator: str
    params:Dict= None

@app.post('/ml_task', status_code=201)
async def addMLTask(ml_task:MLTask) -> dict:
    o = MLWorker()
    print(ml_task)
    # ml_task = task_model.MLTask(**ml_task)
    job = q.enqueue(o.get_module, import_from=ml_task.kind, import_class=ml_task.operator)
    w = Worker(q, connection=redis_con,)
    w.work(burst=True)
    # serialização do objeto para string
    result = dumps(job.result)
    result = zlib.compress(result, zlib.Z_NO_COMPRESSION)
    return {
        'result': str(result, 'latin-1'),
        'import_from' : ml_task.kind, 
        'import_class': ml_task.operator
        }