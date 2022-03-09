import sys
from abc import ABC, abstractmethod

import os
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))))
sys.path.append(root)

from file_parser import file_parser
from . import task_model

class TaskValidator(file_parser.JSONParser):
    def __init__(self):
        super().__init__()
        self.conf_tasks = self.read_json('Controler/workflow/conf_tasks.json')
    def validate_task(self, dict_task:dict) -> bool:
        # validação do supertipo de operação
        task_op = [*dict_task.keys()][0] # DBTastk, MLTask, GraphTask ou TSTask
        return task_op in self.conf_tasks['valid']

class TaskParser(ABC):
    def __init__(self, task_dict:dict) -> None:
        validator = TaskValidator()
        if not validator.validate_task(dict_task=task_dict):
            raise ValueError("operação invalida, confira a sintaxe ou o manual")
        self.dict_task = task_dict
        self.task_supertype = [*self.dict_task.keys()][0]
    @abstractmethod
    def get_task(self):
        pass

class MLTaskParser(TaskParser):
    def __init__(self, task_dict:dict):
        super().__init__(task_dict=task_dict)
    def get_task(self):
        _params = self.dict_task[self.task_supertype]
        _params['kind'] = f"sklearn.{_params['kind']}"
        return task_model.MLTask(**self.dict_task[self.task_supertype])
    
class TaskList(list):
    def __init__(self, *tasks):
        super().__init__()
        for task in tasks:
            self.append(task)
    def run_all(self, data):
        tmp_data = data
        for task in self:
            yield task.run(tmp_data)