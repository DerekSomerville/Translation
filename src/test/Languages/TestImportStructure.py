import unittest
from src.main.Languages.ImportStructure import ImportStructure
from src.main.Languages.Python.PythonConstants import *

class TestImportStructure(unittest.TestCase):
    def testIsBaseClass(self):
        importStructure = ImportStructure("unittest.TestCase")
        importStructure.setBaseClasses(baseClasses)
        self.assertTrue(importStructure.isBaseClass())

    def testIsBaseClass(self):
        importStructure = ImportStructure("src.main.Language.ImportStructure")
        importStructure.setBaseClasses(baseClasses)
        self.assertFalse(importStructure.isBaseClass())

    def testGetClassName(self):
        importStructure = ImportStructure("src.main.Language.ImportStructure")
        importStructure.setBaseClasses(baseClasses)
        result = importStructure.getClassName()
        self.assertEqual(result,"ImportStructure")

    def testGetClassNameWithBaseClass(self):
        importStructure = ImportStructure("unittest.TestCase")
        importStructure.setBaseClasses(baseClasses)
        result = importStructure.getClassName()
        self.assertEqual(result,"unittest.TestCase")

    def testGetClassNameWithNone(self):
        importStructure = ImportStructure("")
        result = importStructure.getClassName()
        self.assertEqual(result,"")

    def testGenerateImport(self):
        importStructure = ImportStructure("src.main.Language.ImportStructure")
        result = importStructure.generateImport()
        self.assertEqual(result,"from src.main.Language.ImportStructure import ImportStructure")

    def testGenerateImportWithBaseClass(self):
        importStructure = ImportStructure("unittest.TestCase")
        importStructure.setBaseClasses(baseClasses)
        result = importStructure.generateImport()
        self.assertEqual(result,"import unittest")

    def testIsEmpty(self):
        importStructure = ImportStructure("")
        self.assertTrue(importStructure.isEmpty())

    def testIsNotEmpty(self):
        importStructure = ImportStructure("src.main.Language.ImportStructure")
        self.assertFalse(importStructure.isEmpty())

    def main():
        unittest.main()

if __name__ == "__main__":
    TestImportStructure.main()
