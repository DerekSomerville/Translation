import unittest
from src.main.Languages.Java.JavaClassDetermine import JavaClassDetermine
from src.main.Utilities.Lines import Lines
from src.main.Languages.ClassStructure import ClassStructure
from src.main.Languages.ImportStructure import ImportStructure

class TestJavaClass(unittest.TestCase):
    line = Lines("public class InputConsole extends InputInterface {")
    javaClass = JavaClassDetermine(line)

    def testGetNextWord(self):
        result = self.javaClass.getNextWord("public")
        self.assertEqual(result,"class")

    def testGetName(self):
        result = self.javaClass.getName()
        self.assertEqual("InputConsole",result)

    def testGetExtended(self):
        result = self.javaClass.getExtended()
        self.assertEqual("InputInterface",result)

    def testIsPublic(self):
        result = self.javaClass.isPrivate()
        self.assertFalse(result)

    def testGetClassPrivate(self):
        result = self.javaClass.getClass()
        self.assertFalse(result.getPrivate())

    def testGetClassName(self):
        result = self.javaClass.getClass()
        self.assertEqual("InputConsole",result.getName())

    def testGetClassExtends(self):
        result = self.javaClass.getClass()
        self.assertEqual(ImportStructure("InputInterface").getClassName(),result.getExtends().getClassName())

    def main():
        print("TestJavaClass")
        unittest.main()

if __name__ == "__main__":
    TestJavaClass.main()
