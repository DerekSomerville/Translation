class DeclareStructure:

    name = ""
    private = False

    def __init__(self,name,private,extends=None):
        self.name = name
        self.private = private

    def getName(self):
        return self.name

    def getPrivate(self):
        return self.private


def main():
    declareStructure = DeclareStructure("method",False)
    print(declareStructure.getName())

if __name__ == "__main__":
    main()
