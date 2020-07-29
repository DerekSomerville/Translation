from src.main.Languages.VariableStructure import VariableStructure
import unittest

class TestVariableStructure(unittest.TestCase):

    variableStructure = VariableStructure("method",False,"String")

    def testGetClassPrivate(self):
        self.assertFalse(self.variableStructure.getPrivate())

    def testGetClassName(self):
        self.assertEqual("method",self.variableStructure.getName())

    def testGetVariableType(self):
        result = self.variableStructure.getVariableType()
        self.assertEqual(result,"String")

    def main():
        unittest.main()

if __name__ == "__main__":
    TestVariableStructure.main()
