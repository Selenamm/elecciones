class Canton:
    name = ""
    districtList = []

    def __init__(self,name):
        self.name = name

    def addDistrict(self,district):
        self.districtList.append(district)