from src.main.Languages.LanguageConstants import *

class TranslateLanguage:

    convertFolder = None
    fromLanguage = None
    toLanguage = None

    def __init__(self,convertFolder,fromLanguage,toLanguage):
        self.convertFolder = convertFolder
        self.fromLanguage = fromLanguage
        self.toLanguage = toLanguage

    def translate(self):
