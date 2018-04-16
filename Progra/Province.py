from Progra import Canton,District

class Province:
    name = ""
    deputyNumber = 0
    cantonList =[]

    def __init__(self,name,deputyNumber):
        self.name = name
        self.deputyNumber = deputyNumber

    def addCanton(self,newCanton):
        self.cantonList.append(newCanton)

    def getCantonList(self):
        return self.cantonList