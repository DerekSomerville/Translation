from src.main.Languages.Java.JavaImportDetermine import JavaImportDetermine
from src.main.Utilities.Lines import Lines

import unittest

class TestJavaImportDetermine(unittest.TestCase):
    javaImportDetermine = JavaImportDetermine()

    def testIsAnImport(self):
        line = Lines("import java.src.PlayerInterface;")
        self.assertTrue(self.javaImportDetermine.isAnImport(line))

    def testNotIsAnImport(self):
        line = Lines("public class BlackGammon {")
        self.assertFalse(self.javaImportDetermine.isAnImport(line))

    def testGenerateImportStructure(self):
        line = Lines("import java.src.PlayerInterface;")
        importStructure = self.javaImportDetermine.generateImportStructure(line)
        self.assertEqual(importStructure.getClassName(),"PlayerInterface")

    def main():
        unittest.main()
if __name__ == "__main__":
    TestJavaImportDetermine.main()
