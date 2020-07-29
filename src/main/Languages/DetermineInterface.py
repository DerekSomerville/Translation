from abc import ABC, abstractmethod

class DetermineInterface(ABC):

    @abstractmethod
    def print(self, line):
        pass
