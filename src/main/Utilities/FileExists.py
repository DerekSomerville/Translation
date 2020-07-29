import os

class FileExists:

    directoryPath = ""
    fileName = ""

    def __init__(self,directoryPath,fileName):
        self.directoryPath = directoryPath
        self.fileName = fileName

    def fileExists(self):
        return os.path.exists(self.directoryPath + self.fileName)

    def directoryExists(self):
        return os.path.exists(self.directoryPath)

    def createDirectory(self):
        os.mkdir(self.directoryPath)
