from abc import ABC, abstractmethod
from datetime import datetime
import sys
import os
import pickle
import zlib
root = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))

sys.path.append(root)

from utils.utils import Status
from utils.request import Request

class Task(ABC):
    def __init__(self) -> None:
        self.time_scheduled = datetime.now()
        self.status = Status.WAITING
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
    
    def get_operator(self) -> None:
        r = Request(port=5057, service='ml_task')
        data = dict()
        data['name'] = self.__dict__['name']
        data['kind'] = self.__dict__['kind']
        data['operator'] = self.__dict__['operator']
        if 'params' in self.__dict__:
            data['params'] = self.__dict__['params']
        response = r.post(data)
        # converte a string para o objeto
        _obj = response['result']
        _obj = bytes(_obj.replace("b\"", "").replace("\"", ""), 'latin-1')
        _obj = zlib.decompress(_obj)
        _obj = pickle.loads(_obj)
        return _obj
    
    def run(self, data) -> any:
        operator = self.get_operator()
        return operator.fit_transform(data)
        
class DBTask(Task):
    def __init__(self) -> None:
        pass
    def run(self):
        pass