from src.main.Data.ReadCSVFile import ReadCSVFile
from src.main.Data.WriteToFile import WriteToFile
from src.main.Utilities.Lines import Lines
from src.main.Languages.Python.PythonClassGenerate import PythonClassGenerate
from src.main.Languages.ClassStructure import ClassStructure
from src.main.Languages.ImportStructure import ImportStructure
from src.main.Utilities.Word import Word
from src.main.Languages.Python.PythonMethodDetermine import PythonMethodDetermine
import os

class GeneratePythonTest:

    writeFile = None
    fromFilePrefix = "src/main/"
    testFilePrefix = "src/test/"
    directory = ""
    fileName = ""
    originalClassName = ""
    lines = []
    output = []

    def __init__(self,directory,fileName):
        self.directory = directory
        self.fileName = fileName
        self.originalClassName = Word(self.fileName.split(".")[0])
        self.readLine(self.fromFilePrefix + self.directory + self.fileName)

    def readLine(self, fileName):
        readFile = open(fileName, "r")
        self.lines = readFile.readlines()
        readFile.close()

    def createWriteFile(self):
        self.writeFile = WriteToFile(self.directory,"Test" + self.fileName,False,self.testFilePrefix)

    def outputAppend(self,ListOfOutput):
        for row in ListOfOutput:
            self.output.append(row)

    def outputTestClass(self):
        for row in self.output:
            self.writeFile.writeToFile(row)


    def generateImportClass(self):
        classPath = self.fromFilePrefix + self.directory + self.originalClassName
        importClass = ImportStructure(classPath.replace("/","."))
        return importClass.generateImport()

    def startTestFile(self):
        output = []
        output.append(self.generateImportClass() )
        testClassStructure = ClassStructure("Test" + self.originalClassName.firstLetterUpperCase(),False,"unittest.TestCase")
        testPythonClass = PythonClassGenerate(testClassStructure)
        output.append(testPythonClass.generateExtendImport())
        output.append(testPythonClass.generateClass())
        output.append("    " + self.originalClassName.firstLetterLowerCase() + " = " + self.originalClassName + "()")
        return output

    def endTestFile(self):
        output = []
        output.append("    def main():")
        output.append("        unittest.main()")
        output.append('if __name__ == "__main__":')
        output.append('    Test' + self.originalClassName + '.main()')
        return output

    def getTestFunctions(self,functions):
        nonTestFunctions = ["init","main"]
        for function in functions:
            if function.getName() in nonTestFunctions:
                functions.remove(function)
        return functions

    def getReturnVariable(self,function):
        name = ""
        if not function.getReturnVariable() == None:
            name = function.getReturnVariable().getName()
        return name

    def generateFunctionString(self,function):
        if self.getReturnVariable(function) == "":
            functionString = ""
        else:
            functionString = self.getReturnVariable(function) + " = "
        functionString += "self." + self.originalClassName.firstLetterLowerCase() + "." + function.getName()
        functionString += "(" + ",".join(function.getListOfInputs()) + ")"
        return functionString

    def generateTestFunctions(self):
        output = []
        methodDetermine = PythonMethodDetermine(self.lines)
        functions = self.getTestFunctions(methodDetermine.getFunctions())
        for function in functions:
            output.append("    def test"+function.getName().firstLetterUpperCase()+"(self):")
            output.append("        " + self.generateFunctionString(function))
            output.append("        self.assertEqual(" + self.getReturnVariable(function) + ","")")
            output.append("")
        return output

    def getFullFilePath(self):
        return self.testFilePrefix + self.directory + "Test" + self.fileName

    def generatePythonTest(self):
        if not os.path.exists(self.getFullFilePath()):
            self.outputAppend(self.startTestFile())
            self.outputAppend(self.generateTestFunctions())
            self.outputAppend(self.endTestFile())
            self.createWriteFile()
            self.outputTestClass()
        else:
            print("File already exists")
def main():
    print(os.getcwd())
    os.chdir('C:/Users/Derek/Documents/GitHub/Translation/')
    generateTestPython = GeneratePythonTest("Languages/Java/","JavaImportDetermine.py")
    generateTestPython.generatePythonTest()

if __name__ == "__main__":
    main()
