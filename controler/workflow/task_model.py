from abc import ABC, abstractmethod
from datetime import datetime

from utils import Status

class Task(ABC):
    _id = None
    def __init__(self, name:str) -> None:
        self.name = name
        self.time_scheduled = datetime.now()
        self.status = Status.WAITING
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
        super().__init__(name)