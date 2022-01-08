from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from redis import Redis

from rq import Queue, Worker

#arquivo worker
import worker as func

# request body classes
class Group(BaseModel):
    name: str
    owner: str
    description: str = None

redis_con = Redis(host='my_redis', port=6379, db=1)
q = Queue('my_queue', connection=redis_con)

app = FastAPI()

@app.get('/hello')
def hello():
    return {"hello":"world"}

@app.post("/test")
def test_func():
    return  {"teste": "pass"}

@app.post('/group', status_code=201)
async def addTask(group:Group) -> dict:
    print(len(q.get_jobs()))
    if not group.name in ('grupo1', 'grupo2'):
        raise HTTPException(status_code=404, detail='Grupo nao encontrado')
    job = q.enqueue(func.runTask, group.owner, group.description)
    w = Worker(q, connection=redis_con,)
    w.work(burst=True)
    print(len(q.get_jobs()))
    return {
        'result': job.result, 
        'result_value': job.return_value
        }