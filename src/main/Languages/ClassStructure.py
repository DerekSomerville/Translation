from src.main.Languages.ImportStructure import ImportStructure
from src.main.Languages.DeclareStructure import DeclareStructure

class ClassStructure(DeclareStructure):

    extends = None


    def __init__(self,name,private,extends=None):
        self.name = name
        self.private = private
        if type(extends) == str or extends == None:
            self.extends = ImportStructure(extends)
        else:
            self.extends = extends

    def setBaseClasses(self,baseClasses):
        self.extends.setBaseClasses(baseClasses)

    def getExtends(self):
        return self.extends

def main():
    classStructure = ClassStructure("method",False)
    print(classStructure.getName())

if __name__ == "__main__":
    main()
