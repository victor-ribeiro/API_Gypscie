from enum import Enum, unique
import random
from datetime import datetime
import json

@unique
class Status(Enum):
    WAITING = 1
    RUNNING = 2
    FAIL = 3
    SUCCESS = 4
    
def generate_name(format:str=None) -> str:
    """
    Gera um nome aleatório para o arquivo.

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