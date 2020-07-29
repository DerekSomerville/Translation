from abc import ABC, abstractmethod

class ImportDetermineInterface(ABC):

    @abstractmethod
    def generateImportStructure(self,line):
        pass

    @abstractmethod
    def isAnImport(self, line):
        pass
