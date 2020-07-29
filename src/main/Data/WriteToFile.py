class WriteToFile:
    # Here will be the instance stored.
    file = ""
    filePathPrefix = "resource/"
    directory = ""
    fileName = ""

    def __init__(self,directory,fileName,append=True,filePathPrefix="resource/"):
        self.directory = directory
        self.fileName = fileName
        self.filePathPrefix = filePathPrefix
        writePermission = "w"
        if append:
            writePermission = "a"
        self.file = open(self.filePathPrefix + self.directory+ self.fileName,writePermission)

    def setFilePathPrefix(self,directory):
        self.filePathPrefix = directory

    def writeToFile(self,logItem):
        self.file.write(str(logItem) + "\n")
