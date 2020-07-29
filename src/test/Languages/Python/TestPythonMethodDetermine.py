from src.main.Languages.Python.PythonMethodDetermine import PythonMethodDetermine
from src.main.Utilities.Lines import Lines
import unittest
class TestPythonMethodDetermine(unittest.TestCase):
    pythonMethodDetermine = PythonMethodDetermine([["  def method(self,Param1,Param2)"]])
    def testCreateFunctionLength(self):
        initialLength = len(self.pythonMethodDetermine.functions)
        self.pythonMethodDetermine.createFunction("method",[],None,[])
        self.assertEqual(initialLength+1,len(self.pythonMethodDetermine.functions))

    def testCreateFunctionName(self):
        initialLength = len(self.pythonMethodDetermine.functions)
        self.pythonMethodDetermine.createFunction("method",[],None,[])
        self.assertEqual(self.pythonMethodDetermine.functions[-1].getName(),"method")

    def testGetListOfInputsSelf(self):
        functionList = ["def", "method", "self", "Param"]
        words = self.pythonMethodDetermine.getListOfInputs(functionList)
        self.assertEqual(words,["Param"])

    def testGetListOfInputsNoSelf(self):
        functionList = ["def", "method", "Param1", "Param2"]
        words = self.pythonMethodDetermine.getListOfInputs(functionList)
        self.assertEqual(words,["Param1","Param2"])

    def testProcessMethodLineFunction(self):
        line = Lines("  def method(self,Param1,Param2)")
        self.pythonMethodDetermine.processMethodLine(line)
        self.assertEqual(self.pythonMethodDetermine.functionName,"method")

    def testProcessMethodLineStartMethod(self):
        line = Lines("  def method(self,Param1,Param2)")
        self.pythonMethodDetermine.processMethodLine(line)
        self.assertTrue(self.pythonMethodDetermine.startOfMethod)

    def testProcessMethodLineFunction(self):
        line = Lines("  def method(self,Param1,Param2)")
        self.pythonMethodDetermine.processMethodLine(line)
        self.assertEqual(self.pythonMethodDetermine.listOfInputs,["Param1","Param2"])

    def testGenerateFunctions(self):
        self.pythonMethodDetermine.functions = []
        self.pythonMethodDetermine.lines = ["  def method(self,Param1,Param2)"]
        self.pythonMethodDetermine.generateFunctions()
        self.assertEqual(self.pythonMethodDetermine.functions[-1].getName(),"method")

    def testGetFunctions(self):
        functions = self.pythonMethodDetermine.getFunctions()
        self.assertEqual(self.pythonMethodDetermine.functions,functions)

    def main():
        unittest.main()

if __name__ == "__main__":
    TestPythonMethodDetermine.main()
