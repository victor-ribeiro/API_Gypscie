from enum import Enum, unique

@unique
class Status(Enum):
    WAITING = 1
    RUNNING = 2
    FAIL = 3
    SUCCESS = 4