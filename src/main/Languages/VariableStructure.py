from src.main.Languages.DeclareStructure import DeclareStructure

class VariableStructure(DeclareStructure):
    name = None
    private = True
    variableType = None

    def __init__(self,name,private,variableType=None):
        self.name = name
        self.private = private
        self.variableType = variableType

    def getVariableType(self):
        return self.variableType
