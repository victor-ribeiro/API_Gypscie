import sys
from abc import ABC, abstractclassmethod, abstractmethod

root = '/home/victor/Documentos/doutorado/disciplinas/1_periodo/arquitetura/trabalho_2/API_Gypscie/'
sys.path.append(root)

from file_parser.file_parser import JSONParser
from task_model import Task, MLTask

class TaskParser(ABC):
    def __init__(self, task_dict:dict) -> None:
        validator = TaskValidator()
        if not validator.validate_task(dict_task=task_dict):
            raise ValueError("operação invalida, confira a sintaxe ou o manual")
        self.dict_task = task_dict
        self.task_supertype = [*self.dict_task.keys()][0]
    @abstractmethod
    def get_task(self) -> Task:
        pass

class TaskValidator(JSONParser):
    def __init__(self):
        super().__init__()
        self.conf_tasks = self.read_json('conf_tasks.json')
    def validate_task(self, dict_task:dict) -> bool:
        # validação do supertipo de poração
        task_op = [*dict_task.keys()][0] # DBTastk, MLTask, GraphTask ou TSTask
        return task_op in self.conf_tasks['valid']

class MLTaskParser(TaskParser):
    def __init__(self, task_dict:dict) -> None:
        super().__init__(task_dict=task_dict)
    def get_task(self) -> Task:
        _params = self.dict_task[self.task_supertype]
        _params['kind'] = f"sklearn.{_params['kind']}"
        return MLTask(**self.dict_task[self.task_supertype])
    
class TaskList(list):
    def __init__(self, *tasks) -> None:
        super().__init__()
        for task in tasks:
            self.append(task)
    def run_all(self):
        for task in self:
            task.run()