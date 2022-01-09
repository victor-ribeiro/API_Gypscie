from abc import ABC, abstractmethod
from datetime import datetime
import sys
import os
root = os.path.dirname(os.path.dirname(os.path.abspath("__file__")))

sys.path.append(root)

from utils.utils import Status

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
    def run(self):
        return self.func

class DBTask(Task):
    def __init__(self) -> None:
        pass
    def run(self):
        pass