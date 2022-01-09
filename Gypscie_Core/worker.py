from typing import Any

class MLWorker:
    """Classe para a importação de classes e módulos python em tempo de execução
        Args:
                import_from (str): caminho absoluto de importação 
                get_module('numpy') equivalente a :
                - import numpy
                import_class (str, optional): classe, ou função a ser importada. Defaults to None.
                get_module('numpy', 'array') equivalente a :
                - from numpy import array
            Return
                Python object com a classe que se deseja instanciar    
    """
    def __init__(self) -> None:
        pass
    def get_module(self, import_from:str, import_class:str = None) -> Any:
        from_list = import_from.split('.')
        mod = __import__(import_from, fromlist=from_list, globals=globals(), level=0)
        if import_class:
            mod = getattr(mod, import_class)
        return mod
    