import requests as rq
from threading import Thread
import json


def run():
    api_url = "http://localhost:5057/group"
    data = {
        "name":'grupo1',
        "owner": 'str',
        "description": "foo"
        }
    response = rq.post(api_url, data=json.dumps(data))
    print(response.json())

for i in range(3):
    t = Thread(target=run)
    t.start()
