import sys
import os
root = '/home/victor/Documentos/doutorado/disciplinas/1_periodo/arquitetura/trabalho_2/API_Gypscie/'
sys.path.append(root)

from file_parser.file_parser import JSONParser

from task_model import Task, MLTask, DBTask

class TaskList:
    def __init__(self, conf_path:str, *tasks) -> None:
        self.conf_path = conf_path
        self.tasks_conf = JSONParser().read_json(self.conf_path)
        print(self.tasks_dict)
    def is_valid(self, task:Task) -> bool:
        pass
    def dict_to_dict_list(self):
        pass