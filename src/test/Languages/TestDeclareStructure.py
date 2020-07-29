from src.main.Languages.DeclareStructure import DeclareStructure
import unittest

class TestDeclareStructure(unittest.TestCase):

    declareStructure = DeclareStructure("method",False)

    def testGetName(self):
        result = self.declareStructure.getName()
        self.assertEqual(result,"method")

    def testGetPrivate(self):
        result = self.declareStructure.getPrivate()
        self.assertFalse(result)

    def main():
        unittest.main()

if __name__ == "__main__":
    TestDeclareStructure.main()
