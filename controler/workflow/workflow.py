import sys
import os
root = '/home/victor/Documentos/doutorado/disciplinas/1_periodo/arquitetura/trabalho_2/API_Gypscie/'
sys.path.append(root)

from file_parser.file_parser import JSONParser

from abc import ABC, abstractmethod
from datetime import datetime
from utils import Status

class Task(ABC):
    name: str
    time_scheduled: datetime
    status: Status
    def __init__(self, name:str) -> None:
        self.name = name
        self.time_scheduled = datetime.now()
        self.status = Status.WAITING
    @abstractmethod
    def run(self) -> None:
        pass

class TaskList:
    def __init__(self, conf_path:str) -> None:
        self.conf_path = conf_path
        self.tasks_dict = JSONParser().read_json(self.conf_path)
        print(self.tasks_dict)
    def is_valid(self):
        pass
    def dict_to_dict_list(self):
        pass
    
if __name__ == '__main__':
    t = TaskList(conf_path='conf_sklearn.json')

class MLTask(Task):
    def __init__(self, name:str, data: any, func: callable, params:dict=None) -> None:
        super().__init__(name=name)
        self.data = data
        self.func = func(**params) if params else func()
    def run(self):
        return self.func.fit_transform(self.data)
    
class DBTask(Task):
    def __init__(self, name: str) -> None:
        super().__init__(name)