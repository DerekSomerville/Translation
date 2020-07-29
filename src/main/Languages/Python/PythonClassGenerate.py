from src.main.Languages.ClassStructure import ClassStructure
from src.main.Data.WriteToFile import WriteToFile
from src.main.Languages.Python.PythonConstants import *

class PythonClassGenerate:

    classStructure = None

    def __init__(self,classStructure):
        classStructure.setBaseClasses(baseClasses)
        self.classStructure = classStructure

    def getExtendsClassName(self):
        return self.classStructure.getExtends().getClassName()

    def generateExtendImport(self):
        return self.classStructure.getExtends().generateImport()

    def generateClass(self):
        classString = "class " + self.classStructure.name
        extends = self.classStructure.getExtends()
        if extends.isPresent():
            classString += "(" + self.getExtendsClassName() + ")"
        classString += ":"
        return classString


