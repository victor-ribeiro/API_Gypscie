import json
import os
from typing import List

import sys

root = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.append(root)

from utils.utils import generate_name

class FileParser:
    def read_file(self, file_path:str) -> str:
        with open(file_path, 'r') as file:
            data_file = file.read()
            return data_file
    def write_file(self, data:dict, file_ext:str=None, save_path:str = None, file_name:str = None) -> None:
        if file_ext and file_name:
            raise ValueError('não use "file_name" e "file_ext" juntos')
        name = file_name if file_name else generate_name(file_ext)
        if save_path:
            path = os.path.join(save_path, name)
            if not os.path.exists(path):
                os.makedirs(save_path)
            with open(path, 'w') as file:
                file.writelines(data)
        else:
            with open(name, 'w') as file:
                file.writelines(data)


class JSONParser:
    def read_json(self, json_path:str) -> dict:
        parser = FileParser()
        data_file = parser.read_file(file_path=json_path)
        json_file = json.loads(data_file)
        return json_file
    
    def write_json(self, data:dict, save_path:str = None, file_name:str = None) -> None:
        parser = FileParser()
        content = json.dumps(data, indent=True)
        if file_name:
            parser.write_file(data=content, save_path=save_path, file_name=file_name)
        else:
            parser.write_file(data=content, save_path=save_path, file_ext='json')