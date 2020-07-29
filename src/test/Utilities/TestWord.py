from src.main.Utilities.Word import Word
import unittest
class TestWord(unittest.TestCase):

    def testFirstLetterLowerCase(self):
        word = Word("LowerCase")
        result = word.firstLetterLowerCase()
        self.assertEqual(result,"lowerCase")

    def testFirstLetterUpperCase(self):
        word = Word("upperCase")
        result = word.firstLetterUpperCase()
        self.assertEqual(result,"UpperCase")

    def main():
        unittest.main()

if __name__ == "__main__":
    TestWord.main()
