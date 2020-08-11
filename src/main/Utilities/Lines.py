import re
#from src.test.Utilities.TestLines import TestLines
from src.main.Utilities.Word import Word

class Lines:
    line = ""
    words = []

    def __init__(self,line):
        self.line = line

    def setLine(self,line):
        self.line = line
        self.words = []

    def removeZeroLengthWords(self,initialWords):
        words = []
        for word in initialWords:
            if len(word) > 0:
                words.append(word)
        return words

    def getLine(self):
        return self.line

    def convertToWords(self,stringWords):
        words = []
        for word in stringWords:
            newWord = Word(word)
            words.append(newWord)
        return words

    def replace(self,toBeReplaced,replacedWith):
        self.line = self.line.replace(toBeReplaced,replacedWith)

    def generateWords(self):
        initialWords = re.split(' |,|-|_|!|:|;|\.|\(|\)|\[|\]', self.line)
        noZeroWords = self.removeZeroLengthWords(initialWords)
        self.words = self.convertToWords(noZeroWords)

    def getWords(self):
        if len(self.words) == 0:
            self.generateWords()
        return self.words

def main():
    #TestLines.main()
    pass

if __name__ == "__main__":
    main()
