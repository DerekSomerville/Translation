import unittest
from src.test.Languages.Java.TestJavaClass import TestJavaClass
#from src.test.Languages.Python.TestGenerateTestPython import TestGenerateTestPython
from src.test.Languages.Python.TestPythonClass import TestPythonClass
from src.test.Languages.Python.TestPythonMethodDetermine import TestPythonMethodDetermine
from src.test.Languages.TestClassStructure import TestClassStructure
from src.test.Languages.TestDeclareStructure import TestDeclareStructure
from src.test.Languages.TestImportStructure import TestImportStructure
from src.test.Languages.TestMethodStructure import TestMethodStructure
from src.test.Languages.TestVariableStructure import TestVariableStructure
from src.test.Utilities.TestLines import TestLines
from src.test.Utilities.TestWord import TestWord


class TestAll:

    def testAll():
        TestJavaClass.main()
        #TestGenerateTestPython.main()
        TestPythonClass.main()
        TestPythonMethodDetermine.main()
        TestClassStructure.main()
        TestDeclareStructure.main()
        TestImportStructure.main()
        TestMethodStructure.main()
        TestVariableStructure.main()
        TestLines.main()
        TestWord.main()



if __name__ == "__main__":
    TestAll.testAll()

