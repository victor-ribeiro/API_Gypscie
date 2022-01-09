from abc import ABC, abstractmethod
from datetime import datetime

import sys

root = '/home/victor/Documentos/doutorado/disciplinas/1_periodo/arquitetura/trabalho_2/API_Gypscie/'
sys.path.append(root)

from utils import Status

class Task(ABC):
    _id = None
    def __init__(self, name:str, **kwargs) -> None:
        self.name = name
        self.time_scheduled = datetime.now()
        self.status = Status.WAITING
        for k, v in kwargs.items():
            self.__setattr__(k, v)
    def __str__(self):
        return self._id
    @abstractmethod
    def run(self) -> None:
        pass

class MLTask(Task):
    _id = "MLTask"
    def __init__(self, name:str, data: any, func: callable, params:dict=None) -> None:
        super().__init__(name=name)
        self.data = data
        self.func = func(**params) if params else func()
    def run(self):
        return self.func
    
class DBTask(Task):
    def __init__(self, name: str) -> None:
        pass