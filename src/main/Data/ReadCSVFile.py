import csv
import subprocess
import os

class ReadCSVFile :

    filePathPrefix = "resource/"

    def setFilePathPrefix(self,directory):
        self.filePathPrefix = directory

    def getFileData(self, directory,  fileName):
        fileData = []
        with open(self.filePathPrefix + directory + fileName,'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getLastLines(self,directory, fileName, numerOfLines):
        return self.getFileData(directory, fileName)[-1*numerOfLines]
