from abc import ABC, abstractmethod
from libs.programador import Programador

class LogHistorico(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def guardaLog(self, nomFich):
        pass



