import numpy as np
from fastapi import FastAPI
from redis import Redis
from rq import Queue, Worker
from typing import List
import sys
import os
root = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(root)

from worker import get_task_list

import json
import requests

redis_con = Redis(host='redis', port=6379, db=1)
q = Queue('controler_queue', connection=redis_con)
app = FastAPI()

@app.post('/', status_code=201)
async def addWF(wf_request:List[dict]) -> dict:
    data = np.random.normal(0, 1, [200, 10])
    w = Worker([q], connection=redis_con,)
    w.work(burst=True)
    # await w.work()
    task_list = await get_task_list(wf_request)
    response = dict()
    for t in task_list:
        print(type(t.get_operator()))
        response[t.name] = t.run(data).tolist()
    return {'result': response}