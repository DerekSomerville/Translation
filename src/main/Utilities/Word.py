class Word(str):

    word = ""

    def __init__(self,word):
        self.word = word

    def firstLetterLowerCase(self):
        return self.word[0].lower() + self.word[1:]

    def firstLetterUpperCase(self):
        return self.word[0].upper() + self.word[1:]
