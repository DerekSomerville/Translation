from src.main.Languages.ImportStructure import ImportStructure
from src.main.Languages.ImportDetermineInterface import ImportDetermineInterface

class JavaImportDetermine(ImportDetermineInterface):

    def isAnImport(self, line):
        result = False
        if "import" in line.getWords():
            result = True
        return result

    def generateImportStructure(self,line):
        importStructure = ImportStructure()


        return importStructure
