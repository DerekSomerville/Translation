from src.main.Languages.LanguageConstants import *
from src.main.Languages.TranslateLanguage import TranslateLanguage
class Main:

    def generateRequest(self,listOfRequest):
        request = "Please select "
        for counter in range(len(listOfRequest)):
            request += " " + str(counter) + " - " + listOfRequest[counter]
        return request

    def requestNewLanguage(self):
        return input(self.generateRequest(listOfLanguages))

    def getNewLanguage(self):
        return self.requestNewLanguage()

    def getFolder(self):
        return input("Please provide folder to covert")

    def main(self):
        print("Provide From Language")
        fromLanguage = self.getNewLanguage()
        print("Provide New Language")
        newLanguage = self.getNewLanguage()
        folder = self.getFolder()
        translateLanguage = TranslateLanguage(folder,fromLanguage,newLanguage)
        translateLanguage.translate()

def main():
    main = Main()
    main.main()

if __name__ == "__main__":
    main()
