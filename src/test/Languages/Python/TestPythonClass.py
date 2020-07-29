import unittest
from src.main.Languages.Python.PythonClassGenerate import PythonClassGenerate
from src.main.Languages.ClassStructure import ClassStructure
from src.main.Languages.ImportStructure import ImportStructure
from src.main.Data.WriteToFile import WriteToFile

class TestPythonClass(unittest.TestCase):

    def testGenerateClassExtends(self):
        classStructure = ClassStructure("InputConsole",False,ImportStructure("InputInterface"))
        pythonClass = PythonClassGenerate(classStructure)
        self.assertEqual(pythonClass.generateClass(),"class InputConsole(InputInterface):")

    def testGenerateClassNoExtends(self):
        classStructure = ClassStructure("InputConsole",False)
        pythonClass = PythonClassGenerate(classStructure)
        self.assertEqual(pythonClass.generateClass(),"class InputConsole:")

    def testGetExtendsClassNameWithExtends(self):
        classStructure = ClassStructure("InputConsole",False,ImportStructure("InputInterface"))
        pythonClass = PythonClassGenerate(classStructure)
        self.assertEqual(pythonClass.getExtendsClassName(),"InputInterface")

    def testGetExtendsClassNameNoExtends(self):
        classStructure = ClassStructure("InputConsole",False)
        pythonClass = PythonClassGenerate(classStructure)
        self.assertEqual(pythonClass.getExtendsClassName(),"")

    def testGenerateExtendImport(self):
        classStructure = ClassStructure("InputConsole",False,ImportStructure("src.main.Language.Python.PythonClass"))
        pythonClass = PythonClassGenerate(classStructure)
        self.assertEqual(pythonClass.generateExtendImport(),"from src.main.Language.Python.PythonClass import PythonClass")

    def main():
        print("TestPythonClass")
        unittest.main()

if __name__ == "__main__":
    TestPythonClass.main()
