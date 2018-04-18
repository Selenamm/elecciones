from Progra import Canton,District

class Province:
    name = ""
    deputyNumber = 0
    legislative = 0

    cantonList =[]

    def __init__(self,name,deputyNumber,legistative):
        self.name = name
        self.deputyNumber = deputyNumber
        self.legislative = legislative

    def addCanton(self,newCanton):
        self.cantonList.append(newCanton)

    def getCantonList(self):
        return self.cantonList

    #def addPartieLegislativeProvince(self,legislative):
     #   self.legislative = legislative