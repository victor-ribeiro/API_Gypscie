from fastapi import FastAPI
from redis import Redis
from rq import Queue, Worker
from typing import List
import sys
import os

root = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))
sys.path.append(root)

from worker import get_task_list

redis_con = Redis(host='redis', port=6379, db=1)
q = Queue('controler_queue', connection=redis_con)
app = FastAPI()

@app.post('/', status_code=201)
async def addWF(wf_request:List[dict]) -> dict:
    def func(t, params):
        job = q.enqueue(t, *params)
        w = Worker(q, connection=redis_con,)
        w.work(burst=True )
        return list(job.result)
    
    import numpy as np
    data = np.random.normal(0, 1, [2, 10])
    task_list = func(get_task_list, [wf_request])
    tmp = data.copy()
    tasK_response = []
    for t in task_list:
        tmp = func(t.run, tmp)
        tasK_response.append(tmp)
    response = dict()
    print(len(task_list), len(tasK_response))
    for task, _r in zip(task_list, tasK_response):
        response[task.name] = _r
    print(":::::::::::> RODEI AS TAREFAS", response)
    return{
        'result': response
        }