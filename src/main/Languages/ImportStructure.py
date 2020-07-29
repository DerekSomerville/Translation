class ImportStructure:

    fullClassPath = ""
    baseClasses = []

    def __init__(self,fullClassPath):
        self.fullClassPath = fullClassPath

    def setBaseClasses(self,baseClassess):
        self.baseClasses = baseClassess

    def isBaseClass(self):
        return not self.fullClassPath == None and self.fullClassPath.split(".")[0] in self.baseClasses

    def getClassName(self):
        if self.fullClassPath == "" or self.fullClassPath == None:
            className = ""
        elif self.isBaseClass():
            className = self.fullClassPath
        else:
            className = self.fullClassPath.split(".")[-1]
        return className

    def generateImport(self):
        if self.fullClassPath == "" or self.fullClassPath == None:
            importString = ""
        elif self.isBaseClass():
            importString = "import " + self.fullClassPath.split(".")[0]
        else:
            importString = "from " + self.fullClassPath + " import " + self.getClassName()
        return importString

    def isEmpty(self):
        return "" == self.getClassName()

    def isPresent(self):
        return not self.isEmpty()
