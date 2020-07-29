import unittest
from src.main.Utilities.Lines import Lines
from src.main.Utilities.Word import Word

class TestLines(unittest.TestCase):
    line = Lines("Hello World")

    def testGetWordsFunction(self):
        self.line.setLine("def createFunction(self,functionName,block,returnVariable,listOfInputs):")
        self.assertEqual(len(self.line.getWords()),7)

    def testGetWordsBrackets(self):
        self.line.setLine("Hello [World] (hello, world):")
        self.assertEqual(['Hello', 'World', 'hello', 'world'],self.line.getWords())

    def testGetWordsImport(self):
        self.line.setLine("import EntitiesDataSourceMapping.DataBaseSetup;")
        self.assertEqual(["import","EntitiesDataSourceMapping","DataBaseSetup"],self.line.getWords())

    def testRemoveZeroLengthWords(self):
        self.assertEqual(["Frank","Kitty"],self.line.removeZeroLengthWords(["Frank","","Kitty"]))

    def testConvertToWords(self):
        frankAsString = "Frank"
        kittyAsString = "Kitty"
        frankAsWord = Word(frankAsString)
        kittyAsWord = Word(kittyAsString)
        self.assertEqual([frankAsWord,kittyAsWord],self.line.convertToWords([frankAsString,kittyAsString]))

    def testGenerateWords(self):
        frankAsString = "Frank"
        kittyAsString = "Kitty"
        self.line.line = frankAsString + " " + kittyAsString
        frankAsWord = Word(frankAsString)
        kittyAsWord = Word(kittyAsString)
        self.line.generateWords()
        self.assertEqual([frankAsWord,kittyAsWord],self.line.words)

    def testGetWords(self):
        frankAsString = "Frank"
        kittyAsString = "Kitty"
        self.line.line = frankAsString + " " + kittyAsString
        frankAsWord = Word(frankAsString)
        kittyAsWord = Word(kittyAsString)
        self.line.generateWords()
        self.assertEqual([frankAsWord,kittyAsWord],self.line.getWords())

    def main():
        print("TestLines")
        unittest.main()

if __name__ == "__main__":
    TestLines.main()
