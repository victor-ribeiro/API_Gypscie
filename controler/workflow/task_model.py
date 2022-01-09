from abc import ABC, abstractmethod
from datetime import datetime

import sys

root = '/home/victor/Documentos/doutorado/disciplinas/1_periodo/arquitetura/trabalho_2/API_Gypscie/'
sys.path.append(root)

from utils.utils import Status

class Task(ABC):
    def __init__(self) -> None:
        self.time_scheduled = datetime.now()
        self.status = Status.WAITING
    def __str__(self):
        return self._id
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
    def run(self):
        return self.func

class DBTask(Task):
    def __init__(self) -> None:
        pass
    def run(self):
        pass