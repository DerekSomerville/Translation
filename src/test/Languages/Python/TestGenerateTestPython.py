from src.main.Languages.Python.GenerateTestPython import GenerateTestPython
import unittest
class TestGenerateTestPython(unittest.TestCase):
    generateTestPython = GenerateTestPython()
    def testReadLine(self):
        self.generateTestPython.readLine(self)
        self.assertEqual(,)
    def testCreateWriteFile(self):
        self.generateTestPython.createWriteFile(self)
        self.assertEqual(,)
    def testOutputAppend(self):
        self.generateTestPython.outputAppend(self)
        self.assertEqual(,)
    def testOutputTestClass(self):
        self.generateTestPython.outputTestClass(self)
        self.assertEqual(,)
    def testGenerateImportClass(self):
        importClass.generateImport = self.generateTestPython.generateImportClass(self)
        self.assertEqual(importClass.generateImport,)
    def testStartTestFile(self):
        output = self.generateTestPython.startTestFile(self)
        self.assertEqual(output,)
    def testEndTestFile(self):
        self.generateTestPython.endTestFile(self)
        self.assertEqual(,)
    def testGetTestFunctions(self):
        functions = self.generateTestPython.getTestFunctions(self)
        self.assertEqual(functions,)
    def testGetReturnVariable(self):
        name = self.generateTestPython.getReturnVariable(self)
        self.assertEqual(name,)
    def testGenerateFunctionString(self):
        functionString = self.generateTestPython.generateFunctionString(self)
        self.assertEqual(functionString,)
    def testGenerateTestFunctions(self):
        self.generateTestPython.generateTestFunctions(self)
        self.assertEqual(,)
    def testGetFullFilePath(self):
        self.testFilePrefix = self.generateTestPython.getFullFilePath(self)
        self.assertEqual(self.testFilePrefix,)
    def testGeneratePythonTest(self):
        self.generateTestPython.generatePythonTest(self)
        self.assertEqual(,)
    def main():
        unittest.main()
if __name__ == "__main__":
    TestGenerateTestPython.main()
