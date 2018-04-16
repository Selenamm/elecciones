class Canton:
    name = ""
    districtList = []

    def __init__(self,name):
        self.name = name

    def addDistrict(self,newDistrict):
        self.districtList.append(newDistrict)


    def getdistrictList(self):
        return self.districtList
