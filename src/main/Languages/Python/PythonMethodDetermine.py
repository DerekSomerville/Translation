from src.main.Languages.MethodStructure import MethodStructure
from src.main.Languages.VariableStructure import VariableStructure
from src.main.Utilities.Lines import Lines
class PythonMethodDetermine():

    lines = []
    functions = []
    startOfMethod = False
    functionName = ""
    listOfInputs = []
    returnVariable = None
    startAtLine = 0
    block = []

    def __init__(self,lines,startAtLine=0):
        self.lines = lines
        self.startAtLine = startAtLine

    def createFunction(self,functionName,block,returnVariable,listOfInputs):
        function = MethodStructure(functionName,False,block,returnVariable,listOfInputs)
        self.functions.append(function)

    def getListOfInputs(self,words):
        counter = 2
        if words[counter] == "self":
            counter += 1
        return words[counter:]

    def processMethodLine(self,line):
        words = line.getWords()
        if "def" in words:
            if self.startOfMethod and len(self.functionName) > 1:
                self.createFunction(self.functionName,self.block,self.returnVariable,self.listOfInputs)
                self.returnVariable = None
                self.block = []
            self.startOfMethod = True
            self.functionName = words[1]
            self.listOfInputs = self.getListOfInputs(words)
        #elif "=" in words and words[0] != "self":
        #    self.append(VariableStructure(line.getWords()[0],None))
        elif "return" in line.getWords():
            self.returnVariable = VariableStructure(line.getWords()[1],None)
            self.block.append(line)
        else:
            self.block.append(line)

    def generateFunctions(self):
        line = Lines("")
        for counter in range(self.startAtLine,len(self.lines)):
            row = self.lines[counter]
            if len(row) > 0:
                line.setLine(row.rstrip("\n"))
                self.processMethodLine(line)
        if self.startOfMethod:
            self.createFunction(self.functionName,self.block,self.returnVariable,self.listOfInputs)

    def getFunctions(self):
        if len(self.functions) == 0:
            self.generateFunctions()
        return self.functions
