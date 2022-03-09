from abc import ABC, abstractmethod
from datetime import datetime
from urllib import response
import requests as rq
import pickle
import zlib
import sys
import os
import json
import requests

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))))
sys.path.append(root)

from utils import request as ml_request
import time

class Task(ABC):
    def __init__(self) -> None:
        self.time_scheduled = datetime.now()
    @abstractmethod
    def run(self) -> None:
        pass

class MLTask(Task):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        if not ('kind' in kwargs) and not ('operator' in kwargs):
            raise ValueError("A definição de Task deve conter 'kind' e 'operator'")
        for k, v in kwargs.items():
            self.__setattr__(k, v)
    def __dict__(self):
        tmp = dict(name = self.name,
            kind = self.kind,
            operator = self.operator
            )
        if hasattr(self, 'params'):
            tmp['params'] = self.params
        return tmp
        
    def get_operator(self) -> any:
        r = ml_request.Request(port=5057, service='ml_task')
        response = r.post(self.__dict__())
        if 'result' in response:
            _obj = response['result']
            # _obj = bytes(_obj.replace("b\"", ""), 'latin-1')
            _obj = bytes(_obj, 'latin-1')
            _obj = zlib.decompress(_obj)
            _obj = pickle.loads(_obj)
            return _obj(**self.params) if self.params else _obj()
        return response

    def run(self, data):
        _obj = self.get_operator()
        _obj.fit(data)
        return _obj.transform(X=data)
        
class DBTask(Task):
    def __init__(self) -> None:
        pass
    def run(self):
        pass