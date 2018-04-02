from Progra import Canton,District

class Province:
    name = ""
    deputyNumber = 0
    cantonList = []

    def __init__(self,name,deputyNumber):
        self.name = name
        self.deputyNumber = deputyNumber

    def addCanton(self,canton):
        self.cantonList.append(canton)

    def getCantonList(self):
        return self.cantonList