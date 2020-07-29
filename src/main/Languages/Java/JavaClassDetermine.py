from src.main.Languages.ClassStructure import ClassStructure
from src.main.Languages.ImportStructure import ImportStructure

class JavaClassDetermine:
    line = None

    def __init__(self,line):
        self.line = line

    def setLine(self,line):
        self.line = line

    def isPrivate(self):
        return self.line.getWords()[0] == "private"

    def getNextWord(self,word):
        return self.line.getWords()[self.line.getWords().index(word)+1]

    def getExtended(self):
        extends = None
        if "extends" in self.line.getWords():
            extends = self.getNextWord("extends")
        return extends

    def getName(self):
        name = ""
        if "class" in self.line.getWords():
            self.name = self.getNextWord("class")
        return self.name

    def getClass(self):
        classStructure = ClassStructure(self.getName(),self.isPrivate(),ImportStructure(self.getExtended()))
        return classStructure

