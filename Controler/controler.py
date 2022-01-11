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
    import numpy as np
    data = np.random.normal(0, 1, [200, 10])
    job = q.enqueue(get_task_list, [wf_request])
    w = Worker(q, connection=redis_con,)
    w.work(burst=True )
    task_list = job.result
    
    tmp = data.copy()
    tasK_response = []
    print(":::::::::::> RODEI AS TAREFAS", len(task_list), task_list)
    for t in task_list:
        tmp = await t.run(tmp)
        tasK_response.append(tmp)
    response = dict()
    for task, _r in zip(task_list, tasK_response):
        response[task.name] = _r
    print(":::::::::::> RODEI AS TAREFAS", response)
    return{
        'result': response
        }