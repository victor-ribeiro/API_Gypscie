from enum import Enum, unique
import random
from datetime import datetime
import sys

root = '/home/victor/Documentos/doutorado/disciplinas/1_periodo/arquitetura/trabalho_2/API_Gypscie/'
sys.path.append(root)

from file_parser.file_parser import JSONParser

def generate_name(format:str=None)->str:
    """Gera um nome aleatório para o arquivo.

    Args:
        format (str): extensão do arquivo. Não deve conter o '.' para a extensão

    Returns:
        [str]: nome aleatório completo do arquivo.
    """
    val = random.gauss(mu=0, sigma=1) * random.randint(0, 10e4)
    now = str(datetime.now())
    now = now.replace("-", "_")
    now = now.replace(":", "_")
    now = now.replace(" ", "_")
    name = f'{now}_{hash(val)}.{format}' if format else f'{now}_{hash(val)}'
    return name


@unique
class Status(Enum):
    WAITING = 1
    RUNNING = 2
    FAIL = 3
    SUCCESS = 4

class TaskValidator(JSONParser):
    def __init__(self):
        super().__init__()
        self.conf_tasks = self.read_json('conf_tasks.json')
    def validate_task(self, dict_task:dict) -> bool:
        # validação do supertipo de poração
        task_op = [*dict_task.keys()][0] # DBTastk, MLTask, GraphTask ou TSTask
        if not (task_op in self.conf_tasks['valid']):
            return False        
        # validação do tipo de opração 
        mapper = self.conf_tasks['map_app']
        conf_file = self.read_json(mapper[task_op]['conf_file'])
        if not(dict_task[task_op]['kind'] in conf_file.keys()):
            return False
        #validação do operador
        operator = dict_task[task_op]['kind']
        return dict_task[task_op]['operator'] in conf_file[operator]