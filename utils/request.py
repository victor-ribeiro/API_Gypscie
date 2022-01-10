from dataclasses import dataclass
import requests as rq
import json

@dataclass
class Request:
    port: int
    service:str
    url = "http://localhost"
    
    def post(self, data:dict) -> any:
        _data = json.dumps(data)
        _url = f'{self.url}:{self.port}/{self.service}'

        #resquisição para o serviço
        response = rq.post(_url, data=_data)
        response = response.json()
        
        return response