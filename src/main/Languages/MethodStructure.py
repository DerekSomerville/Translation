from src.main.Languages.DeclareStructure import DeclareStructure
from src.main.Utilities.Word import Word

class MethodStructure(DeclareStructure):

    returnVariables = []
    listOfInputs = []
    private = None
    static = None
    block = []
    name = None

    def __init__(self,name,private,block,returnVariable,listOfInputs,static=None):
        self.name = Word(name)
        self.private = private
        self.returnVariable = returnVariable
        self.listOfInputs = listOfInputs
        self.static = static
        self.block = block

    def getReturnVariable(self):
        return self.returnVariable

    def getListOfInputs(self):
        return self.listOfInputs

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getListOfVariables(self):
        return self.listOfInputs
