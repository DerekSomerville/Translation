import unittest
from src.main.Languages.ClassStructure import ClassStructure
from src.main.Languages.ImportStructure import ImportStructure
class TestClassStructure(unittest.TestCase):
    classStructure = ClassStructure("InputConsole",False,ImportStructure("InputInterface"))

    def testGetClassPrivate(self):
        self.assertFalse(self.classStructure.getPrivate())

    def testGetClassName(self):
        self.assertEqual("InputConsole",self.classStructure.getName())

    def testGetClassExtends(self):
        self.assertEqual("InputInterface",self.classStructure.getExtends().getClassName())

    def testGetClassExtendsFromString(self):
        classStructure = ClassStructure("InputConsole",False,"InputInterface")
        self.assertEqual("InputInterface",classStructure.getExtends().getClassName())

    def testGetClassExtendsFromNone(self):
        classStructure = ClassStructure("InputConsole",False)
        self.assertEqual("",classStructure.getExtends().getClassName())

    def testSetBaseClasses(self):
        self.classStructure.setBaseClasses(["unittest"])
        self.assertEqual(["unittest"],self.classStructure.extends.baseClasses)

    def testGetClassExtendsWithBase(self):
        classStructure = ClassStructure("InputConsole",False,"unittest.TestCase")
        classStructure.setBaseClasses(["unittest"])
        self.assertEqual("unittest.TestCase",classStructure.getExtends().getClassName())

    def main():
        print("TestClassStructure")
        unittest.main()

if __name__ == "__main__":
    TestClassStructure.main()
