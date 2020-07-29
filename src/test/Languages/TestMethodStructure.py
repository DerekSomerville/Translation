from src.main.Languages.MethodStructure import MethodStructure
from src.main.Languages.VariableStructure import VariableStructure
import unittest

class TestMethodStructure(unittest.TestCase):

    returnVariable = VariableStructure("result",None,"String")
    listOfInput = [returnVariable]
    methodStructure = MethodStructure("method",False,[],returnVariable,listOfInput)

    def testGetClassPrivate(self):
        self.assertFalse(self.methodStructure.getPrivate())

    def testGetClassName(self):
        self.assertEqual("method",self.methodStructure.getName())

    def testGetReturnVariable(self):
        result = self.methodStructure.getReturnVariable()
        self.assertEqual(result,self.returnVariable)

    def testGetListOfVariables(self):
        result = self.methodStructure.getListOfVariables()
        self.assertEqual(result,self.listOfInput)

if __name__ == "__main__":
    TestMethodStructure.main()
