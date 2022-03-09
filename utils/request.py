from dataclasses import dataclass
import requests as rq
import json



@dataclass
class Request:
    port: int
    service:str
    
    def post(self, data:dict) -> dict:
        _data = json.dumps(data)
        _url = f'http://gypscie_core_api:{self.port}/{self.service}'
        #resquisição para o serviço
        response = rq.post(_url, data=_data, headers={'Content-Type': 'application/json'})
        response = response.json()
        return response
    def get(self) -> dict:
        pass
    def put(self, data:dict) -> dict:
        pass